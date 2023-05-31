# Variabelen

prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
}

aanbieding = 0.8 * prijzen["aardbei"]

reclame_tekst = (f"Vandaag in de aanbieding: Aardbei-ijs - slechts € {aanbieding}")

reclame_tekst2 = reclame_tekst[:54]

reclame_tekst3 = reclame_tekst2.upper()

reclame_tekst4 = reclame_tekst3.split(" ")

for el in reclame_tekst4:
    if 5 < len(el):
        print(el.lower())
    else:
        print(el)
