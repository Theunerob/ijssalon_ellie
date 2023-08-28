from helper import decoreer

def print_aanbieding():
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
decoreer("Aanbieding")

print_aanbieding()



print()
print()

def mijn_functie(str1, str2):
    uitvoer = ""
    for c in str1:
        if c in str2:
            uitvoer = uitvoer + c
    return uitvoer

print(mijn_functie("hallo", "hello"))
