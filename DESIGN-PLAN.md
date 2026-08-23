# Red Lotus Streetfood — Designplan (FREIGEGEBEN 2026-08-21)

Stand: 2026-08-21 · Richtung: Punk-Plakat (Impossible-Foods-Referenz) + Flyer-DNA · Format: Onepager

## Feste Inhalte (Quelle: Flyer + Felix, 21.08.2026)

- **Standort:** Biberacher Wochenmarkt, **Samstag 10–15 Uhr** (einziger regulärer Termin)
- **E-Mail:** info@redlotusstreetfood.com · **Telefon:** 0151 55460254
- **Instagram:** @red.lotusstreetfood (Seite existiert noch nicht — Link erst einbauen, wenn live)
- **Domain (geplant):** www.redlotusstreetfood.com — Hostinger-Freikontingent, Registrierung prüfen
- **Claim:** „Events & Foodtruck"

## Creative North Star: „Das Nachtmarkt-Plakat"

Seite 1 ist das Kerzenlicht-Buffet — leise, dunkel, edel. Seite 2 ist das Plakat am Bauzaun
daneben: dieselbe Dunkelheit, aber angeschrien. Riesige Condensed-Typo in Lotus-Rot,
Food-Fotos, die in organischen Blüten-Formen um die Schrift schweben, Preise groß und
ehrlich. Kein Schnickschnack, kein Schatten, keine Verläufe — Farbe, Schrift, Essen.

**Verwandtschaft zu Seite 1 (bewusst):** rot-getöntes Nachtschwarz statt neutralem Anthrazit,
dieselbe Cream-Textfarbe, dieselbe Body-Schrift (Bricolage Grotesque), das Lotus-Icon.
**Abgrenzung (bewusst):** kein Gold (bleibt Seite-1-exklusiv), keine Serifen, keine Stille.

## Tokens

### Farben (5 + Ampel)
| Name | Hex | Rolle |
|---|---|---|
| Lotus Night | `#1E0B0E` | Canvas — Schwarz mit Rotstich (Seite 1 hat Braunstich: #1c1a17) |
| Glut | `#3B1116` | Angehobene Flächen, Menü-Karten, Bänder |
| Lotus-Rot | `#E0473A` | Display-Typo, CTAs, aktive Zustände — identisch mit Seite-1-Token `red-bright` |
| Lotus Blush | `#F2C4BC` | Sekundärtext, Klammer-Zusätze, inaktive Pills — das „leise Rosa" zum lauten Rot |
| Cream | `#F5F0E6` | Fließtext — 1:1 aus Seite 1 übernommen (Familien-DNA) |
| Chili | `#FF2E63` | NUR Schärfegrad-Badges (🌶-Ersatz als SVG) — sparsamst |

Kontrast-Pflicht: Lotus-Rot auf Lotus Night für Display-Größen ok (Large Text), für
Fließtext immer Cream. CTA-Text Cream auf Lotus-Rot: prüfen, ggf. Night auf Rot.

### Typografie
| Rolle | Font | Einsatz |
|---|---|---|
| Display | **Anton** (Google, 400) | ALL CAPS, clamp(3.5rem, 12vw, 11rem), line-height 0.85, Hero + Sektionstitel + Preise |
| Body/UI | **Bricolage Grotesque** (wie Seite 1) | Fließtext 1rem/1.6, Labels 0.72rem ALL CAPS mit 0.28em Tracking |

Signatur-Stilmittel: der **Klammer-Zusatz** in Blush hinter dem roten Hauptwort —
„LOADED FRIES *(RICHTIG LOADED)*", „BOWLS *(AUCH VEGAN)*", „SAMSTAG *(BIS AUSVERKAUFT)*".
Übernimmt die Witz-Funktion, die Seite 1 nicht haben darf.

### Form & Raum
- Radius: 16px Pills für Buttons/Badges/Filter, sonst 0 — Karten sind flache Farbflächen
- Keine Schatten, keine Verläufe. Tiefe = Night → Glut → Rot
- Sektionsabstand 96–140px, max-width 1280px, Menü volle Breite

## Signature-Element: Angepinnte Polaroids (aus dem Flyer übernommen)

Food- und Truck-Fotos erscheinen als angepinnte Polaroids: Lotus-Rot gerahmt, leicht
gedreht (-4° bis +6°), mit Pin-Punkt oben — exakt die Behandlung, die der Flyer vormacht.
Sie kleben asymmetrisch neben/über der Display-Typo, das Foto ist die Fußnote zum
geschrienen Wort. Genau EIN Boldness-Ort; alles andere bleibt diszipliniert.

## Passport-Konzept (Felix, 21.08.2026 — finale Fassung: Monatskarte als Länder-Mix)

Jeden Monat eine kleine Karte mit 3–4 Gerichten quer durch Asien — z.B. September:
Bulgogi Loaded Fries (Seoul) + Fried Rice (Bangkok) + Veggie Gyoza (Tokyo).
NICHT eine Stadt pro Monat — der Mix ist das Konzept.

- **Stempel am Gericht, nicht am Kapitel:** jedes Gericht trägt seinen
  Herkunfts-Stempel (SEL/BKK/TYO/HAN/HKG) als kleine Line-Art-SVG neben dem Namen.
  Jede Monatskarte zeigt so 3–4 Stempel = mehr Reise pro Karte
- **Monatsrahmen:** Karte als „Boarding Pass SEPTEMBER" gerahmt; vergangene Monate
  als verblasste Stempel-Sammlung darunter („Wo wir schon waren")
- **Gerichte-Pool:** die Monatskarte wird aus einem festen Pool zusammengestellt —
  der Pool existiert bereits als Streetfood-/Getränke-Unterkatalog in Felix'
  Eventkalender-App (Kategorie bisher „Thyme & Lime", wird in Red Lotus Streetfood
  umbenannt — Entscheidung Felix 21.08.2026: Lime & Thyme endgültig ersetzt)
- **App-Verknüpfung (gewünscht):** Website liest die Monatskarte perspektivisch aus
  einer neuen, separaten Firestore-Collection „website" (App schreibt, Website liest).
  ⚠️ Sicherheitsregel aus dem Seite-1-Briefing gilt: öffentliche Seite bekommt
  AUSSCHLIESSLICH Lesezugriff auf diese eine Collection, nie auf interne Daten
  (Löhne, Bestellungen, Inventar). Bis die Anbindung steht: Monatskarte als
  editierbarer JSON-Datenblock im Repo
- **Dauerbrenner bestätigt (Felix, 21.08.2026):** die **Loaded Fries bleiben immer
  auf der Karte** — mit „Immer an Bord"-Badge statt Städte-Stempel. Monatskarte =
  Loaded Fries + 2–3 wechselnde Gerichte. Optionale Idee (unbestätigt): das
  Fries-Topping könnte mit dem Monat reisen (September: Bulgogi)
- **Design:** Einreisestempel als flache Line-Art-SVGs (Lotus-Rot/Blush, oval/rund,
  Stadtname + Koordinaten, leicht gedreht) als Sektionsmarker im Menü. KEIN
  skeuomorphes Passport-Büchlein, keine Lederoptik — Stempel + Polaroids sprechen
  dieselbe Reisetagebuch-Sprache auf dem Punk-Plakat
- **Authentizitäts-Puffer:** Unterzeile „Inspiriert von den Nachtmärkten Asiens" —
  Fusion (Bulgogi Fries) ist Konzept, nicht Anspruch auf Landesküche
- **Später (Offline-Anschluss):** physischer Stempelpass am Truck als
  Kundenbindungs-Idee — Web-Design und Karte würden sich 1:1 spiegeln

## Marken-Elemente aus dem Flyer (Entscheidung 21.08.2026)

- **Logo:** der Script-Schriftzug „Red Lotus Streetfood" bleibt als Wortmarke (Bilddatei) —
  die Seiten-Typo (Anton) ersetzt ihn NICHT, Logos dürfen anders sein
- **Maskottchen:** Winke-Katze als flaches Line-Art-Element (Chalk-Stil), sparsam:
  einmal im Hero-Umfeld oder Footer, nicht als wiederholtes Pattern.
  Hinweis: Seite-1-Briefing schloss die Katze nur für die Premium-Seite aus — für die
  verspielte Seite 2 ist sie bewusst freigegeben (Felix, 21.08.2026)
- **Lotus-Icon:** rot, als Favicon + Trennelement (wie Seite 1)
- **Kreide-Textur:** NICHT als Flächen-Look übernehmen (Template-Falle) — höchstens als
  dezente Grain-Note auf dem Night-Canvas

## Onepager-Struktur

```
┌─────────────────────────────────────┐
│ Sticky Nav: Logo · Menü · Standort ·│  schmal, Night, rote Pill "Wo? Wann?"
│ Galerie · [Wo? Wann?]               │
├─────────────────────────────────────┤
│ HERO                                │  RED LOTUS eyebrow (Blush, getrackt)
│  STREET                             │  Display Anton, Lotus-Rot, 2 Zeilen
│  FOOD (VOM TRUCK.)                  │  2–3 angepinnte Polaroids (rot gerahmt,
│  ↓ Pill-CTA: Speisekarte            │  gedreht): Nachtfoto Truck + Pad-Thai
├─────────────────────────────────────┤
│ TICKER-BAND (Glut): LOADED FRIES ·  │  laufende Zeile, pausiert bei
│ BOWLS · PAD THAI · SUMMER ROLLS ·   │  prefers-reduced-motion
├─────────────────────────────────────┤
│ MENÜ = BOARDING PASS SEPTEMBER      │  Unterzeile: „Inspiriert von den
│  (DIE SEPTEMBER-KARTE)              │  Nachtmärkten Asiens"
│   [IMMER AN BORD]                   │  Dauerbrenner zuerst, eigenes Badge
│         Loaded Fries . 10,50 €      │  statt Städte-Stempel
│   [BKK] Fried Rice ....  8,90 €     │  Stempel-SVG PRO GERICHT (Herkunft),
│   [TYO] Veggie Gyoza ..  7,50 €     │  Anton, Preis rechts, Chili-Badges,
│   [SEL] + 1 Motto-Gericht           │  Vegan-Kennzeichnung
│  [Verblasste Stempel-Reihe]         │  Archiv: „Wo wir schon waren" —
│  AUG · JUL · …                      │  vergangene Monatskarten, blass          │
├─────────────────────────────────────┤
│ WO? WANN?                           │  Riesige Typo: SAMSTAG (10–15 UHR)
│  BIBERACHER WOCHENMARKT             │  Maps-Link als Pill
├─────────────────────────────────────┤
│ GALERIE-BAND                        │  Polaroid-Collage, angepinnt, 4–6 Fotos
├─────────────────────────────────────┤
│ FAMILIE                             │  „Catering? Kochkurse? → Red Lotus     │
│                                     │  Asian Food" — Cross-Link Seite 1      │
├─────────────────────────────────────┤
│ FOOTER: WhatsApp · IG · Impressum · │  Night, Hairline in Glut
│ Datenschutz · Lotus-Icon            │
└─────────────────────────────────────┘
```

## Motion (dezent, orchestriert)

- Hero-Load: Display-Zeilen staggern von unten (0.4s, back.out), Masken-Fotos faden nach
- Scroll: Menü-Reihen staggern (GSAP-frei machbar, IntersectionObserver reicht)
- Ticker: CSS-Marquee, pausiert on hover + reduced-motion → statisch
- Sonst nichts. Kein Parallax.

## Qualitäts-Floor (nicht verhandelbar)

Responsive 375/768/1024/1440 · Kontrast 4.5:1 für Fließtext · sichtbarer Fokus ·
prefers-reduced-motion · scroll-margin-top auf Anker · echte `<button>`/`<a>` ·
Bilder mit width/height + lazy · SVG-Icons statt Emoji (Chili!) · smooth scroll.
Abnahme gegen web-design-guidelines-Skill vor Livegang; impeccable-Review nach Erstbau.

## Selbstkritik (frontend-design-Pass)

„Dunkler Canvas + ein greller Akzent" ist AI-Default-Cluster Nr. 2 — hier trotzdem richtig,
weil (a) vom Kunden explizit gewählt, (b) Rot die Marke IST, (c) die Differenzierung aus
Rotstich-Schwarz, angepinnten Polaroids, Winke-Katze und Klammer-Witz kommt, nicht aus
der Palette allein. Kreidetafel-Volloptik wurde erwogen und verworfen (Template-Falle).
Verworfen wurde: genereller Orange/Blau-Vorschlag aus dem Katalog (generisch), Gelb-Canvas
(kämpft gegen die Marke), Gold-Akzente (verwischt die Grenze zu Seite 1).

## Offene Inhalte (blockiert den Bau nicht, aber den Feinschliff)

1. Speisekarte konkret: Gerichte + Preise (aktuell „latent") — Loaded Fries vom Flyer-Foto
   als Aufhänger gesetzt
2. Logo als Datei: Script-Wortmarke + Katze in Web-Auflösung (transparentes PNG/SVG);
   bis dahin Nachbau-Platzhalter
3. Domain redlotusstreetfood.com im Hostinger-Freikontingent registrieren (Flyer nennt
   sie bereits — E-Mail-Adresse info@… setzt sie voraus)
4. Instagram @red.lotusstreetfood anlegen, Link erst danach scharf schalten
5. ⚠️ Foodtruck7.jpg trägt ein „KI-generierter Inhalt"-Wasserzeichen — nicht verwenden
   (Widerspruch zum Authentizitäts-Versprechen, siehe Briefing Seite 1). Foodtruck6 zeigt
   eine private Glas-Box statt Takeaway — auch eher nicht. Stark: Foodtruck3 (Nacht, Gäste),
   Foodtruck5 (Pad-Thai-Bowl top-down), Foodtruck1 (Truck frontal Tag).
