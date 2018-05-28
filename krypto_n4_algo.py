#!/usr/bin/env python3
# coding=utf-8

gAlphabet = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
gWB = [["Zeichenkette","Anzahl"]]

def GetPlaintext():
    _date = open("text5.txt", "r")
    _text = _date.read()
    _date.close()
    return _text

def StringCount(_string, _cleartext):
    _num = _cleartext.count(_string)
    return _num

def SetNum(_string, _count):            
    if _count > 5:
        gWB.append([_string, _count])      
    return

def CondProb(_text):
    _count = 0
    _string = raw_input("Bedingte Wahrscheinlichkeit welches Strings? ")
    for i in range(len(_text)-3):
        if (_text[i]+_text[i+1]+_text[i+2]+_text[i+3]) == _string:
            _count = _count + 1
    print(_count)
        

#*********START*********#

gText = GetPlaintext()

m = 0
n = 0
o = 0
p = 0
q = 0

for m in range(0, 26):
    letter1 = gAlphabet[m]

    for n in range(0, 26):
        letter2 = gAlphabet[n]

        for o in range(0, 26):
            letter3 = gAlphabet[o]

            for p in range(0, 26):
                letter4 = gAlphabet[p]

                for q in range(0, 26):
                    letter5 = gAlphabet[q]
                    letter12345 = letter1 + letter2 + letter3 + letter4 + letter5
                    gCounter = StringCount(letter12345, gText)
                    SetNum(letter12345, gCounter)
                    #print("Status: Suche " + letter12345)
                    if q < 26:
                        q = q + 1
                q = 0
                if p < 26:
                    p = p + 1
            p = 0
            if o < 26:
                o = o + 1
        o = 0
        if n < 26:
            n = n + 1
    n = 0  
    if m < 26:
        m = m + 1

for x in gWB:
    print(x[0],x[1])          

while True:
    CondProb(gText) 
