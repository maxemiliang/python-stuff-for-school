#!/usr/bin/python
#coding=utf-8
import string

vowels = 'aeiouyåäö'

def translate(s):
    ''' Translates the string s to "rövarspråket".'''
    result = ''
    for char in s:
        if char not in string.letters:
            result += char
        elif char not in vowels:
            result += (char+'o'+char)
        else:
            result += char

    return result

def continue_trans(f):
    for rows in f.readlines():
        print translate(rows),
    f.close()


def check_file(f):
    try:
        of = open(f, "r")
        of.close()
        return True
    except IOError:
        return False


def convertor(f):
    newFile = open("noNewLines.txt", "w")
    full = ""
    for lines in f.readlines():
        nolines = lines.replace("\n", " ")
        full += nolines
    newFile.write(full)
    print "Sucessfully Wrote: %s to file noNewLines.txt" % full
    newFile.close()
    f.close()





def uppgift1b():
    print "Rövarspråketcreator v1.0"
    print "------------------------"
    uFile = raw_input("What file do you want translated:")
    if check_file(uFile):
        file = open(uFile, "r")
        continue_trans(file)
    else:
        print "File not found!"
        uppgift1b()

def uppgift2():
    print
    print "NewLineDeletor v1.0"
    print "-------------------"
    nFile = raw_input("What file do you want to be newline-removed:")
    if check_file(nFile):
        file = open(nFile, "r")
        convertor(file)
    else:
        print "File not found!"
        uppgift2()


def uppgift3():
    crypto()

#------------------------------------- KODEN FÖR KRYPTERING NEDAN ------------------------------------
def check_number(i):
    try:
        int(i)
        return True
    except ValueError:
        return False

def menu():
    print "---------------------"
    print "--DenCrypted v13.37--"
    print "---------------------"
    print "Choose an option:"
    print "1) Encrypt message \n2) Decrypt message \n3) Encrypt from file \n4) Decrypt from file \n5) Quit"

def choice():
    v = string.lower(raw_input(">"))
    if v == "1":
        return 1
    elif v == "2":
        return 2
    elif v == "3":
        return 3
    elif v == "4":
        return 4
    elif v == "5":
        exit()
    else:
        print "That's not a valid choice!"
        choice()

def crypto():
    menu()
    val = choice()
    if val == 1:
        encryptText()
    elif val == 2:
        decryptText()
    elif val == 3:
        encryptFile()
    elif val == 4:
        decryptFile()

def encryptor(text, key):
    en_text = ""
    for char in text:
            if char in string.uppercase:
                old = ord(char)
                new = (old + int(key) - 65) % 26 + 65
                en_text += chr(new)
            elif char in string.lowercase:
                old = ord(char)
                new = (old + int(key) - 97) % 26 + 97
                en_text += chr(new)
            else:
                en_text += char
    if ask():
        loc = raw_input("Insert filename to save to:")
        save_to(loc, en_text)
    else:
        print "The Encrypted text is: %s and was encrypted from: %s, using key: %s" % (en_text, text, key)
    return

def decryptor(text, key):
    de_text = ""
    for char in text:
            if char in string.uppercase:
                old = ord(char)
                new = (old - int(key) - 65) % 26 + 65
                de_text += chr(new)
            elif char in string.lowercase:
                old = ord(char)
                new = (old - int(key) - 97) % 26 + 97
                de_text += chr(new)
            else:
                de_text += char
    if ask():
        loc = raw_input("Insert filename to save to:")
        save_to(loc, de_text)
    else:
        print "The decrypted text is: %s and was decrypted from: %s, using key: %s" % (de_text, text, key)
    return


def ask():
    q = raw_input("Wanna save result to a file (y or n): ")
    if string.lower(q) == "y":
        return True
    elif string.lower(q) == "n":
        return False
    else:
        ask()


def save_to(f, text):
    sFile = open(f, "w")
    sFile.write(text)
    print "Saved file: %s with text: %s" % (f, text)
    sFile.close()
    return


def encryptText():
    text = raw_input("What do you want to encrypt:")
    key = raw_input("Encryption key (integer):")
    if check_number(key):
        encryptor(text, key)
    else:
        encryptText()
def encryptFile():
    file = raw_input("What file do you want to encrypt:")
    key = raw_input("Encryption key (integer):")
    en_text = ""
    text = ""
    if check_number(key) and check_file(file):
        f = open(file, "r")
        for line in f.readlines():
            nline = line.replace("\n", " ")
            text += nline
        encryptor(text, key)
    else:
        encryptFile()
def decryptText():
    text = raw_input("What do you want to decrypt:")
    key = raw_input("Encryption key (integer):")
    if check_number(key):
        decryptor(text, key)
    else:
        decryptText()
def decryptFile():
    file = raw_input("What file do you want to decrypt:")
    key = raw_input("Encryption key (integer):")
    text = ""
    if check_number(key) and check_file(file):
        f = open(file, "r")
        for line in f.readlines():
            nline = line.replace("\n", " ")
            text += nline
        decryptor(text, key)
    else:
        decryptFile()

uppgift1b()
uppgift2()
uppgift3()