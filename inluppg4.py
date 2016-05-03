#!/usr/bin/python
#coding=utf-8
import random

def check(i):
    try:
        float(i)
        return True
    except ValueError:
        return False

def r(lvl):
    if lvl == "easy":
        return random.randint(1, 10)
    else:
        return random.randint(1,30)

def startQ(q, q2):
    questions = []
    answers = []
    correct = []
    right = 0
    for x in range(0, q):
        questions.append([r(q2), r(q2)])
        c = questions[x][0] * questions[x][1]
        correct.append(c)
        current = int(input("What is %d times %d?: " % (questions[x][0], questions[x][1])))
        if current == correct[x]:
            right += 1
            answers.append(current)
            print "Correct Answer!"
        else:
            answers.append(current)
            print "Sorry wrong answer, the right answer is %d" % correct[x]

    print "You answered on %d questions and got %d of them right!" % (q, right)
    print "Here are the questions and your answers: "
    for i in range(0, q):
        print "%d * %d = %d and you answered: %d" % (questions[i][0], questions[i][1], correct[i], answers[i])





def uppgift1():
    q = int(input("How many questions do you want?:"))
    q2 = raw_input("How hard should it be? (easy or hard):")
    if check(q) and (q2 == "easy" or q2 == "hard"):
        startQ(q, q2)
    else:
        uppgift1()

def uppgift2(signum):
    cont = signum[-4:-1]
    if int(cont) % 2 == 0:
        print "Signumet tillhör en kvinna!"
    else:
        print "Signumet tillhör en man!"


def uppgift3():
    p = int(input("Hur många poäng vill du spela till?: "))
    if p > 0:
        game(p, True)
    else:
        uppgift3()

def playscreen():
    print "Välj en:"
    print "1) Sten"
    print "2) Sax"
    print "3) Papper"
    return

def checkResults(d, p):
    if not p > 3 or p < 1:
        if (p == 1 and d == 2) or (p == 2 and d == 3) or (p == 3 and d == 1):
            return 1 # spelaren vinner
        elif (p == d):
            return 3 # oavgjort
        else:
            return 2 # datorn vinner
    else:
        return 4


def game(p, f):
    # 1 = Sten, 2 = Sax, 3 = Papper
    ongoing = True
    pP = 0
    dP = 0
    val = ["Sten", "Sax", "Papper"]
    while ongoing:
        dVal = random.randint(1, 3)
        playscreen()
        pVal = int(input(">"))
        if checkResults(dVal, pVal) == 1:
            pP += 1
            print "Du vann, Datorn valde %s och du valde %s" % (val[dVal-1], val[pVal-1])
        elif checkResults(dVal, pVal) == 2:
            dP += 1
            print "Datorn vann, Datorn valde %s och du valde %s" % (val[dVal-1], val[pVal-1])
        elif checkResults(dVal, pVal) == 3:
            print "Oavgjort!"
        else:
            print "Okänt nummer insatt.. använd enbart 1, 2 eller 3."
        if pP >= p or dP >= p:
            ongoing = False

    print "Spelet Slut!\n---------------------------"
    print "Dina poäng: %d" % pP
    print "Datorns poäng: %d" % dP
    return



uppgift1()
uppgift2("280499+0138")
uppgift3()