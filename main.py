import random
import string
passwords = []
for _ in range(5):
    password = ''.join(random.choices(string.ascii_lowercase, k=15))
    passwords.append(password)


#1
dic = {}
set1 = set()
set2 = set()
set3 = set()

passW = "abcde"

character = input("Enter a lowercase character:")
while(True):
    replacement = input("Enter a replacement for " + character + ": ")
    if (len(replacement) != 1): continue
    dic[replacement] = set1
    set1.add(replacement)
    if(len(set1) == 3): break


character2 = input("Enter a lowercase character:")
while(True):
    replacement = input("Enter a replacement for " + character2 + ": ")
    if (len(replacement) != 1): continue
    dic[replacement] = set2
    set2.add(replacement)
    if(len(set2) == 3): break


character3 = input("Enter a lowercase character:")
while(True):
    replacement = input("Enter a replacement for " + character3 + ": ")
    if(len(replacement) != 1): continue
    dic[replacement] = set3
    set3.add(replacement)
    if(len(set3) == 3): break


for i in range(len(passW)):
    if(passW[i] in dic):
        passW[i] = string(random.choices(dic[passW[i]]))



