import time

##Dette er kun for å tømme terminalen og få det til å se ryddig ut, lærte om det gjennom Gemini flash. Trenger absolutt ikke å ha dette nødvendigvis, og koden funker helt fint uten.
import os
import subprocess

subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True) #se over



#Oppsett av oppgave
print("Erling har fått i oppdrag om å lede et sammensatt fagteam og utvikle kommunens nye digital medborgerportal.\nSom gruppeleder med mye ansvar må man tenke seg godt om når man tar ulike valg for å sikre at gruppen kommer over i norming-fasen. \nDin jobb er å ta disse beslutningene for Erling, og sikre best mulig utfall for gruppen hans")
time.sleep(1.5) #Liker å bruke time.sleep for at alt ikke printer ut samtidig, gjør det litt mer lesbart føler jeg. 



def startSimulasjon(): #Funksjon for å lett kunne kjøre spillet på nytt
    while True: #Konstant sjekker om brukeren har skrevet riktig input; vil ikke la bruker fortsette simulasjonen før start = Y/n. Gjelder også nedover.
        start = input("Er du klar for å begynne? Y/n: ")
        if start == "Y" or start == "y":
            print("Starter simulasjon ...")
            time.sleep(1.5)
            break
        elif start == "N" or start == "n":
            print("fair enough...")
            return
        else:
            print("Ugyldig svar! Skriv Y for ja, n for nei!")

    #Oppstart og poengvariabel
    print("Velkommen til medborgerportalen!")
    poeng = 0

    #Scenario 1
    print("-- Scenario 1: Silje og Elias' konflikt --")
    print("Silje er UX-designer og krever fokus på universell utforming og enkel brukeropplevelse \nElias jobber med datasikkerhet og krever mer fokus på streng sikkerhet og innlogging før noe annet.")
    print("Begge står fast på sine egne synspunkt, og fagligheten i samtalen har sporet av og uenigheten blir nå opplevd som en personkonflikt i teamet")
    time.sleep(1)

    print("\nHvordan ønsker du å håndtere konflikten?")
    print("A: Kalle inn til individuelle samtaler med hver av de")
    print("B: Ta opp konflikten i plenum")

    while True:
        svar1 = input("\nVelg A eller B: ")

        if svar1 == "A" or svar1 =="a":
            print("Du tar en-til-en samtaler med begge parter. I egne rom føler begge seg trygge nok til å forklare sine faglige bekymringer uten å måtte forsvare seg foran resten av teamet. \nDere finner et kompromiss, og tilliten i teamet styrkes. ")
            poeng = poeng + 10 #Oppdatere poengvariabelen avhengig av svar
            break
        elif svar1 == "B" or svar1 =="b":
            print("Du tar uenigheten opp i plenum for hele gruppen. Siden konflikten allerede er betent, fører det offentlige presset til at Silje og Elias går rett i forsvarsposisjon. \nMøtet eskalerer, stemningen blir dårlig og ingen avklaring blir nådd.")
            poeng = poeng + 0
            break
        else:
            print("Ugyldig valg! Skriv enten 'A' eller 'B'.")
    time.sleep(2)



    #Scenario 2
    print("\n\n -- Scenario 2: Hamdi og Hallgeirs konflikt --")
    print("Det skal arrangeres et digitalt folkemøte for å demonstrere den nye medborgerportalen for innbyggerne")
    print("Hamdi ønsker en åpen og interaktiv plattform der innbyggerne kan stille spørsmål og gi direkte innspill. \nHallgeir frykter kaos, omgåelse av offentlige saksbehandlingsregler og digital tidsspille, og krever at de bruker kommunens eksisterende og trygge e-skjemaløsning")
    time.sleep(1)

    print("\nHvordan ønsker du å håndtere konflikten?")
    print("A: Skjære gjennom og overstyre med kommunens gamle e-skjemaløsning for å være på den sikre siden")
    print("B: Samle Hamdi og Hallgeir til en felles workshop for å designe et kompromiss som ivaretar både sikkerhet og samhandling")

    while True:
        svar2 = input("\nVelg enten A eller B: ")

        if svar2 == "A" or svar2 == "a":
            print("Du overstyrer Hamdi og velger den trygge, gamle løsningen. \nHallgeir er fornøyd, men Hamdi mister motivasjonen helt.\nFolkemøtet oppfattes som stivt og gammeldags av innbyggerne, og teamet mistet muligheten til å innovere")
            poeng = poeng + 0
            break
        elif svar2 == "B" or svar2 == "b":
            print("Du samler partene til en strukturert workshop. \nSammen klarer dere å kombinere ønsket om interaktivitet med kravet til sikkerhet.\nLøsningen blir et moderert digitalt maktrom som både er nyskapende og trygt. \nTilliten og samarbeidet i teamet vinner stort!")
            poeng = poeng + 10
            break
        else: 
            print("Ugyldig svar! Velg enten A eller B!")
    time.sleep(2)



    #Scenario 3
    print("\n\n -- Scenario 3: Innspurten og prioritering --")
    print("Det gjenstår kun to uker til den endelige leveransen av medborger portalen. Arbeidspresset er enormt, og man merker sjapt at teamet er slitne. \nSilje og Hamdi ønsker å ta en pust i bakken for å ta vare på samholdet og sikre at alle er på samme side før oppløpet. \nElias og Hallgeir argumenterer heller for å kjøre på med en beinhard sprint og pålagt overtid for å få ferdigstilt flest mulig funksjoner.")
    time.sleep(1)

    print("\nHvordan ønsker du å håndtere konflikten?")
    print("A: Prioritere teamet, ta en pust i bakken og fokusere på relasjoner og psykologisk trygghet")
    print("B: Kjøre hardt og satse på pålagt overtid for å levere alt av funksjonalitet")

    while True:
        svar3 = input("\nVelg enten A eller B: ")

        if svar3 == "A" or svar3 == "a":
            print("Du velger å ta vare på teamet. Ved å ro ned presset og samle laget, finner dere overskudd til å samarbeide effektivt de siste dagene. \nPrototypen blir ferdig levert med høy kvalitet og et godt team")
            poeng = poeng + 10
            break
        elif svar3 == "B" or svar3 == "b":
            print("Du presser teamet gjennom lange dager med pålagt overtid. Utmattelsen fører til misforståelser, koding under press skaper nye feil og samholdet i teamet bryter sammen før fristen.")
            poeng = poeng + 0
            break
        else: 
            print("Ugyldig svar! Velg enten A eller B!")
    time.sleep(2)


    print("Da er simulasjonen fullført! Kalkulerer utfall ...")
    time.sleep(2)

    if poeng == 30:
        print("\n\n--- UTFALL 1: NORMING-FASEN OPPNÅDD, FULL POTT! (30 POENG) ---")
        print("Erling har håndtert alle konfliktene på best måte!")
        print("Gjennom god kommunikasjon og tilrettelegging har teamet oppnådd psykologisk trygghet, og stiger mot norming-fasen")
        print("Medborgerportalen leveres innen fristen og er et fantastisk produkt. ")
        time.sleep(1)
        print("Bra jobba :)")
    elif 10 <= poeng <= 20:
        print("\n\n--- UTFALL 2: MIDDELS MÅLOPPNÅELSE --- ")
        print("Erling har løst enkelte av utfordringene, men teamet sliter fortsatt med gnisninger.")
        print("Relasjonene i gruppen er sårbare, og enkelte teammedlemmer føler seg forbigått.")
        print("Portalen blir levert, men prosjektet har noen hull og arbeidsmiljøet bærer med seg spenstig stemning.")
        time.sleep(1)
        print("Du kan gjøre det bedre!")
    else:
        print("\n\n--- UTFALL 3: MISLYKKET PROSJEKT OG FULLSTENDIG SAMMENBRUDD ---")
        print("Erling har håndtert konfliktene ved å være overstyrende og autoriterende")
        print("Teamet har absolutt null tillit, og motivasjonen har aldri vært lavere")
        print("Det kortsiktige tidspresset førte til utmattelse og misforståelser.")
        print("Prosjektet sporer av, portalen forsinkes kraftig, og teamet fungerer ikke lenger sammen.")
        time.sleep(1)
        while True:
            restart = input("Vil du prøve igjen? Y/n: ")
            if restart == "Y" or restart == "y":
                print("Tilbakestiller simulasjonen ...")
                time.sleep(2)
                subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True) #se over
                startSimulasjon()
                return
            elif restart == "N" or restart == "n":
                print("Takk for at du spilte :)")
                return
            else:
                print("Ugyldig svar!")

startSimulasjon()
