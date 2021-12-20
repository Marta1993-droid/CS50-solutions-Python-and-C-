#Card number validation

import sys

card = input("Card number:")
N = list(card)

b = []
for i in range(0,len(N),2): #ITERATING EVERY OTHER DIGIT
    h=int(N[i])*2
    if len(str(h))>1: #12 DEAL
        for i in str(h):
            #print (i)
            b.append(i)
    else:
        b.append(str(h)) #LIST OF CHARACTERS #1

c=0
for i in range(0,len(b),1): #SUM #1 - EVERY OTHER DIGIT
    #print(i)
    c+=int(b[i])
#print (c)

pizda = 0
d = [] #LIST OF CHARS

for i in range(1,len(N),2): #ITERATING OTHER DIGITS
    p=int(N[i])
    for i in str(p):
        d.append(str(p)) #LIST OF CHARACTERS #2

e = 0 #SUM OF OTHER DIGITS

for i in range(0,len(d),1): #SUM #2 - EVERY OTHER DIGIT
    #print(i)
    e+=int(d[i])
#print (e)

x = e+c #FINAL SUM

if len(str(x))>2:
    print ("Invalid card")
elif str(x)[1] == '0':
    pass
else:
    print ("Invalid card")

#STRING ASSIGMENT BEFORE VALIDATION

if N[0:2] == '34' or '37' and len(card) == 15:
    print ("American express")
elif N[0:1] == '4' and len(card) == 16 or 13:
    print ("Visa")
elif N[0:2] == '51' or '52' or '53' or '54' or '55' and len(card) == 16:
    print ("MasterCard")

else:
    print ("Invalid card")