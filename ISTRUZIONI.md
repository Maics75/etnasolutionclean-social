# ETNASOLUTIONclean – Istruzioni per i post settimanali automatici

Impresa di pulizie professionali a Catania e nei comuni etnei. Profili: Instagram @etnasolutionclean, pagina Facebook, Google Business Profile, tutti collegati a Metricool (brand/blogId **7404415**, fuso Europe/Rome).

## Cosa fare ogni settimana
1. Leggi `storico.md` per non ripetere temi, titoli e frasi d'apertura già usati.
2. Prepara **3 post** per la settimana successiva: **mercoledì, venerdì e lunedì** (il lunedì dopo il venerdì), sempre alle **12:30**.
3. Temi da far ruotare, sempre con un taglio diverso: uffici e aziende, negozi e attività commerciali, ambulatori e strutture sanitarie (priorità); poi, a turno, hotel e strutture ricettive, palestre, piscine, casa, pulizie in quota/acrobatiche, fine cantiere, sanificazioni, trattamento pavimenti, vetrate, derattizzazione/disinfestazione. Si possono usare anche consigli pratici, stagionalità (cambio stagione, festività, rientro dalle ferie) e curiosità sulla pulizia professionale.
4. Grafiche: crea una spec JSON e lancia `python3 scripts/genera_grafiche.py spec.json img/<anno>-w<settimana>`. Stile fisso (template.html): sfondo scuro con colore d'accento, marchio ETNASOLUTIONclean, icona emoji, kicker, titolo breve (max 2 righe), 4 punti con spunta, chiusura "Preventivo gratuito". Varia le coppie di colori (es. #0b3d5c/#3fd0c9, #0f4c4a/#9be7c4, #1d2b4f/#ffb547, #3a1f4f/#f08fc0, #2b3a1f/#c6e86b). **Controlla ogni immagine con Read** prima di pubblicarla: il testo non deve sovrapporsi né uscire dai bordi.
5. Fai commit e push delle immagini su `main`. URL pubblico: `https://raw.githubusercontent.com/Maics75/etnasolutionclean-social/main/<percorso>`.
6. Programma ogni post con Metricool `createScheduledPost`: providers facebook + instagram + gmb; facebookData {type: POST}, instagramData {type: POST}, gmbData {type: publication}; media = URL raw dell'immagine; autoPublish true, draft false. Il testo deve restare sotto i 1500 caratteri (limite di Google Business).
7. Prima di creare, verifica con `getScheduledPosts` che in quelle date non ci siano già post, per evitare doppioni.
8. Aggiorna `storico.md` (data, tema, titolo) e fai commit.

## Struttura del testo (obbligatoria)
- 1 frase d'apertura a effetto con un'emoji, poi 1-2 frasi sul servizio del giorno. Tono professionale e concreto, dare del "tu", niente esagerazioni o promesse non verificabili.
- Poi la **chiusura standard, IDENTICA** (non modificarla):

```
👉 📢 Richiedi un sopralluogo e un preventivo gratuito!

Servizi di pulizia professionale, sanificazione e manutenzione per ogni tipo di ambiente:
🏠 Casa
💻 Ufficio & Azienda
🏨 Hotel & Strutture Ricettive
🏬 Attività Commerciali
🏥 Strutture Sanitarie
🏋️‍♂️ Palestre
🏊‍♂️ Piscine
🧗‍♂️ Pulizie in quota

🌐 Scopri tutti i servizi: www.etnasolutionclean.it
📞 Per urgenze e preventivi: 346 2468238 / 377 1212161
```

- Hashtag finali (15): sempre `#etnasolutionclean #impresadipuliziecatania #pulizieprofessionali #sanificazioni #professionalcleaning #housekeeping #pulizieufficio #puliziepostcantiere #puliziaacrobatica #disinfezione #trattamentopavimentazioni #derattizzazione #pestcontrol` più 2 hashtag specifici del tema.
