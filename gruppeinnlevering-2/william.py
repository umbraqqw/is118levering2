# Interaktiv historie: Erling og prosjektteamet (IS-118, gruppeinnlevering 2)

poeng = 0  # Lagrer poeng basert på Erlings valg


def spor_om_valg(sporsmal):
    """Spør til brukeren skriver A eller B, så ugyldig input ikke stopper historien."""
    while True:
        svar = input(sporsmal + " (A/B): ").strip().upper()
        if svar in ("A", "B"):
            return svar
        print("Ugyldig valg, skriv A eller B.")


# --- Introduksjon ---
print("Det har gått seks uker siden Erling samlet prosjektteamet som skal utvikle kommunens nye medborgerportal.")
print("Portalen skal gjøre det enklere for innbyggerne å delta i lokaldemokratiet, og prototypen skal være klar om tre uker.")
print("Men stemningen i teamet er anspent. Silje og Elias er uenige om teknologi og design,")
print("og Hamdi og Hallgeir krangler om hvilket system som skal brukes til folkemøtet.")
print("Som prosjektleder må Erling ta flere valg som avgjør hvordan det går med teamet.")
input("\nTrykk Enter for å fortsette...")

# --- Beslutningspunkt 1: Silje og Elias ---
print("\nSilje og Elias krangler om teknologi og design, og diskusjonene tar stadig mer tid på møtene.")
print("A: Ta separate samtaler med hver av dem")
print("B: Ta opp konflikten mellom Silje og Elias i plenum")
valg1 = spor_om_valg("Hva gjør Erling?")
if valg1 == "A":
    poeng += 10
    print("Temperaturen senkes, og begge føler seg hørt. Silje og Elias blir enige om å samarbeide om en løsning som tar hensyn til både teknologi og design.")
else:
    print("Møtet blir intenst, og Silje og Elias går i forsvarsposisjon. Resten av teamet blir ukomfortable, og konflikten blir mer synlig enn før.")
input("\nTrykk Enter for å fortsette...")

# --- Beslutningspunkt 2: Hamdi og Hallgeir ---
print("\nHamdi og Hallgeir er uenige om hvilket system som skal brukes til folkemøtet.")
print("Skal de bruke det gamle systemet som ikke er like godt, men som innbyggere kjenner,")
print("Eller det nye systemet som er mer brukervennlig, men som ikke er ferdig?")
print("A: Skjære gjennom og bestemme at kommunens gamle system skal brukes")
print("B: Samle partene til et felles arbeidsmøte for å finne et kompromiss")
valg2 = spor_om_valg("Hva gjør Erling?")
if valg2 == "B":
    poeng += 10
    print("Begge parter føler seg hørt, og de finner sammen en hybridløsning som fungerer for både kommunen og innbyggerne.")
else:
    print("Hallgeir føler seg overkjørt og mister troen på prosjektet. Innbyggerne risikerer å få en løsning som oppleves som vanskelig og lite tilgjengelig.")
input("\nTrykk Enter for å fortsette...")

# --- Beslutningspunkt 3: Motivasjon ---
print("\nFristen nærmer seg, og Erling står overfor et valg: Skal han prioritere å motivere teamet eller å fokusere på fremdrift?")
print("A: Prioritere å motivere teamet på bekostning av arbeidstiden")
print("B: Prioritere fremdrift og leveranser, uavhengig av teamets nåværende motivasjon")
valg3 = spor_om_valg("Hva gjør Erling?")
if valg3 == "A":
    poeng += 10
    print("Teamet føler seg sett og verdsatt, og motivasjonen øker. Samarbeidet blir bedre, og arbeidet går raskere enn ventet.")
else:
    print("Teamet føler seg presset og demotivert, og samarbeidet svekkes. Flere begynner å jobbe hver for seg, og kvaliteten på arbeidet går ned.")
input("\nTrykk Enter for å se utfallet...")

# --- Avslutning: utfall basert på poeng ---
print(f"\nDine valg: {valg1}, {valg2}, {valg3}  |  Poeng: {poeng} av 30")
if poeng == 30:
    print("Utfall 1: Teamet gjenoppretter tillit og når norming-fasen! Prototypen leveres i tide.")
elif poeng >= 10:
    print("Utfall 2: Konflikten løses delvis, men relasjonene er sårbare. Prototypen leveres, men den uløste konflikten kan blusse opp igjen.")
else:
    print("Utfall 3: Prosjektet mister samhold og forsinkes. Teamet blir stående fast i storming-fasen, og prototypen blir ikke klar til bystyret.")