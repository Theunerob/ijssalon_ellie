from algemene_functies import mijn_functie_2

def aanbiedig_1(smaak, prijs, korting):
    voordeel = prijs * korting
    kortingsprijs = prijs - voordeel
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {kortingsprijs} euro."
    return uitvoer

print(aanbiedig_1("aardbei", 4, 0.1))

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    bedrag = totaal * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag:.2f} euro btw betaald dient te worden."

verkoop = [30, 40, 50, 49, 780, 34]
print(inkomsten_totaal(verkoop, 0.09))

def laag_en_hoog(mijn_lijst):
    uitvoer = [max(mijn_lijst), min(mijn_lijst)]
    return uitvoer

print(laag_en_hoog(verkoop))

def gemiddelde(mijn_lijst):
    bedrag = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {bedrag:.2f} euro."

print(gemiddelde(verkoop))

def meervoudig(invoer_lijst):
    uitvoer = laag_en_hoog(invoer_lijst)
    return uitvoer

print(meervoudig(verkoop))

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer

