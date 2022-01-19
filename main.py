from random import randint, choice
x = 0

#Jakub Tichy

try:

    s1 = input("Zadej název prvního souboru prosím: \n")

    s2 = input("Zadej název druhého souboru děkuji: \n")

    f1 = open(s1, "r")

    f2 = open(s2, "w")


except FileNotFoundError:

    print("Jejda! Soubor neplatný.")
    x = 1


if x == 1:

    print('')


if x == 0:

    vyber = int(input("Prosím vyber úkon, který chceš provést : \n"
        "1 - Změna celého textu na malá písmnena \n"
        "2 - Výměna znaku za jiný \n"
        "3 - Výpis \n"
        "4 - Generování textu \n" ))

if vyber == 1:

    for line in f1:
        f2.write(line.lower())


if vyber == 2:

    char1 = input("Zadej znak, který chceš změnit: ")
    char2 = input("Zadej znak, na který budeme měnit: ")

    while True:

        char = f1.read(1)

        if char == "":
            break

        else:
            if char.upper() == char1.upper():
                f2.write(char2)
            else:
                f2.write(char)

if vyber == 3:

    txt = f1.read()
    print(txt)

    f1.close()
    kolik = {}

    for pismeno in txt:
        if pismeno.isalpha():

            if pismeno not in kolik.keys():
                kolik[pismeno] = 1
            else:
                kolik[pismeno] +=1

    print()

    maximum = max(kolik.values())
    for key in sorted(kolik.keys()):
        print("({0}) -> {1:4} | {2}".format(key, kolik[key],
        30 *  kolik[key]//maximum * "#"))

if vyber == 4:

    samohlasky = 'aeiouy'
    souhlasky = 'qwertzuiopasdfghjklyxcvbnm'

    def gen_z(minchars=1, maxchars=8):

        sumarum = ''

        kolik = randint(minchars, maxchars)

        if kolik == 1:
            zacatek = 0
        zacatek = randint(0,1)

        for i in range(kolik):

            if i % 2 == zacatek:
                sumarum = sumarum + choice(samohlasky)
            else:
                sumarum = sumarum + choice(souhlasky)
                if randint(1,10) == 1:
                    sumarum = sumarum + choice(souhlasky)

        return sumarum

    print(gen_z())


    def gen_v(minwords=4, maxwords=10):

        sumarum = ''

        for i in range(randint(minwords,maxwords)):

            sumarum = sumarum + gen_z() + ' '

        return sumarum.capitalize()[0:-1] + '.'


    def avg(a,b,c):

        return (a+b+c)/3


f1.close()
f2.close()
