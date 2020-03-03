import os
import random
import time 
from tkinter import *

print("Hey! As-tu vu tes notes, camarade?")
time.sleep(2)
print("Motive-toi sinon les profs seront rancuniers!")
time.sleep(2)
print("Choisis les quatres matières que tu veux travailler:")
time.sleep(2)
print("La première s'il te plait?:")
matieres = ['anglais','maths','francais','histoire']
scorem = 0
scorea = 0
scoree = 0
scoreh = 0
M1 = input('Entre la première matière: ')
M2 = input('Entre la deuxième matière: ')
M3 = input('Entre la troisième matière: ')
M4 = input('Entre la quatrième matière: ')
M5 = "score"
M6 = "quitter"
T1 = M1
while(1):
    T1 = input('Affiche ton score, la matière que tu veux travailler ou quitte: ')
    if T1 == M1 or T1 == M2 or T1 == M3 or T1 == M4 or T1 == M5 or T1 == M6:
        if T1 == "score":
            print('Score maths:' + str(scorem))
            print('Score anglais:' + str(scorea))
            print('Score espagnol:' + str(scoree))
            print('Score histoire:' + str(scoreh))
            
        elif T1 == "quitter":
            print("Au revoir et reviens vite pour de nouvelles aventures!")
            time.sleep(2)
            break
        
        elif T1 == "anglais" and scorea < scorem + 5 and scorea < scoree + 5 and scorea < scoreh + 5:
            print("Voici 5 questions " + str(T1))
            time.sleep(2)
            for i in range(5):
                Q =  random.randint(1,4) #ligne de la question
                f1 = open("anglais.txt", "r") #lire question
                for i in range(Q):
                    ligne = f1.readline()
                print(ligne)
                f2 = open("Vanglais.txt", "r") #lire bonne réponse
                for i in range(Q):
                    ligne1 = f2.readline()
                    nligne1 = 1
                f3 = open("Fanglais.txt", "r") #lire mauvaise réponse
                for i in range(Q):
                    ligne2 = f3.readline()
                    ligne2 = ligne2.strip()
                    nligne2 = 2
                R = random.randint(1,2) #questions aléatoires
                if R == nligne1:
                    print(ligne1)
                    print(ligne2)
                else:
                    print(ligne2)
                    print(ligne1)
                while i not in (ligne1, ligne2):
                    R1 = input("Réponse:")
                    if R1 == ligne1:
                        print("Bonne réponse!")
                        time.sleep(2)
                        scorea = scorea + 1
                        break
                    elif R1 == ligne2:
                        print("Mauvaise réponse!")
                        time.sleep(2)
                        break
                    else: 
                        print("Recommence")
                        time.sleep(2)            
    
                
        elif T1 == "maths" and scorem < scorea + 5 and scorem < scoree + 5 and scorem < scoreh + 5:
            print("Voici 5 questions " + str(T1))
            time.sleep(2)
            for i in range(5):
                Q =  random.randint(1,4) #ligne de la question
                f1 = open("maths.txt", "r") #lire question
                for i in range(Q):
                    ligne = f1.readline()
                print(ligne)
                f2 = open("Vmaths.txt", "r") #lire bonne réponse
                for i in range(Q):
                    ligne1 = f2.readline()
                    ligne1 = ligne1.strip()
                    nligne1 = 1
                f3 = open("Fmaths.txt", "r") #lire mauvaise réponse
                for i in range(Q):
                    ligne2 = f3.readline()
                    ligne2 = ligne2.strip()
                    nligne2 = 2
                R = random.randint(1,2) #questions aléatoires
                if R == nligne1:
                    print(ligne1)
                    print(ligne2)
                else:
                    print(ligne2)
                    print(ligne1)
                while i not in (ligne1, ligne2):
                    R1 = input("Réponse:")
                    if R1 == ligne1:
                        print("Bonne réponse!")
                        time.sleep(2)
                        scorem = scorem + 1
                        break
                    elif R1 == ligne2:
                        print("Mauvaise réponse!")
                        time.sleep(2)
                        break
                    else: 
                        print("Recommence")
                        time.sleep(2)
        
            
        elif T1 == "espagnol" and scoree < scorea + 5 and scoree < scorem + 5 and scoree < scoreh + 5:
            print("Voici 5 questions en " + str(T1))
            time.sleep(2)
            for i in range(5):
                Q =  random.randint(1,4) #ligne de la question
                f1 = open("espagnol.txt", "r") #lire question
                for i in range(Q):
                    ligne = f1.readline()
                print(ligne)
                f2 = open("Vespagnol.txt", "r") #lire bonne réponse
                for i in range(Q):
                    ligne1 = f2.readline()
                    ligne1 = ligne1.strip()
                    nligne1 = 1
                f3 = open("Fespagnol.txt", "r") #lire mauvaise réponse
                for i in range(Q):
                    ligne2 = f3.readline()
                    ligne2 = ligne2.strip()
                    nligne2 = 2
                R = random.randint(1,2) #questions aléatoires
                if R == nligne1:
                    print(ligne1)
                    print(ligne2)
                else:
                    print(ligne2)
                    print(ligne1)
                while i not in (ligne1, ligne2):
                    R1 = input("Réponse:")
                    if R1 == ligne1:
                        print("Bonne réponse!")
                        time.sleep(2)
                        scoree = scoree + 1
                        break
                    elif R1 == ligne2:
                        print("Mauvaise réponse!")
                        time.sleep(2)
                        break
                    else: 
                        print("Recommence")
                        time.sleep(2)
                        
        elif T1 == "histoire" and scoreh < scorea + 5 and scoreh < scorem + 5 and scoreh < scoree + 5:
            print("Voici 5 questions en " + str(T1))
            time.sleep(2)
            for i in range(5):
                Q =  random.randint(1,5) #ligne de la question
                f1 = open("histoire.txt", "r") #lire question
                for i in range(Q):
                    ligne = f1.readline()
                print(ligne)
                f2 = open("Vhistoire.txt", "r") #lire bonne réponse
                for i in range(Q):
                    ligne1 = f2.readline()
                    ligne1 = ligne1.strip()
                    nligne1 = 1
                f3 = open("Fhistoire.txt", "r") #lire mauvaise réponse
                for i in range(Q):
                    ligne2 = f3.readline()
                    ligne2 = ligne2.strip()
                    nligne2 = 2
                R = random.randint(1,2) #questions aléatoires
                if R == nligne1:
                    print(ligne1)
                    print(ligne2)
                else:
                    print(ligne2)
                    print(ligne1)
                while i not in (ligne1, ligne2):
                    R1 = input("Réponse:")
                    if R1 == ligne1:
                        print("Bonne réponse!")
                        time.sleep(2)
                        scoree = scoree + 1
                        break
                    elif R1 == ligne2:
                        print("Mauvaise réponse!")
                        time.sleep(2)
                        break
                    else: 
                        print("Recommence")
                        time.sleep(2)
        elif scoree >= scorem + 5 or scoree >= scorea + 5 or scoree >= scoreh +5:
            print('Tu as fais trop de questions sur cette matière, travaille les autres!')
        elif scorem >= scoree + 5 or scorem >= scorea + 5 or scorem >= scoreh +5:
            print('Tu as fais trop de questions sur cette matière, travaille les autres!')
        elif scorea >= scoree + 5 or scorea >= scorem + 5 or scorea >= scoreh +5:
            print('Tu as fais trop de questions sur cette matière, travaille les autres!')
        elif scoreh >= scoree + 5 or scoreh >= scorea + 5 or scoreh >= scorem +5:
            print('Tu as fais trop de questions sur cette matière, travaille les autres!')
    else:
        print("Ta commande n'est pas valable, recommence")
    
                
            