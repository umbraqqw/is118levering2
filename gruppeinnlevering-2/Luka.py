# is-118 Gruppeoppgave 2 Del 2: Interaktic Storyline i Python Eksempel

spille_igjen = "ja"
while spille_igjen == "ja" or spille_igjen == "Ja" or spille_igjen == "JA":
        

    # her kjører hele spillet og poeng nullstilles automatisk til 0 hver runde

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

    while not (start_input == "start" or start_input == "Start" or start_input == "START"):
        print("UGYLDIG VALG")
        start_input = input("vennligst skriv ordet `start` for å begynne: ")

    poeng = 0

    # Beslutningspunkt 1: Konflikten mellom Silje og Elias 

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

    while not (valg1 == "A" or valg1 == "a" or valg1 == "B" or valg1 == "b"):
        print("UGYLDIG VALG!")
        valg1 = input("Velg alternativ A eller B: ") 
        


    if valg1 == "A" or valg1 == "a":
        poeng += 10
        print("Erling tar samtalen for å komme til bunnen av årsaken,")
        print("og med det så løser du uenigheten mellom Silje og Elias.")
        print("+10 Poeng")
    elif valg1 =="B" or valg1 == "b":
        print("Erling setter konflikten i det åpne på fellesmøtet")
        print("og ber Silje og Elias diskutere uenighetene sine åpent.")
        print("Møtet blir ubehagelig, stemningen blir pressende (0 poeng)")
    else:
        print("UGYLDIG VALG!")
        print("Vennligst velg enten A eller B")

    input("\nTrykk Enter for å få videre til Beslutning 2...")


    # Beslutningspunkt 2: Uenigheten om digital folkemøter

    print()
    print("[Beslutning 2]")
    print("Det er to uker igjen til prototypen skal vises frem, og en ny uenighet oppstår.")
    print("Hamdi krever at folkemøte styres strengt gjennom kommunens gamle system for full kontroll.")
    print("Halgeir (innbyggerrepresentant) krever derimot en åpen løsning hvor innbygerne")
    print("kan delta uten teknisk sperring.")
    print()
    print("Hva gjør du?")
    print("     [A] skjær gjennom og bestem at kommunens gamle system skal brukes.")
    print("     [B] Samle partene til et møte for å finne et kompromiss.")
    print(f"Poengsum: {poeng}")
    valg2 = input("Velg alternativ A eller B: ")

    while not (valg2 == "A" or valg2 == "a" or valg2 == "B" or valg2 == "b"):
        print("UGYLDIG VALG!")
        valg2 = input("Velg alternativ A eller B: ")
    
    if valg2 == "A" or valg2 == "a":
        print("Erling bruker sjefsrollen sin og tvinger gjennom det gamle systemet.")
        print("Hallgeir føler seg overkjørt og mister motivasjonen for hele prosjektet")
        print("0 Poeng")
    elif valg2 =="B" or valg2 == "b":
        poeng += 10
        print("Erling samler partene for å finne en felles løsning.")
        print("Dette gjør at innbyggerne blir hørt, og at Hallgeir og Hamdi blir enig om et kompromiss.")
        print("(+10 poeng)")
    else:
        print("UGYLDIG VALG!")
        print("Vennligst velg enten A eller B")

    input("\nTrykk Enter for å få videre til Beslutning 3...")

    # Beslutningspunkt 3: Prioriterin i innspurten

    print()
    print("[Beslutning 3]")
    print("Det er bare en uke igjen før prototypen skal demostreres for kommunestyret.")
    print("Teamer er slitne, og arbedsbelastningen har vært uvanlig høy den siste tiden.")
    print()
    print("Hva gjør du?")
    print("     [A] Ta en pust i bakken og prioriter teambyggingen og relasjonene mellom partene (felles lunsj).")
    print("     [B] Kjøre hard teknisk sprint med pålagt overtid for å sikre at prosjektet blir ferdig.")
    print(f"Poengsum: {poeng}")
    valg3 = input("Velg alternativ A eller B: ")

    while not (valg3 == "A" or valg3 == "a" or valg3 == "B" or valg3 == "b"):
        print("UGYLDIG VALG!")
        valg3 = input("Velg alternativ A eller B: ")

    if valg3 == "A" or valg3 == "a":
        poeng += 10
        print("Erling prioriterer teambygging og en felles pause.")
        print("Stresset roer seg, og teamet får ny energi og bedre samhold!")
        print("+10 Poeng")
    elif valg3 =="B" or valg3 == "b":
        print("Erling krever hard teknisk sprint og overtid.")
        print("Teamet blir utslitt, feill oppstår og samarbeidsklimaet blir verre")
        print("(0 poeng)")
    else:
        print("UGYLDIG VALG!")
        print("Vennligst velg enten A eller B")

    input("\nTrykk Enter for å få sluttresultatet...")

    # sluttresultat

    print()
    print("                 SLUTRESULTAT FOR PROSJEKTLEDER ERLING")
    print()
    print(f"Totall puengsum: {poeng} av 30 mulig poeng.")

    if poeng == 30:
        print()
        print("[UTFALL 1]: SUKSESS (30 POENG)")
        print("Gratulerer! du tok alle de relasjonsbyggende valgene.")
        print("gjennom å etablere psykologisk trygghet og legge til rett for læring,")
        print("så har du ledd teamt ut av storming-fasen og over i norming-fasen.")
        print("prototypen levers med høy kvalitey og full forankring hos innbyggerne!")
    elif poeng >= 10:
        print()
        print(f"[UTFALL 2]: DELVIS LØST KONFLIKT ({poeng} POENG)")
        print("prototypen ble ferdigstilt til fristen, men relasjonene i teamet er sårbare.")
        print("Noen av konliktene ble løst, men teamet sliter fortsatt med spenning under overflaten.")
        print("Du har levert det tekniske, men må fortsette å jobbe med tilliten i teamet")
    else:
        print()
        print("[UTFALL 3]: SORMING-FELLE OG KRISE (0 POENG)")
        print("Prosjektet har stivnet helt fast i storming-fasen.")
        print("Gjentatte overkjøringer og mangel på psykologisk trygghet har skapt mistillit.")
        print("Teamet er fragmentert, fremdriften stopper opp, og prosjektet er i krise.")
    print()
    spille_igjen = input("Vil du spille på nytt (ja)?: ")

    while not (spille_igjen == "ja" or spille_igjen == "Ja" or spille_igjen == "JA"):
        print("UGYLDIG SVAR")
        spille_igjen = input("Vil du spille på nytt (ja)?: ")