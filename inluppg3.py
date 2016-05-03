'''
märkte i förra uppgiften att mitt test av numror inte fungerade då jag före testet försökte omvandla inputet till siffror,
men nu skall det fungera!
'''
def uppgift1(wows):
    if check_number(wows):
        wow(float(wows))
    else:
        print "Not a number!"

def check_number(i):
    try:
        float(i)
        return True
    except ValueError:
        return False
        

def wow(wows):
    if wows > 0:
        if wows == 1:
            print "Wow!"
            return
        else:
            print "Wow!"
            wow(wows - 1)
    else:
        print "Don't be a spoilsport!"

def uppgift2(s):
    s = input("Hur många SOS vill du skicka? ")
    if check_number(s):
        print sos(s)
    else:
        print "Not a number!"

def sos(s):
    if s == 1:
        return "SOS!"
    elif s == 0:
        return "Don't be a spoilsport!"
    else:
        return "SOS!" + sos(s - 1)

def uppgift3(n):
    if check_number(n):
        print summa(float(n))
    else:
        print "Not a number!"

#jag fattade inte riktigt vad man skulle göra här men försökte mitt bästa.
def summa(n):
    if n == 1:
        return n
    else:
        return 1/n + summa(n - 1)

def uppgift4(r):
    if check_number(r):
        print antalet_burkar(int(r))
    else:
        print "Not a number!"

def antalet_burkar(r):
    if r == 1:
        return r
    else:
        return r * r + antalet_burkar(r - 1)
    
        


uppgift1(23)
uppgift2(20)
uppgift3(100)
uppgift4(100)

