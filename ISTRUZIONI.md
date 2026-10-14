# ETNASOLUTIONclean – Istruzioni per i post settimanali automatici

Impresa di pulizie professionali a Catania e nei comuni etnei. Profili: Instagram @etnasolutionclean, pagina Facebook e Google Business Profile, tutti collegati a Metricool (brand/blogId **7404415**, fuso Europe/Rome).

## Cosa fare ogni settimana
1. Leggi `storico.md` per non ripetere temi, ganci e frasi d'apertura già usati.
2. Prepara **3 post** per **mercoledì, venerdì e lunedì** (il lunedì dopo il venerdì), sempre alle **12:30**.
3. **Formato: CAROSELLO** per Instagram e Facebook. Crea la spec JSON e lancia
   `python3 scripts/genera_carosello.py spec.json img/<anno>-w<settimana>`
   (il formato della spec è descritto in testa allo script). Struttura del carosello: copertina con il gancio, 3-5 schede (una per punto dell'elenco del testo), scheda finale con i contatti, generata in automatico. Titoli delle schede brevi (2 righe, usa `<br>`); testo delle schede massimo ~200 caratteri. Varia le coppie di colori: #0b3d5c/#3fd0c9, #0f4c4a/#9be7c4, #1d2b4f/#ffb547, #3a1f4f/#f08fc0, #2b3a1f/#c6e86b, #4a1f1f/#ffa58a.
   **Controlla tutte le slide con Read** (meglio un foglio riassuntivo con PIL) prima di pubblicare: il testo non deve sovrapporsi né uscire dai bordi.
4. Fai commit e push delle immagini su `main`. URL pubblico: `https://raw.githubusercontent.com/Maics75/etnasolutionclean-social/main/<percorso>`.
5. Per ogni post crea **DUE** programmazioni con `createScheduledPost`, alla stessa data e ora:
   - **A) Facebook + Instagram**: providers facebook + instagram; media = tutte le slide in ordine; testo COMPLETO; facebookData {type: POST}, instagramData {type: POST}.
   - **B) Google Business**: provider gmb, gmbData {type: publication}; media = solo la copertina; testo BREVE (2-3 frasi di sintesi + chiusura standard, **senza hashtag**, sotto i 1500 caratteri).
   - In entrambe: autoPublish true, draft false.
6. Prima di creare, verifica con `getScheduledPosts` che in quelle date non ci siano già post nostri (per evitare doppioni).
7. Aggiorna `storico.md` (data, tema, gancio) e fai commit e push.

## Stile del testo completo (modello: i post di giugno 2026 del profilo)
**Lunghezza totale (con chiusura e hashtag) tra 1.600 e 2.150 caratteri.** Instagram non accetta più di 2.200 caratteri: verificalo sempre con Python.
1. **Gancio** in apertura con un'emoji: una domanda o una curiosità che incuriosisce ("Qual è il punto più contaminato di un ambulatorio? Non è il pavimento.").
2. **Spiegazione** in 2-3 frasi: il problema, perché conta.
3. **Elenco numerato** 1️⃣ 2️⃣ 3️⃣ 4️⃣ con titoletto e i due punti (stessi punti delle schede del carosello).
4. **💡 Il consiglio pratico**: un suggerimento concreto e utile per chi legge.
5. **Domanda finale** per stimolare i commenti, con 👇.
6. **Chiusura standard IDENTICA** (vedi sotto), poi gli hashtag.

Tono: professionale, concreto e divulgativo; dai del "tu" al lettore. **Non inventare dati, percentuali, studi o normative**: se citi una regola o un dato, deve essere generale e verificabile. Niente promesse esagerate.

Argomenti: ampi e utili, non solo pubblicità. Fai ruotare: uffici e aziende, negozi e attività commerciali, ambulatori e strutture sanitarie (priorità); hotel e B&B, palestre, piscine, casa, condomini (scale, aree comuni), pulizie in quota e a fune, fine cantiere, sanificazione, trattamento pavimenti (marmo, cotto, parquet), vetrate, disinfestazione e derattizzazione, stagionalità (cambio stagione, piogge, festività, estate e zanzare), curiosità ("l'oggetto più sporco in ufficio"), errori comuni ("5 errori nel pulire il marmo"), "dietro le quinte" del metodo di lavoro.

## Chiusura standard (non modificarla)
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

## Hashtag (solo per Facebook e Instagram)
Sempre: `#etnasolutionclean #impresadipuliziecatania #pulizieprofessionali #sanificazioni #professionalcleaning #housekeeping #pulizieufficio #puliziepostcantiere #puliziaacrobatica #disinfezione #trattamentopavimentazioni #derattizzazione #pestcontrol`, più 2 hashtag specifici del tema.
