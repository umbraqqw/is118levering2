
 
# ---------------- INTRODUKSJON ----------------
print("=== ERLING OG STORMEN ===")
print("Seks uker har gått siden Erling samlet prosjektteamet.")
print("Portalen skal ha en prototype klar om tre uker, men stemningen er spent.")
print("Silje og Elias krangler om teknologi og design.")
print("Hamdi og Hallgeir er uenige om hvordan folkemøter skal foregå.")
input("\nTrykk Enter for å begynne...")

# ---------------- VALG 1: Silje og Elias ----------------
print("\n--- VALG 1: Konflikten mellom Silje og Elias ---")
print("Diskusjonene har blitt personlige og tar tid fra møtene.")
print("1) Ta en samtale med hver av dem hver for seg")
print("2) Ta opp konflikten i plenum")

if hent_valg() == "1":
    valg1 = "samtaler"
    stemning = "rolig"
    print("Erling lytter til begge. Temperaturen synker, og Silje og Elias")
    print("er villige til å finne en løsning sammen.")
else:
    valg1 = "plenum"
    stemning = "spent"
    print("Alle får høre striden. Silje og Elias går i forsvar,")
    print("og resten av teamet blir ukomfortable.")

# ---------------- VALG 2: Hamdi og Hallgeir ----------------
print("\n--- VALG 2: Uenigheten mellom Hamdi og Hallgeir ---")
print("Hamdi vil bruke kommunens plattform. Hallgeir vil ha et åpent system.")
print("1) Kalle inn til et felles møte nå")
print("2) Vente og håpe at de løser det selv")

if hent_valg() == "1":
    valg2 = "fellesmote"
    print("Hamdi og Hallgeir blir enige om en kompromissløsning:")
    print("kontrollert plattform, men med et åpent innspillsfelt.")
else:
    valg2 = "avvente"
    stemning = "spent"  # å vente gjør stemningen verre uansett
    print("Uenigheten blir liggende. Hallgeir slutter å dukke opp på møtene,")
    print("og Hamdi tar avgjørelser uten ham.")

# ---------------- VALG 3: Motivasjonen i teamet ----------------
print("\n--- VALG 3: Motivasjonen i teamet ---")
if stemning == "rolig":
    print("Stemningen er bedre, men det er kun tre uker til prototypen.")
else:
    print("Stemningen er amper, og tre uker til prototypen føles kort.")
print("1) Sette av tid til sosiale aktiviteter og tillitsbygging")
print("2) Prioritere fremdrift og leveranser")

if hent_valg() == "1":
    valg3 = "sosialt"
    print("Teamet spiser lunsj sammen og snakker om noe annet enn jobb.")
else:
    valg3 = "fremdrift"
    print("Erling setter strenge frister. Arbeidet går fort, men det blir stille i gangene.")

# ---------------- UTFALL ----------------
print("\n=== SLUTTEN ===")

if valg2 == "fellesmote" and valg3 == "sosialt":
    # Utfall 1: alt går bra
    print("UTFALL 1: Teamet går inn i norming-fasen!")
    if valg1 == "samtaler":
        print("De individuelle samtalene la grunnlaget for tilliten som nå bærer teamet.")
    else:
        print("Plenumsmøtet var tøft, men åpenheten ble til slutt en styrke.")
    print("Prototypen leveres i tide, og alle står bak den.")

elif valg2 == "avvente" and (valg3 == "fremdrift" or valg1 == "plenum"):
    # Utfall 3: for mange dårlige valg
    print("UTFALL 3: Teamet mister samholdet, og prosjektet blir forsinket.")
    print("Konfliktene ble aldri løst, og prototypen leveres for sent.")

else:
    # Utfall 2: blanding av gode og dårlige valg
    print("UTFALL 2: Konfliktene løses delvis, men relasjonene er sårbare.")
    print("Prototypen blir ferdig, men Erling må jobbe videre med tilliten.")

# Oppsummering av valgene Erling tok (bruker variablene vi lagret)
print("\nDine valg: " + valg1 + " -> " + valg2 + " -> " + valg3)
git add .
git commit -m "Ferdig med min del av gruppeinnlevering 2"
git pull
git push
git add .
git commit -m "Ferdig med min del av gruppeinnlevering 2"
git pull
git push
   print("\nDine valg: " + valg1 + " -> " + valg2 + " -> " + valg3)
   
