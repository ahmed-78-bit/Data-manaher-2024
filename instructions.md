# Instructions for Taking Screenshots and Scheduling the Script

## Steg 2: Ta en skärmbild av databasfilen
1. Öppna mappen där din `database.db`-fil finns.
2. Tryck på `Print Screen`-tangenten på ditt tangentbord för att ta en skärmbild.
3. Öppna ett bildredigeringsprogram som Paint.
4. Klistra in skärmbilden (Ctrl + V).
5. Spara bilden som `database_screenshot.png`.

## Steg 3: Schemalägg skriptet och ta en skärmbild
1. **Öppna Schemaläggaren**:
   - Tryck på `Win + R` för att öppna dialogrutan Kör.
   - Skriv `taskschd.msc` och tryck på Enter. Detta öppnar Schemaläggaren.

2. **Skapa en ny uppgift**:
   - I Schemaläggaren, klicka på `Skapa uppgift` i åtgärdsfönstret till höger.

3. **Ställ in utlösaren**:
   - I det nya uppgiftsfönstret, gå till fliken `Utlösare`.
   - Klicka på `Ny` för att skapa en ny utlösare.
   - Ställ in starttid och frekvens (dagligen, veckovis, etc.) för när du vill att skriptet ska köras.
   - Klicka på `OK` för att spara utlösaren.

4. **Ställ in åtgärden**:
   - Gå till fliken `Åtgärder`.
   - Klicka på `Ny` för att skapa en ny åtgärd.
   - I rullgardinsmenyn `Åtgärd`, välj `Starta ett program`.
   - I fältet `Program/script`, skriv `python` (eller sökvägen till din Python-exekverbara fil om den inte finns i din system-PATH).
   - I fältet `Lägg till argument`, skriv sökvägen till ditt skript, t.ex. `C:\path\to\data_script.py`.
   - Klicka på `OK` för att spara åtgärden.

5. **Spara uppgiften**:
   - Gå igenom de andra flikarna (Villkor, Inställningar) om du behöver ställa in ytterligare alternativ.
   - Klicka på `OK` för att spara uppgiften.

### Ta en skärmbild av Schemaläggaren
1. När uppgiften är skapad, ta en skärmbild av Schemaläggaren som visar din nya uppgift.
2. Tryck på `Print Screen`-tangenten på ditt tangentbord för att ta en skärmbild.
3. Öppna ett bildredigeringsprogram som Paint.
4. Klistra in skärmbilden (Ctrl + V).
5. Spara bilden som `task_scheduler_screenshot.png`.
