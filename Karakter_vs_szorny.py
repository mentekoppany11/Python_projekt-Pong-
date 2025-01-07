#Mente Koppány & Takács Bence 10_A

import random
import os
import time

def fej_vagy_iras():
    import random
    fvi_lista = ["f", "i"]
    while True:    
        fvi_valasztas = input("\nFej vagy írás(f/i)?\n - ").lower()
        if fvi_valasztas in fvi_lista:
            break
        else:
            print("Érvénytelen választás! Kérlek, csak 'f' vagy 'i' értéket adj meg.")
    vegeredmeny = random.choice(fvi_lista)
    if vegeredmeny == fvi_valasztas:
        kezdes = True
    else:
        kezdes = False
    return kezdes

#Változók

gyozelem = 0

abel = {
    "elet" : 1000,
    "tamadas" : 150,
    "crit_chance" : 26,
    "dodge" : 44
}

victor = {
    "elet" : 750,
    "tamadas" : 200,
    "crit_chance" : 18,
    "dodge" : 62
}

arthur = {
    "elet" : 1200,
    "tamadas" : 100,
    "crit_chance" : 55,
    "dodge" : 31
}

szorny1 = {
    "elet" : random.randint(600,1350),
    "tamadas" : random.randint(85,250),
    "crit_chance" : random.randint(24,50),
    "dodge" : random.randint(27,55)
}

while True:
    os.system("cls")
    time.sleep(1)
    print(f"""------------------------------
  --> Ábel
      élet - {int(abel['elet'])}
      támadás - {abel['tamadas']}
      Critchance - {abel['crit_chance']}
      Dodge - {abel['dodge']}
------------------------------
  --> Victor
      élet - {int(victor['elet'])}
      támadás - {victor['tamadas']}
      Critchance - {victor['crit_chance']}
      Dodge - {victor['dodge']}
------------------------------
  --> Arthur
      élet - {int(arthur['elet'])}
      támadás - {arthur['tamadas']}
      Critchance - {arthur['crit_chance']}
      Dodge - {arthur['dodge']}
------------------------------""")
    while True:
        karakter = input("Válasz egy karaktert!\n - ").lower()
        if karakter in ["ábel", "victor", "arthur", "dev"]:
            break
        else:
            print("Érvénytelen választás! Kérlek, csak a karakter nevét add meg.")
    while True:
        biztos = input("Biztosan ezzel a karakterrel akarsz lenni(i/n)?\n - ").lower()
        if biztos in ["i", "n"] or biztos == "dev":
            break
        else:
            print("Érvénytelen választás! Kérlek, csak 'i' vagy 'n' értéket adj meg.")
    if karakter == "dev" and biztos == "i":
        while True:
            dev_karakter = input("\nMelyik araktert akarod módosítani?\n - ").lower()
            if dev_karakter in ["ábel", "victor", "arthur"]:
                break
            else:
                print("Érvénytelen választás! Kérlek, csak a karakter nevét add meg.")
        if dev_karakter == "ábel":
            elet = int(input("Élet: "))
            tamadas = int(input("Tamadás: "))
            abel["elet"] = elet
            abel["tamadas"] = tamadas
        elif dev_karakter == "victor":
            elet = int(input("Élet: "))
            tamadas = int(input("Tamadás: "))
            victor["elet"] = elet
            victor["tamadas"] = tamadas
        elif dev_karakter == "arthur":
            elet = int(input("Élet: "))
            tamadas = int(input("Tamadás: "))
            arthur["elet"] = elet
            arthur["tamadas"] = tamadas

    else:
        if karakter == "ábel" and biztos == "i":
            os.system('cls')
            print("Akkor kezdődjön a játék!")

            while abel["elet"] > 0 and szorny1["elet"] > 0:
                    critchance = random.randint(1,100)
                    dodgechance = random.randint(1,100)
                    if fej_vagy_iras() == True:
                        os.system("cls")
                        print(f"""Te statjaid:\n------------------------------
  --> Ábel
      élet - {int(abel['elet'])}
      támadás - {abel['tamadas']}
      Critchance - {abel['crit_chance']}
      Dodge - {abel['dodge']}
------------------------------""")
                        print(f"""Az ellenfél statjai:\n------------------------------
  --> Ellenfél
      élet - {int(szorny1['elet'])}
      támadás - {szorny1['tamadas']}
      Critchance - {szorny1['crit_chance']}
      Dodge - {szorny1['dodge']}
------------------------------""")
                        print("\nA dobás végeredmény alapján TE jössz")
                        time.sleep(2)
                        if critchance <= abel["crit_chance"] and dodgechance > szorny1["dodge"]:
                            szorny1["elet"] -= abel["tamadas"] * (abel["crit_chance"]/100 + 1)
                            os.system("cls")
                            print("\nA párharc során kritkusámadást sulytottál az ellenfeledre.")
                            time.sleep(5)
                            os.system('cls')
                            print(f"""Te statjaid:\n------------------------------
  --> Ábel
      élet - {int(abel['elet'])}
      támadás - {abel['tamadas']}
      Critchance - {abel['crit_chance']}
      Dodge - {abel['dodge']}
------------------------------""")
                            print(f"""Az ellenfél statjai:\n------------------------------
  --> Ellenfél
      élet - {int(szorny1['elet'])}
      támadás - {szorny1['tamadas']}
      Critchance - {szorny1['crit_chance']}
      Dodge - {szorny1['dodge']}
------------------------------""")
                        elif critchance > abel["crit_chance"] and dodgechance > szorny1["dodge"]:
                            szorny1["elet"] -= abel["tamadas"]
                            os.system("cls")
                            print("\nA párharc során megsebezted az ellenfeled.")
                            time.sleep(5)
                            os.system("cls")
                            print(f"""Te statjaid:\n------------------------------
  --> Ábel
      élet - {int(abel['elet'])}
      támadás - {abel['tamadas']}
      Critchance - {abel['crit_chance']}
      Dodge - {abel['dodge']}
------------------------------""")
                            print(f"""Az ellenfél statjai:\n------------------------------
  --> Ellenfél
      élet - {int(szorny1['elet'])}
      támadás - {szorny1['tamadas']}
      Critchance - {szorny1['crit_chance']}
      Dodge - {szorny1['dodge']}
------------------------------""")
                        else:
                            os.system("cls")
                            print("\nAz ellenfeled kitért a támadásodból.")
                            time.sleep(5)
                            print(f"""Te statjaid:\n------------------------------
  --> Ábel
      élet - {int(abel['elet'])}
      támadás - {abel['tamadas']}
      Critchance - {abel['crit_chance']}
      Dodge - {abel['dodge']}
------------------------------""")
                            print(f"""Az ellenfél statjai:\n------------------------------
  --> Ellenfél
      élet - {int(szorny1['elet'])}
      támadás - {szorny1['tamadas']}
      Critchance - {szorny1['crit_chance']}
      Dodge - {szorny1['dodge']}
------------------------------""")
                    else:
                        os.system("cls")
                        print(f"""Te statjaid:\n------------------------------
  --> Ábel
      élet - {int(abel['elet'])}
      támadás - {abel['tamadas']}
      Critchance - {abel['crit_chance']}
      Dodge - {abel['dodge']}
------------------------------""")
                        print(f"""Az ellenfél statjai:\n------------------------------
  --> Ellenfél
      élet - {int(szorny1['elet'])}
      támadás - {szorny1['tamadas']}
      Critchance - {szorny1['crit_chance']}
      Dodge - {szorny1['dodge']}
------------------------------""")
                        print("\nA dobás végeredménye miatt az ELLENFELED kezd")
                        time.sleep(5)
                        if critchance <= abel["crit_chance"] and dodgechance > abel["dodge"]:
                            abel["elet"] -= szorny1["tamadas"] * (szorny1["crit_chance"]/100 + 1)
                            os.system("cls")
                            print("\nA párharc során kritkusámadást sulytott az ellenfeled rád.")
                            time.sleep(5)
                            os.system('cls')
                            print(f"""Te statjaid:\n------------------------------
  --> Ábel
      élet - {int(abel['elet'])}
      támadás - {abel['tamadas']}
      Critchance - {abel['crit_chance']}
      Dodge - {abel['dodge']}
------------------------------""")
                            print(f"""Az ellenfél statjai:\n------------------------------
  --> Ellenfél
      élet - {int(szorny1['elet'])}
      támadás - {szorny1['tamadas']}
      Critchance - {szorny1['crit_chance']}
      Dodge - {szorny1['dodge']}
------------------------------""")
                        elif critchance > szorny1["crit_chance"] and dodgechance > abel["dodge"]:
                            abel["elet"] -= szorny1["tamadas"]
                            os.system("cls")
                            print("\nA párharc során megsebzett az ellenfeled.")
                            time.sleep(5)
                            os.system("cls")
                            print(f"""Te statjaid:\n------------------------------
  --> Ábel
      élet - {int(abel['elet'])}
      támadás - {abel['tamadas']}
      Critchance - {abel['crit_chance']}
      Dodge - {abel['dodge']}
------------------------------""")
                            print(f"""Az ellenfél statjai:\n------------------------------
  --> Ellenfél
      élet - {int(szorny1['elet'])}
      támadás - {szorny1['tamadas']}
      Critchance - {szorny1['crit_chance']}
      Dodge - {szorny1['dodge']}
------------------------------""")
                        else:
                            os.system("cls")
                            print("\nKitértél az ellen feled támadásodból.")
                            time.sleep(5)
                            print(f"""Te statjaid:\n------------------------------
  --> Ábel
      élet - {int(abel['elet'])}
      támadás - {abel['tamadas']}
      Critchance - {abel['crit_chance']}
      Dodge - {abel['dodge']}
------------------------------""")
                            print(f"""Az ellenfél statjai:\n------------------------------
  --> Ellenfél
      élet - {int(szorny1['elet'])}
      támadás - {szorny1['tamadas']}
      Critchance - {szorny1['crit_chance']}
      Dodge - {szorny1['dodge']}
------------------------------""")
            if abel["elet"] <= 0:
                os.system('cls')
                print("Legyőzött az ellenfeled, meghaltál.")
                time.sleep(2)
                while True:
                    ujra = input("\nSzeretnél ujra játszani(i/n)?\n - ")
                    if ujra in ["i", "n"]:
                        break
                    else:
                        print("Érvénytelen választás! Kérlek, csak 'i' vagy 'n' értéket adj meg.")
                if ujra == "i":
                    karakter = "ujra"
                    abel["elet"] = 1000
                    abel["tamadas"] = 150
                    abel["crit_chance"] = 26
                    abel["dodge"] = 44
                elif ujra == "n":
                    print("Harcaid során ennyi szörnyet győztél le: ", gyozelem)
                    break
            else:
                gyozelem += 1
                os.system('cls')
                print("Sikeresen legyőzted ellenfeled!")
                time.sleep(2)
                while True:
                    ujra = input("\nSzeretnél ujra játszani(i/n)?\n - ")
                    if ujra in ["i", "n"]:
                        break
                    else:
                        print("Érvénytelen választás! Kérlek, csak 'i' vagy 'n' értéket adj meg.")
                if ujra == "i":
                        karakter = "ujra"
                        abel["elet"] = 1000
                        abel["tamadas"] = 150
                        abel["crit_chance"] = 26
                        abel["dodge"] = 44
                elif ujra == "n":
                    print("Harcaid során ennyi szörnyet győztél le: ", gyozelem)
                    break
        if karakter == "victor" and biztos == "i":
            os.system('cls')
            print("Akkor kezdődjön a játék!")

            while victor["elet"] > 0 and szorny1["elet"] > 0:
                    critchance = random.randint(1,100)
                    dodgechance = random.randint(1,100)
                    if fej_vagy_iras() == True:
                        os.system("cls")
                        print(f"""Te statjaid:\n------------------------------
  --> Victor
      élet - {int(victor['elet'])}
      támadás - {victor['tamadas']}
      Critchance - {victor['crit_chance']}
      Dodge - {victor['dodge']}
------------------------------""")
                        print(f"""Az ellenfél statjai:\n------------------------------
  --> Ellenfél
      élet - {int(szorny1['elet'])}
      támadás - {szorny1['tamadas']}
      Critchance - {szorny1['crit_chance']}
      Dodge - {szorny1['dodge']}
------------------------------""")
                        print("\nA dobás végeredmény alapján TE jössz")
                        time.sleep(2)
                        if critchance <= victor["crit_chance"] and dodgechance > szorny1["dodge"]:
                            szorny1["elet"] -= victor["tamadas"] * (victor["crit_chance"]/100 + 1)
                            os.system("cls")
                            print("\nA párharc során kritkusámadást sulytottál az ellenfeledre.")
                            time.sleep(5)
                            os.system('cls')
                            print(f"""Te statjaid:\n------------------------------
  --> Victor
      élet - {int(victor['elet'])}
      támadás - {victor['tamadas']}
      Critchance - {victor['crit_chance']}
      Dodge - {victor['dodge']}
------------------------------""")
                            print(f"""Az ellenfél statjai:\n------------------------------
  --> Ellenfél
      élet - {int(szorny1['elet'])}
      támadás - {szorny1['tamadas']}
      Critchance - {szorny1['crit_chance']}
      Dodge - {szorny1['dodge']}
------------------------------""")
                        elif critchance > victor["crit_chance"] and dodgechance > szorny1["dodge"]:
                            szorny1["elet"] -= victor["tamadas"]
                            os.system("cls")
                            print("\nA párharc során megsebezted az ellenfeled.")
                            time.sleep(5)
                            os.system("cls")
                            print(f"""Te statjaid:\n------------------------------
  --> Victor
      élet - {int(victor['elet'])}
      támadás - {victor['tamadas']}
      Critchance - {victor['crit_chance']}
      Dodge - {victor['dodge']}
------------------------------""")
                            print(f"""Az ellenfél statjai:\n------------------------------
  --> Ellenfél
      élet - {int(szorny1['elet'])}
      támadás - {szorny1['tamadas']}
      Critchance - {szorny1['crit_chance']}
      Dodge - {szorny1['dodge']}
------------------------------""")
                        else:
                            os.system("cls")
                            print("\nAz ellenfeled kitért a támadásodból.")
                            time.sleep(5)
                            print(f"""Te statjaid:\n------------------------------
  --> Victor
      élet - {int(victor['elet'])}
      támadás - {victor['tamadas']}
      Critchance - {victor['crit_chance']}
      Dodge - {victor['dodge']}
------------------------------""")
                            print(f"""Az ellenfél statjai:\n------------------------------
  --> Ellenfél
      élet - {int(szorny1['elet'])}
      támadás - {szorny1['tamadas']}
      Critchance - {szorny1['crit_chance']}
      Dodge - {szorny1['dodge']}
------------------------------""")
                    else:
                        os.system("cls")
                        print(f"""Te statjaid:\n------------------------------
  --> Victor
      élet - {int(victor['elet'])}
      támadás - {victor['tamadas']}
      Critchance - {victor['crit_chance']}
      Dodge - {victor['dodge']}
------------------------------""")
                        print(f"""Az ellenfél statjai:\n------------------------------
  --> Ellenfél
      élet - {int(szorny1['elet'])}
      támadás - {szorny1['tamadas']}
      Critchance - {szorny1['crit_chance']}
      Dodge - {szorny1['dodge']}
------------------------------""")
                        print("\nA dobás végeredménye miatt az ELLENFELED kezd")
                        time.sleep(5)
                        if critchance <= victor["crit_chance"] and dodgechance > victor["dodge"]:
                            victor["elet"] -= szorny1["tamadas"] * (szorny1["crit_chance"]/100 + 1)
                            os.system("cls")
                            print("\nA párharc során kritkusámadást sulytott az ellenfeled rád.")
                            time.sleep(5)
                            os.system('cls')
                            print(f"""Te statjaid:\n------------------------------
  --> Victor
      élet - {int(victor['elet'])}
      támadás - {victor['tamadas']}
      Critchance - {victor['crit_chance']}
      Dodge - {victor['dodge']}
------------------------------""")
                            print(f"""Az ellenfél statjai:\n------------------------------
  --> Ellenfél
      élet - {int(szorny1['elet'])}
      támadás - {szorny1['tamadas']}
      Critchance - {szorny1['crit_chance']}
      Dodge - {szorny1['dodge']}
------------------------------""")
                        elif critchance > szorny1["crit_chance"] and dodgechance > victor["dodge"]:
                            victor["elet"] -= szorny1["tamadas"]
                            os.system("cls")
                            print("\nA párharc során megsebzett az ellenfeled.")
                            time.sleep(5)
                            os.system("cls")
                            print(f"""Te statjaid:\n------------------------------
  --> Victor
      élet - {int(victor['elet'])}
      támadás - {victor['tamadas']}
      Critchance - {victor['crit_chance']}
      Dodge - {victor['dodge']}
------------------------------""")
                            print(f"""Az ellenfél statjai:\n------------------------------
  --> Ellenfél
      élet - {int(szorny1['elet'])}
      támadás - {szorny1['tamadas']}
      Critchance - {szorny1['crit_chance']}
      Dodge - {szorny1['dodge']}
------------------------------""")
                        else:
                            os.system("cls")
                            print("\nKitértél az ellen feled támadásodból.")
                            time.sleep(5)
                            print(f"""Te statjaid:\n------------------------------
  --> Victor
      élet - {int(victor['elet'])}
      támadás - {victor['tamadas']}
      Critchance - {victor['crit_chance']}
      Dodge - {victor['dodge']}
------------------------------""")
                            print(f"""Az ellenfél statjai:\n------------------------------
  --> Ellenfél
      élet - {int(szorny1['elet'])}
      támadás - {szorny1['tamadas']}
      Critchance - {szorny1['crit_chance']}
      Dodge - {szorny1['dodge']}
------------------------------""")
            if victor["elet"] <= 0:
                os.system('cls')
                print("Legyőzött az ellenfeled, meghaltál.")
                time.sleep(2)
                while True:
                    ujra = input("\nSzeretnél ujra játszani(i/n)?\n - ")
                    if ujra in ["i", "n"]:
                        break
                    else:
                        print("Érvénytelen választás! Kérlek, csak 'i' vagy 'n' értéket adj meg.")
                if ujra == "i":
                    karakter = "ujra"
                    victor["elet"] = 750
                    victor["tamadas"] = 200
                    victor["crit_chance"] = 18
                    victor["dodge"] = 62
                elif ujra == "n":
                    print("Harcaid során ennyi szörnyet győztél le: ", gyozelem)
                    break
            else:
                gyozelem += 1
                os.system('cls')
                print("Sikeresen legyőzted ellenfeled!")
                time.sleep(2)
                while True:
                    ujra = input("\nSzeretnél ujra játszani(i/n)?\n - ")
                    if ujra in ["i", "n"]:
                        break
                    else:
                        print("Érvénytelen választás! Kérlek, csak 'i' vagy 'n' értéket adj meg.")
                if ujra == "i":
                    while True:
                        karakter = "ujra"
                        victor["elet"] = 750
                        victor["tamadas"] = 200
                        victor["crit_chance"] = 18
                        victor["dodge"] = 62
                elif ujra == "n":
                    print("Harcaid során ennyi szörnyet győztél le: ", gyozelem)
                    break        
        if karakter == "arthur" and biztos == "i":
            os.system('cls')
            print("Akkor kezdődjön a játék!")
            while arthur["elet"] > 0 and szorny1["elet"] > 0:
                    critchance = random.randint(1,100)
                    dodgechance = random.randint(1,100)
                    if fej_vagy_iras() == True:
                        os.system("cls")
                        print(f"""Te statjaid:\n------------------------------
  --> Arthur
      élet - {int(arthur['elet'])}
      támadás - {arthur['tamadas']}
      Critchance - {arthur['crit_chance']}
      Dodge - {arthur['dodge']}
------------------------------""")
                        print(f"""Az ellenfél statjai:\n------------------------------
  --> Ellenfél
      élet - {int(szorny1['elet'])}
      támadás - {szorny1['tamadas']}
      Critchance - {szorny1['crit_chance']}
      Dodge - {szorny1['dodge']}
------------------------------""")
                        print("\nA dobás végeredmény alapján TE jössz")
                        time.sleep(2)
                        if critchance <= arthur["crit_chance"] and dodgechance > szorny1["dodge"]:
                            szorny1["elet"] -= arthur["tamadas"] * (arthur["crit_chance"]/100 + 1)
                            os.system("cls")
                            print("\nA párharc során kritkusámadást sulytottál az ellenfeledre.")
                            time.sleep(5)
                            os.system('cls')
                            print(f"""Te statjaid:\n------------------------------
  --> Arthur
      élet - {int(arthur['elet'])}
      támadás - {arthur['tamadas']}
      Critchance - {arthur['crit_chance']}
      Dodge - {arthur['dodge']}
------------------------------""")
                            print(f"""Az ellenfél statjai:\n------------------------------
  --> Ellenfél
      élet - {int(szorny1['elet'])}
      támadás - {szorny1['tamadas']}
      Critchance - {szorny1['crit_chance']}
      Dodge - {szorny1['dodge']}
------------------------------""")
                        elif critchance > arthur["crit_chance"] and dodgechance > szorny1["dodge"]:
                            szorny1["elet"] -= arthur["tamadas"]
                            os.system("cls")
                            print("\nA párharc során megsebezted az ellenfeled.")
                            time.sleep(5)
                            os.system("cls")
                            print(f"""Te statjaid:\n------------------------------
  --> Arthur
      élet - {int(arthur['elet'])}
      támadás - {arthur['tamadas']}
      Critchance - {arthur['crit_chance']}
      Dodge - {arthur['dodge']}
------------------------------""")
                            print(f"""Az ellenfél statjai:\n------------------------------
  --> Ellenfél
      élet - {int(szorny1['elet'])}
      támadás - {szorny1['tamadas']}
      Critchance - {szorny1['crit_chance']}
      Dodge - {szorny1['dodge']}
------------------------------""")
                        else:
                            os.system("cls")
                            print("\nAz ellenfeled kitért a támadásodból.")
                            time.sleep(5)
                            print(f"""Te statjaid:\n------------------------------
  --> Arthur
      élet - {int(arthur['elet'])}
      támadás - {arthur['tamadas']}
      Critchance - {arthur['crit_chance']}
      Dodge - {arthur['dodge']}
------------------------------""")
                            print(f"""Az ellenfél statjai:\n------------------------------
  --> Ellenfél
      élet - {int(szorny1['elet'])}
      támadás - {szorny1['tamadas']}
      Critchance - {szorny1['crit_chance']}
      Dodge - {szorny1['dodge']}
------------------------------""")
                    else:
                        os.system("cls")
                        print(f"""Te statjaid:\n------------------------------
  --> Arthur
      élet - {int(arthur['elet'])}
      támadás - {arthur['tamadas']}
      Critchance - {arthur['crit_chance']}
      Dodge - {arthur['dodge']}
------------------------------""")
                        print(f"""Az ellenfél statjai:\n------------------------------
  --> Ellenfél
      élet - {int(szorny1['elet'])}
      támadás - {szorny1['tamadas']}
      Critchance - {szorny1['crit_chance']}
      Dodge - {szorny1['dodge']}
------------------------------""")
                        print("\nA dobás végeredménye miatt az ELLENFELED kezd")
                        time.sleep(5)
                        if critchance <= arthur["crit_chance"] and dodgechance > arthur["dodge"]:
                            arthur["elet"] -= szorny1["tamadas"] * (szorny1["crit_chance"]/100 + 1)
                            os.system("cls")
                            print("\nA párharc során kritkusámadást sulytott az ellenfeled rád.")
                            time.sleep(5)
                            os.system('cls')
                            print(f"""Te statjaid:\n------------------------------
  --> Arthur
      élet - {int(arthur['elet'])}
      támadás - {arthur['tamadas']}
      Critchance - {arthur['crit_chance']}
      Dodge - {arthur['dodge']}
------------------------------""")
                            print(f"""Az ellenfél statjai:\n------------------------------
  --> Ellenfél
      élet - {int(szorny1['elet'])}
      támadás - {szorny1['tamadas']}
      Critchance - {szorny1['crit_chance']}
      Dodge - {szorny1['dodge']}
------------------------------""")
                        elif critchance > szorny1["crit_chance"] and dodgechance > arthur["dodge"]:
                            arthur["elet"] -= szorny1["tamadas"]
                            os.system("cls")
                            print("\nA párharc során megsebzett az ellenfeled.")
                            time.sleep(5)
                            os.system("cls")
                            print(f"""Te statjaid:\n------------------------------
  --> Arthur
      élet - {int(arthur['elet'])}
      támadás - {arthur['tamadas']}
      Critchance - {arthur['crit_chance']}
      Dodge - {arthur['dodge']}
------------------------------""")
                            print(f"""Az ellenfél statjai:\n------------------------------
  --> Ellenfél
      élet - {int(szorny1['elet'])}
      támadás - {szorny1['tamadas']}
      Critchance - {szorny1['crit_chance']}
      Dodge - {szorny1['dodge']}
------------------------------""")
                        else:
                            os.system("cls")
                            print("\nKitértél az ellen feled támadásodból.")
                            time.sleep(5)
                            print(f"""Te statjaid:\n------------------------------
  --> Arthur
      élet - {int(arthur['elet'])}
      támadás - {arthur['tamadas']}
      Critchance - {arthur['crit_chance']}
      Dodge - {arthur['dodge']}
------------------------------""")
                            print(f"""Az ellenfél statjai:\n------------------------------
  --> Ellenfél
      élet - {int(szorny1['elet'])}
      támadás - {szorny1['tamadas']}
      Critchance - {szorny1['crit_chance']}
      Dodge - {szorny1['dodge']}
------------------------------""")
            if arthur["elet"] <= 0:
                os.system('cls')
                print("Legyőzött az ellenfeled, meghaltál.")
                time.sleep(2)
                while True:
                    ujra = input("\nSzeretnél ujra játszani(i/n)?\n - ")
                    if ujra in ["i", "n"]:
                        break
                    else:
                        print("Érvénytelen választás! Kérlek, csak 'i' vagy 'n' értéket adj meg.")
                if ujra == "i":
                    karakter = "ujra"
                    arthur["elet"] = 1200
                    arthur["tamadas"] = 200
                    arthur["crit_chance"] = 55
                    arthur["dodge"] = 31
                elif ujra == "n":
                    print("Harcaid során ennyi szörnyet győztél le: ", gyozelem)
                    break
            else:
                gyozelem += 1
                os.system('cls')
                print("Sikeresen legyőzted ellenfeled!")
                time.sleep(2)
                while True:
                    ujra = input("\nSzeretnél ujra játszani(i/n)?\n - ")
                    if ujra in ["i", "n"]:
                        break
                    else:
                        print("Érvénytelen választás! Kérlek, csak 'i' vagy 'n' értéket adj meg.")
                if ujra == "i":
                        karakter = "ujra"
                        arthur["elet"] = 1200
                        arthur["tamadas"] = 200
                        arthur["crit_chance"] = 56
                        arthur["dodge"] = 31
                elif ujra == "n":
                    print("Harcaid során ennyi szörnyet győztél le: ", gyozelem)
                    break