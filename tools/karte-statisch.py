#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Schreibt die aktuelle Wochenkarte als statisches HTML in index.html.

Warum das nötig ist
-------------------
Die Seite lädt die Wochenkarte per JavaScript aus Firestore (Dokument
website/streetfood_karte, gepflegt über streetfood-karte.html im Eventkalender).
Für Besucher ist das ideal — für Suchmaschinen nur halb: Googlebot rendert
JavaScript verzögert, die Crawler von ChatGPT, Perplexity und Claude in der
Regel gar nicht. Ohne diesen Lauf steht im ausgelieferten HTML dauerhaft die
Platzhalter-Karte aus der Bauphase, also erfundene Gerichte zu erfundenen
Preisen.

Dieses Skript holt dieselben Daten über die Firestore-REST-Schnittstelle und
trägt sie zwischen den Markern <!--karte:X--> und <!--/karte:X--> ein. Das
JavaScript bleibt unangetastet und überschreibt den Inhalt im Browser weiterhin
mit dem Live-Stand — statisch ist also nur die Rückfallebene, die aber jetzt
echte Gerichte enthält.

Das erzeugte Markup entspricht exakt dem, was das Skript am Seitenende im
Browser erzeugt. Ändert sich das eine, muss das andere mit.

Aufruf: python3 tools/karte-statisch.py [--pruefen]
  ohne Argument  schreibt index.html
  --pruefen      meldet nur, ob sich etwas ändern würde (Exit 1 = Änderung)
"""

import html
import json
import os
import re
import sys
import urllib.error
import urllib.request

WURZEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEITE = os.path.join(WURZEL, "index.html")

PROJEKT = "red-lotus-eventkalender"
DATENBANK = "default"        # benannte Datenbank, NICHT "(default)" — häufige Stolperfalle
SAMMLUNG = "website"
DOKUMENT = "streetfood_karte"

STAEDTE = {"BKK": "BANGKOK", "SEL": "SEOUL", "TYO": "TOKYO",
           "HAN": "HANOI", "HKG": "HONGKONG"}


class Stoerung(Exception):
    """Dienst nicht erreichbar — im Unterschied zu 'Dokument gibt es nicht'."""


def api_schluessel(quelle: str) -> str:
    """Liest den öffentlichen Web-API-Schlüssel aus index.html.

    Bewusst kein zweiter Ablageort: Der Schlüssel steht ohnehin im
    ausgelieferten Clientcode. Wird er dort getauscht, zieht dieses Skript
    automatisch nach.
    """
    treffer = re.search(r'firestore\.googleapis\.com[^"]*?key=([A-Za-z0-9_\-]+)', quelle)
    if not treffer:
        raise SystemExit("Kein Firestore-Schlüssel in index.html gefunden — URL geändert?")
    return treffer.group(1)


def esc(text: str) -> str:
    """Entspricht dem esc() im Browser (textContent -> innerHTML)."""
    return html.escape(text or "", quote=False)


def karte_holen(schluessel: str) -> dict:
    url = (f"https://firestore.googleapis.com/v1/projects/{PROJEKT}"
           f"/databases/{DATENBANK}/documents/{SAMMLUNG}/{DOKUMENT}?key={schluessel}")
    try:
        with urllib.request.urlopen(url, timeout=20) as antwort:
            return json.load(antwort)
    except urllib.error.HTTPError as fehler:
        if fehler.code == 404:
            return {}          # Dokument existiert (noch) nicht — kein Fehlerfall
        raise Stoerung(f"Firestore antwortete mit HTTP {fehler.code}") from fehler
    except Exception as fehler:                      # Netz, DNS, Zeitüberschreitung
        raise Stoerung(str(fehler)) from fehler


def sv(feld) -> str:
    return (feld or {}).get("stringValue", "").strip()


def bv(feld) -> bool:
    return bool((feld or {}).get("booleanValue"))


def gerichte_lesen(felder: dict) -> list:
    roh = felder.get("gerichte", {}).get("arrayValue", {}).get("values", [])
    liste = []
    for eintrag in roh:
        g = eintrag.get("mapValue", {}).get("fields", {})
        name = sv(g.get("name"))
        if not name:
            continue
        liste.append({
            "name": name,
            "stempel": sv(g.get("stempel")),
            "beschreibung": sv(g.get("beschreibung")) or sv(g.get("zusatz")),
            "preis": sv(g.get("preis")),
            "vegan": bv(g.get("vegan")),
            "vegetarisch": bv(g.get("vegetarisch")),
            "glutenfrei": bv(g.get("glutenfrei")),
            "scharf": bv(g.get("scharf")),
            "db": bv(g.get("dauerbrenner")),
        })
    liste.sort(key=lambda g: 0 if g["db"] else 1)     # Dauerbrenner zuerst, sonst stabil
    return liste


# ---------- Markup-Bausteine, spiegelbildlich zum Browser-Skript ----------

def stempel_svg(code: str) -> str:
    stadt = STAEDTE.get(code)
    if not stadt:
        return ""
    return ('<svg width="64" height="64" viewBox="0 0 64 64" fill="none">'
            '<ellipse cx="32" cy="32" rx="29" ry="22" stroke="#F2C4BC" stroke-width="2" stroke-dasharray="4 3"/>'
            f'<text x="32" y="30" text-anchor="middle" fill="#F2C4BC" font-size="13" '
            f'font-family="Arial, sans-serif" font-weight="bold" letter-spacing="2">{esc(code)}</text>'
            f'<text x="32" y="42" text-anchor="middle" fill="#F2C4BC" font-size="7" '
            f'font-family="Arial, sans-serif" letter-spacing="1">{esc(stadt)}</text></svg>')


def dauerbrenner_svg() -> str:
    return ('<svg width="64" height="64" viewBox="0 0 64 64" fill="none">'
            '<circle cx="32" cy="32" r="29" stroke="#E0473A" stroke-width="2" stroke-dasharray="4 3"/>'
            '<text x="32" y="28" text-anchor="middle" fill="#E0473A" font-size="9" '
            'font-family="Arial, sans-serif" font-weight="bold" letter-spacing="1">IMMER</text>'
            '<text x="32" y="40" text-anchor="middle" fill="#E0473A" font-size="9" '
            'font-family="Arial, sans-serif" font-weight="bold" letter-spacing="1">AN BORD</text></svg>')


def chili_badge() -> str:
    return (' <span class="badge-chili" role="img" aria-label="scharf">'
            '<svg width="12" height="12" viewBox="0 0 16 16" fill="none" aria-hidden="true">'
            '<path d="M10.5 3.5c.3-1 .1-1.8-.5-2.5 1.8.2 2.8 1.2 3 3 .8 4.5-2 9-6.5 10.5C3.6 15.5 2 13.8 2 11.5c2.5 1 4.5.5 6-1.5 1.2-1.6 1.7-3.7 2.5-6.5Z" fill="#FF2E63"/>'
            '</svg>scharf</span>')


def mini_stempel(code: str) -> str:
    stadt = STAEDTE.get(code)
    if not stadt:
        return ""
    return ('<span aria-hidden="true" style="display:inline-flex">'
            '<svg width="46" height="34" viewBox="0 0 64 48" fill="none">'
            '<ellipse cx="32" cy="24" rx="29" ry="20" stroke="#F2C4BC" stroke-width="2.6" '
            'stroke-dasharray="4 3" transform="rotate(-6 32 24)"/>'
            f'<text x="32" y="30" text-anchor="middle" fill="#F2C4BC" font-size="17" '
            f'font-family="Arial, sans-serif" font-weight="bold" letter-spacing="2">{esc(code)}</text>'
            '</svg></span>')


def gerichte_html(gerichte: list) -> str:
    teile = []
    for i, g in enumerate(gerichte):
        stempel = dauerbrenner_svg() if g["db"] else stempel_svg(g["stempel"])
        zusatz = esc(g["beschreibung"])
        tags = []
        if g["vegan"]:
            tags.append("vegan")
        elif g["vegetarisch"]:                    # vegan impliziert vegetarisch
            tags.append("vegetarisch")
        if g["glutenfrei"]:
            tags.append("glutenfrei")
        for t in tags:
            zusatz += (" · " if zusatz else "") + f'<span class="badge-tag">{t}</span>'
        if g["scharf"]:
            zusatz += chili_badge()
        preis = esc(g["preis"])
        if preis and "€" not in preis:
            preis += " €"
        teile.append(
            '<div class="gericht">'
            f'<span class="gericht__stempel {"stempel--2" if i % 2 else "stempel"}" aria-hidden="true">{stempel}</span>'
            f'<p class="gericht__name"><span translate="no">{esc(g["name"])}</span>'
            + (f'<span class="gericht__zusatz">{zusatz}</span>' if zusatz else '')
            + f'</p><p class="gericht__preis">{preis}</p></div>'
        )
    return "\n".join(teile)


def ticker_html(gerichte: list) -> str:
    if len(gerichte) < 2:
        return ""
    einmal = "<span>·</span>".join(
        f'<span>{esc(g["name"])}</span>' + mini_stempel(g["stempel"]) for g in gerichte
    )
    return einmal + "<span>·</span>" + einmal + "<span>·</span>"


def ersetzen(quelle: str, marke: str, inhalt: str) -> str:
    muster = re.compile(f"(<!--karte:{marke}-->).*?(<!--/karte:{marke}-->)", re.S)
    if not muster.search(quelle):
        raise SystemExit(f"Marker karte:{marke} fehlt in index.html")
    return muster.sub(lambda m: m.group(1) + inhalt + m.group(2), quelle, count=1)


def main() -> int:
    nur_pruefen = "--pruefen" in sys.argv
    quelle = open(SEITE, encoding="utf-8").read()

    try:
        daten = karte_holen(api_schluessel(quelle))
    except Stoerung as fehler:
        # Wichtig: Bei einer Störung NICHTS anfassen. Eine kurzzeitig nicht
        # erreichbare Datenbank darf keine echte Karte durch nichts ersetzen.
        print(f"Firestore nicht erreichbar ({fehler}) — Datei bleibt unverändert.")
        return 0

    felder = daten.get("fields", {})
    titel = sv(felder.get("titel")) or sv(felder.get("monat"))
    gerichte = gerichte_lesen(felder)

    if not titel or not gerichte:
        print("Karte ist leer oder unvollständig — Datei bleibt unverändert.")
        return 0

    neu = ersetzen(quelle, "titel", esc(titel))
    neu = ersetzen(neu, "gerichte", "\n" + gerichte_html(gerichte) + "\n")
    lauf = ticker_html(gerichte)
    if lauf:
        neu = ersetzen(neu, "ticker", lauf)

    if neu == quelle:
        print("Keine Änderung — statischer Stand ist aktuell.")
        return 0

    if nur_pruefen:
        print("Änderung nötig.")
        return 1

    open(SEITE, "w", encoding="utf-8").write(neu)
    print(f"index.html aktualisiert: „{titel}“ mit {len(gerichte)} Gericht(en).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
