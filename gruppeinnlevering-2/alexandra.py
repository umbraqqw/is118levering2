print("Velkommen til digital medborgerportal-simulator \n")

print("---Situasjon---")
print("Erling har fått i oppdrag om å ledet et sammensatt fagteam og utvikle kommunens nye digitale medborgerportal. \n Med dette følger mye ansvar for å sikre at gruppen kommer inn i norming-fasen. \n Din jobb er å ta disse beslutningene for Erling, og sikre best mulig utfall for gruppen hans. \n")

print("---Teamet består av---")
print("Erling (prosjektleder) \n Silje (UX-designer) \n Elias (IT- og datasikkerhet) \n Hamdi (fra kulturavdelingen) \n Hallgeir (innbyggerrepresentant)")
print("-" * 50 + "\n")

def retry(retry_choice):
    if retry_choice == "Y":
        valg("", "", "")
    elif retry_choice == "N":
        exit()
    else:
        print("Ugyldig input. Prøv på nytt!")
        retry(retry_choice)

def valg(valg1, valg2, valg3):
    print("Scenario 1: Konflikten mellom Silje og Elias (Sikkerhet vs. Brukervennlighet)")
    print("Silje (UX-Designer) og Elias (IT- og datasikkerhet) er i konflikt om balansen mellom brukervennlighet og datasikkerhet, og en faglig uenighet har utviklet seg til en personskonflikt. De avbryter hverandre, kritiserer hverandre og skaper splittelse i gruppen.")
    print("Hva skal Erling gjøre?")
    print("A. Separate samtaler med Silje og Elias? \n" + "B. Kalle inn til et felles plenumsmøte?")
    valg1 = input("Velg A / B: ").upper()
    match valg1:
        case "A":
            print("Riktig svar! (+10 poeng)")
            print("Temperaturen og det emosjonelle spenningsnivået senkes raskt. Både Silje og Elias opplever å bli hørt uten frykt for å tape ansikt foran gruppen.")
        case "B":
            print("Feil svar! (0 poeng)")
            print("Møtet blir veldig ubehagelig og intenst. Silje og Elias går rett i forsvarsposisjon, stemningen blir pressende, og mer tilbakeholdene medlemmer som Hamdi og Hallgeir trekker seg unna i stillhet.")
        case _:
            print("Ugyldig input. Prøv på nytt!")
            valg("", "", "")
    print("-" * 50 + "\n")
    print("Scenario 2: Uenighet om digitale folkemøter (Kommunal kontroll vs. Åpenhet)")
    print("Nå er det kun to uker igjen til prototypen skal presenteres, og det oppstår en konflikt mellom Hamdi (fra kulturavdelingen) og Hallgeir (innbyggerrepresentant) om hvorvidt digitale folkemøter skal styres gjennom kommunens eksisterende system eller en mer åpen og moderne løsning. \n Den økende frustrasjonen gjør at Erling må ta en avgjørelse for å sikre fremdrift i prosjektet.") 
    print("Hva skal Erling gjøre?")
    print("A. Skal Erling tvinge gjennom et gammelt system? \n" + "B. Skal Erling kalle inn til et felles arbeidsmøte")
    valg2 = input("Velg A / B: ").upper()
    match valg2:
        case "A":
            print("Feil svar! (0 poeng)")
            print("Hallgeir føler seg overkjørt og mister troen på prosjektet. \n Innbyggerne risikerer å få en løsning som oppleves som vanskelig og lite tilgjengelig.")
        case "B":
            print("Riktig svar! (+10 poeng)")
            print("Hallgeir og innbyggerne føler seg respektert og hørt. \n Løsningen ivaretar kommunens trygghetskrav samtidig som den støtter målet om å øke innbyggerengasjementet med 20 prosent.")
        case _:
            print("Ugyldig input. Prøv på nytt!")
            valg("", "", "")
    print("-" * 50 + "\n")
    print("Scenario 3: Prioritering i innspurten (Milepæl om 1 uke)")
    print("Det er bare én uke igjen før prototypen skal demonstreres for kommunestyret. Arbeidspresset er høyt, og teamet er slitne og stressede etter ukene med uenigheter. Erling må ta en siste avgjørelse om hvordan de siste dagene skal brukes.")
    print("Hva skal Erling gjøre?")
    print("A. Skal Erling velge teambygging og felles lunsj \n" + "B. Skal Erling kjøre en hard teknisk sprint / overtid?")
    valg3 = input("Velg A / B: ").upper()
    match valg3:
        case "A":
            print("Riktig svar! (+10 poeng)")
            print("Stresset demper seg, samholdet styrkes, og medlemmene ser hverandre som lagkamerater igjen. Dette gjør teamet klare til å gå inn i norming-fasen")
        case "B":
            print("Feil svar! (0 poeng)")
            print("Teammedlemmene blir utslitte og irriterte. Uenigheten blir bare feid under teppet og risikerer å blusse opp igjen rett etter milepælen.")
        case _:
            print("Ugyldig input. Prøv på nytt!")
            valg("", "", "")
    print("-" * 50 + "\n")
    utfall(valg1, valg2, valg3)


def utfall(valg1, valg2, valg3):
    if valg1 == "A" and valg2 == "B" and valg3 == "A":
        print("Beste mulige utfall (30/30 poeng).") 
        print("Erling leder teamet inn i norming-fasen, og prototypen leveres med god kvalitet. Teamet er nå klar for neste steg.")
        print("Bra jobbet!")
        exit()
    elif valg1 == "B" and valg2 == "A" and valg3 == "B":
        print("Verste mulige utfall (0/30 poeng).")
        print("Teamet blir fastlåst i storming-fasen, og prosjektet forsinkes betraktelig. Teamet mister sin lagånd, og det oppstår nye personskonflikter.")
        retry_choice = input("Vil du prøve på nytt? (Y/N): ").upper()
        retry(retry_choice)
    else:
        print("Middels utfall (10-20/30 poeng).")
        print("Prototypen leveres i tide, men relasjonene i teamet er fremdeles sårbare. Teamet får en tregere fremdrift fremover, og det preger gruppen med uro.")
        retry_choice = input("Vil du prøve på nytt? (Y/N): ").upper()
        retry(retry_choice)

valg("", "", "")
