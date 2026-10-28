# is-118 Gruppeoppgave 2 Del 2: Interaktic Storyline i Python

print()
print("                 INTERAKTIV STORYLINE: ERLINGS LEDERUTFORDRINGER") 
print()
print("Du er Erling, prosjektelder for kommunens nye digitale medborgerportal.")
print("Etter seks uker har teamet havnet i storming-fasen.")
print("Din lederbeslutinger er kritisk for at prosjektet skal komme i mål uten uforsette stopp.")
print()
print("Valgene du tar gir poeng, og totalsummen bestemmer slutreslutatet.") 
print("Så pass på at du velger riktig!")
print()



start_input = input("vennligst skriv ordet `start` for å begynne: ")
gokjente_start_svar = ["start", "Start", "START"]

# Beslutningspunkt 1: Konflikten mellom Silje og Elias 

poeng = 0

if start_input == "start" or start_input == "Start" or start_input == "START":
    print("[Beslutning 1]")
    print("Silje (UX-designer) og Elias (IT og datasikkerhet) er uenige.")
    print("Silje vil ha ne åpen og brukervennlig portal som innebyggerne enkelt forstår,")
    print("Elias vil i motsetning ha en streng BankID og høy datasikkerhet.")
    print("Handlingen utvikler seg til en personkonflikt.")
    print()

    print("Hva gjør du?")
    print("     [A] ta seperate, individuelle samtaler med Silje og Elias.")
    print("     [B] ta opp konflikten foran hele teamet i et felles plenumsmøte.")
    print(f"Poengsum: {poeng}")
    valg1 = input("Velg alternativ A eller B: ") 
    
    
   

    if valg1 == "A":
        poeng += 10
        print("Erling tar samtalen for å komme til bunnen av årsaken,")
        print("og med det så løser du uenigheten mellom Silje og Elias.")
        print("+10 Poeng")
    elif valg1 =="B":
        print("Erling setter konflikten i det åpne på fellesmøtet")
        print("og ber Silje og Elias diskutere uenighetene sine åpent.")
        print("Møtet blir ubehagelig, stemningen blir pressende (0 poeng)")
    else:
        print("UGYLDIG VALG!")
        print("Vennligst velg enten A eller B")
else:
    print("UGYLDIG VALG")
    print("skriv `start` for og begyne.")




