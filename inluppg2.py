#uppgift 1 nedan!
def uppgift1():
    inp = raw_input("Vad var ditt tentvitsord?: ")
    if check_number(inp):
        kursvits(int(float(inp)))
    else:
        uppgift1()

def check_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False 

def kursvits(i):
    if (i >= 0 and i < 15):
        print "Ditt kursvitsord är: 0"
    elif (i > 14 and i < 18):
        print "Ditt kursvitsord är: 1"
    elif (i > 17 and i < 21):
        print "Ditt kursvitsord är: 2"
    elif (i > 20 and i < 24):
        print "Ditt kursvitsord är: 3"
    elif (i > 23 and i < 27):
        print "Ditt kursvitsord är: 4"
    elif (i > 26 and i < 31):
        print "Ditt kursvitsord är: 5"
    else:
        return -1

#Uppgift 2 nedan!
def uppgift2():
    y = raw_input("Kolla om året är ett skottår: ")
    if check_number(y):
        y = int(y)
        if y >= 1600:
            kolla(y)
        else:
            print "Årtalet måste vara större en eller lika med 1600"
            uppgift2()
    else:
        uppgift2()

def kolla(y):
    y = int(y)
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                print "Året {} är ett skottår!".format(y)
            else:
                print "Året {} är inte ett skottår!".format(y)
        else:
            print "Året {} är ett skottår!".format(y)
    else:
        print "Året {} är inte ett skottår!".format(y)

#Uppgift 3 nedan!
def uppgift3():
    try:
        typ = float(raw_input("Vilken typ av produkt är det frågan om? 1 = DVD eller 2 = bok?: "))
        if typ > 0 and typ < 3:
            slut = float(raw_input("Vad är beställningens slutvärde? (inkl. postkostnader)?: "))
        else:
            print "Fel, du skall lägga in ett nummer mellan 1 och 2!"
            uppgift3()
    except TypeError:
        print "Fel, Du skall lägga in ett nummer (OBS: Punkter istället för kommatecken)!"
        uppift3()
    count(typ, slut)

def count(typ, slut):

    if typ == 1:
        t = 0.035
        m = 0.24
        tk = slut * t
        mk = (slut + tk) * m
        if tk > 10:
            print "Tull: {} (Uppbärs)".format(round(tk, 2))
        else:
            print "Tull: {} (Uppbärs inte)".format(round(tk, 2))
            tk = 0.00
        if mk > 10:
            print "Moms: {} (Uppbärs)".format(round(mk, 2))
        else:
            print "Moms: {} (Uppbärs inte)".format(round(mk, 2))
            mk = 0.00
        tot = tk + mk
        print "-----------------\nTotalt uppbärs: {}".format(round(tot, 2))
            
        
    else:
        m = 0.10
        tk = 0.00
        mk = slut * m
        print "Tull: {} (Uppbärs inte)".format(round(tk, 2))
        if mk > 10:
            print "Moms: {} (Uppbärs)".format(round(mk, 2))
        else:
            print "Moms: {} (Uppbärs inte)".format(round(mk, 2))
            mk = 0.00
        tot = tk + mk
        print "-----------------\nTotalt uppbärs: {}".format(round(tot, 2)) 
    

uppgift1()
uppgift2()
uppgift3()
