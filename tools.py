"""
Autor : Ray-Nox
Date (create) : 29/10/2022
Date (last update) : 15/12/2022
/!\ Requirment : colorama
Utilities : - ipcalc() : Addresse IP calculator
            - event() : How much time separates us from an event.
            - pow2ex() : Practising powers of 2 [0-16]
            - multiplication_table() : revise your multiplication tables [0-10]
"""

from time import time, localtime, sleep
from random import randint
from tkinter import *
from colorama import init
from termcolor import colored
from colorama import Fore, Back, Style
init()

'''
--- Fonctions ---
'''


# Fonctions de calculs
def et8(liste1: list, liste2: list):
    res = []
    for i in range(8):
        res.append(liste1[i] * liste2[i])
    return res


def ou8(liste1: list, liste2: list):
    res = []
    for i in range(8):
        if liste1[i] == 1 or liste2[i] == 1:
            res.append(1)
        else:
            res.append(0)
    return res


def non8(liste: list):
    res = []
    for i in range(8):
        if liste[i] == 1:
            res.append(0)
        else:
            res.append(1)
    return res


def dec2bin8(n: int):
    res = []
    b = 128
    for i in range(8):
        if n >= b:
            res.append(1)
            n -= b
        else:
            res.append(0)
        b = b // 2
    return res


def bin2dec8(liste: list):
    res = 0
    for i in range(8):
        res += liste[7 - i] * 2 ** i
    return res


def cidr2bin32(n: int):
    res = []
    for i in range(32):
        if i < n:
            res.append(1)
        else:
            res.append(0)
    return res


def bin2cidr32(liste: list):
    res = 0
    for i in range(32):
        res += liste[i]
    return res


def adrbin2adrdec(o1, o2, o3, o4):
    o1 = bin2dec8(o1)
    o2 = bin2dec8(o2)
    o3 = bin2dec8(o3)
    o4 = bin2dec8(o4)
    res = str(o1) + "." + str(o2) + "." + str(o3) + "." + str(o4)
    return res


# Fonctions du script
def ipcalc():
    """
    --- Programme ---
    """
    # Données
    adresse = str(input(Fore.LIGHTCYAN_EX + "Adresse [W.X.Y.Z] : " + Fore.RESET))
    mask = str(input(Fore.LIGHTCYAN_EX + "Masque [1-31] : " + Fore.RESET))
    masque = None
    if "." in mask:  # decimal pointée
        mask_lst = mask.split(".")
        if len(mask_lst) != 4:
            print("")
            print("Erreur : la saisie du masque n'est pas au format attendu.")
            print("")
            main()
        o1mask = mask_lst[0]
        o2mask = mask_lst[1]
        o3mask = mask_lst[2]
        o4mask = mask_lst[3]

        o1mask_bin = dec2bin8(int(o1mask))
        o2mask_bin = dec2bin8(int(o2mask))
        o3mask_bin = dec2bin8(int(o3mask))
        o4mask_bin = dec2bin8(int(o4mask))
        mask_bin = []
        for i in range(8):
            mask_bin.append(o1mask_bin[i])
        for i in range(8):
            mask_bin.append(o2mask_bin[i])
        for i in range(8):
            mask_bin.append(o3mask_bin[i])
        for i in range(8):
            mask_bin.append(o4mask_bin[i])
        masque = bin2cidr32(mask_bin)

        if mask_bin != cidr2bin32(masque):
            print("")
            print(Fore.RED + "Erreur : la saisie du masque n'est pas au format attendu." + Fore.RESET)
            print("")
            main()

    elif 1 <= int(mask) <= 31:  # cidr
        masque = mask  # cidr
    else:
        print("")
        print(Fore.RED + "Erreur : la saisie du masque n'est pas au format attendu." + Fore.RESET)
        print("")
        main()

    # Tri des données
    # ADRESSE
    adresse_lst = adresse.split(".")
    if len(adresse_lst) != 4 or adresse_lst[0] == '' or adresse_lst[3] == '':
        print("")
        print(Fore.RED + "Erreur : la saisie de l'adresse n'est pas au format attendu." + Fore.RESET)
        print("")
        main()
    o1adr = int(adresse_lst[0])
    o2adr = int(adresse_lst[1])
    o3adr = int(adresse_lst[2])
    o4adr = int(adresse_lst[3])

    o1adr_bin = dec2bin8(o1adr)
    o2adr_bin = dec2bin8(o2adr)
    o3adr_bin = dec2bin8(o3adr)
    o4adr_bin = dec2bin8(o4adr)

    # MASK
    masquebin = cidr2bin32(int(masque))
    o1masquebin = []
    o2masquebin = []
    o3masquebin = []
    o4masquebin = []

    for i in range(24, 32):
        o4masquebin.append(masquebin[i])
    for i in range(16, 24):
        o3masquebin.append(masquebin[i])
    for i in range(8, 16):
        o2masquebin.append(masquebin[i])
    for i in range(0, 8):
        o1masquebin.append(masquebin[i])

        # MASK_INV
    o1masquebin_inv = non8(o1masquebin)
    o2masquebin_inv = non8(o2masquebin)
    o3masquebin_inv = non8(o3masquebin)
    o4masquebin_inv = non8(o4masquebin)

    # Calculs adresse réseau
    o1a_res_bin = et8(o1adr_bin, o1masquebin)
    o2a_res_bin = et8(o2adr_bin, o2masquebin)
    o3a_res_bin = et8(o3adr_bin, o3masquebin)
    o4a_res_bin = et8(o4adr_bin, o4masquebin)

    o1a_res = bin2dec8(o1a_res_bin)
    o2a_res = bin2dec8(o2a_res_bin)
    o3a_res = bin2dec8(o3a_res_bin)
    o4a_res = bin2dec8(o4a_res_bin)

    adresse_reseau = str(o1a_res) + "." + str(o2a_res) + "." + str(o3a_res) + "." + str(o4a_res)

    # Calculs adresse de diffusion
    o1a_bdt_bin = ou8(o1adr_bin, o1masquebin_inv)
    o2a_bdt_bin = ou8(o2adr_bin, o2masquebin_inv)
    o3a_bdt_bin = ou8(o3adr_bin, o3masquebin_inv)
    o4a_bdt_bin = ou8(o4adr_bin, o4masquebin_inv)

    o1a_bdt = bin2dec8(o1a_bdt_bin)
    o2a_bdt = bin2dec8(o2a_bdt_bin)
    o3a_bdt = bin2dec8(o3a_bdt_bin)
    o4a_bdt = bin2dec8(o4a_bdt_bin)

    adresse_broadcast = str(o1a_bdt) + "." + str(o2a_bdt) + "." + str(o3a_bdt) + "." + str(o4a_bdt)

    # Calculs adresse machine
    o1a_mac_bin = et8(o1adr_bin, o1masquebin_inv)
    o2a_mac_bin = et8(o2adr_bin, o2masquebin_inv)
    o3a_mac_bin = et8(o3adr_bin, o3masquebin_inv)
    o4a_mac_bin = et8(o4adr_bin, o4masquebin_inv)

    o1a_mac = bin2dec8(o1a_mac_bin)
    o2a_mac = bin2dec8(o2a_mac_bin)
    o3a_mac = bin2dec8(o3a_mac_bin)
    o4a_mac = bin2dec8(o4a_mac_bin)

    adresse_machine = str(o1a_mac) + "." + str(o2a_mac) + "." + str(o3a_mac) + "." + str(o4a_mac)

    # Calcul nombre d'hosts
    nombre_hosts = 2 ** (32 - int(masque)) - 2

    # RFC1918
    if o1a_res == 10 and int(masque) >= 8:
        rfc1918 = "privée"
    elif o1a_res == 192 and o2a_res == 168 and int(masque) >= 16:
        rfc1918 = "privée"
    elif o1a_res == 172 and 16 < o2a_res < 31 and int(masque) >= 12:
        rfc1918 = "privée"
    else:
        rfc1918 = "publique"

    # Sortie
    print("")
    print(Fore.LIGHTYELLOW_EX + " adresse  réseau  = ", adresse_reseau)
    print("adresse broadcast = ", adresse_broadcast)
    print(" adresse machine  = ", adresse_machine)
    print(" nombre  d'hotes  = ", nombre_hosts)
    print("     RFC1918      = ", rfc1918 + Fore.RESET)
    print("")
    # codes retour
    '''
    if adresse == adresse_reseau:
        print(" type  d'adresse  = réseau")
        raise Exception(2)
    elif adresse == adresse_broadcast:
        print(" type  d'adresse  = diffusion")
        raise Exception(4)
    else:
        print(" type  d'adresse  = ordinaire")
        raise Exception(0)
    '''
    main()
    '''
    --- Variables utiles ---
    adresse_reseau
    adresse_broadcast
    adresse_machine
    nombre_hosts
    type_adresse
    '''


def pow2ex():
    question = 1
    score = 0
    N = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    A = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]
    print("Quel mode souhaitez-vous utiliser ?")
    mode = input("[1/learn] ou [2/test] : ")
    if int(mode) == 1 or mode == "learn" or mode == "l":
        q = []
        nb_q = int(input("Nombre de questions souhaitées : "))
        for i in range(nb_q):
            q.append(randint(0, 16))
        a = 0
        while a < nb_q:
            if a < nb_q // 2:
                print("question ", a + 1, "/", nb_q)
                print(A[q[a]])
                rep = input("= 2**")
                if int(rep) == int(N[q[a]]):
                    score += 1
                    print(Fore.GREEN + "Bien joué ! Continuez comme ça" + Fore.RESET)
                else:
                    print(Fore.RED + "Dommage...")
                    print(A[q[a]], " = 2**", N[q[a]], "" + Fore.RESET)
                for j in range(5):
                    print("")
            else:
                print("question ", a + 1, "/", nb_q)
                print("2**", N[q[a]])
                rep = input("= ")
                if int(rep) == int(A[q[a]]):
                    score += 1
                    print(Fore.GREEN + "Bien joué ! Continuez comme ça" + Fore.RESET)
                else:
                    print(Fore.RED + "Dommage...")
                    print("2**", N[q[a]], " = ", A[q[a]], "" + Fore.RESET)
                for j in range(5):
                    print("")
            a += 1
        print("score = ", score, "/", nb_q)
        print("")
        print("----------")
        print("")
        main()
    if int(mode) == 2 or mode == "test" or mode == "t":
        t_deb = time()
        while question <= 20:
            A_ou_N = randint(0, 1)
            if A_ou_N == 0:
                q = randint(0, 16)
                print(A[q])
                rep = input("= 2**")
                if int(rep) == int(N[q]):
                    score += 1
            else:
                q = randint(0, 1)
                print("2**", N[q])
                rep = input("= ")
                if int(rep) == int(A[q]):
                    score += 1
            for i in range(5):
                print("")
            question += 1
        t_fin = time()
        temps_s = int(t_fin - t_deb)
        if score >= 15:
            print(Fore.GREEN + "score = ", score, "/20" + Fore.RESET)
        else:
            print(Fore.RED + "score = ", score, "/20" + Fore.RESET)
            print(Fore.RED + "temps = ", temps_s, " secondes" + Fore.RESET)
            if temps_s > 59:
                temps_m = temps_s // 60
                temps_s = temps_s % 60
                print(Fore.RED + "soit, ", temps_m, "minutes et ", temps_s, " secondes" + Fore.RESET)
            main()
        if int(temps_s) <= 30:
            print(Fore.GREEN + "temps = ", temps_s, " secondes" + Fore.RESET)
        else:
            print(Fore.RED + "temps = ", temps_s, " secondes" + Fore.RESET)
            if temps_s > 59:
                temps_m = temps_s // 60
                temps_s = temps_s % 60
                print(Fore.RED + "soit, ", temps_m, "minutes et ", temps_s, " secondes" + Fore.RESET)
        print("")
        main()


def event():
    print(Back.RED + Fore.LIGHTWHITE_EX + "La fonction est destinée pour un usage maitrisé, les erreurs d'entrées ne "
                                          "sont pas gérées." + Style.RESET_ALL)
    date_cible = input(Fore.LIGHTCYAN_EX + "Jour cible [jj/mm/aaaa] | [0](pour aujourd'hui) : " + Fore.RESET)
    heure_cible = input(Fore.LIGHTCYAN_EX + "Heure cible [hh:mm:ss] | [0](pas d'heure precise) : " + Fore.RESET)
    date_now = localtime()
    date_now_lst1 = str(date_now).split(", ")
    date_now_lst2 = []
    for i in range(len(date_now_lst1) - 3):
        var_tmp = date_now_lst1[i].split("=")
        date_now_lst2.append(var_tmp[1])
    date_now_dict = {"aaaa": date_now_lst2[0], "mm": date_now_lst2[1], "jj": date_now_lst2[2]}
    heure_now_dict = {"hh": date_now_lst2[3], "mm": date_now_lst2[4], "ss": date_now_lst2[5]}
    date_cible_dict = {}
    if str(date_cible) == str(0):
        date_cible_dict["aaaa"] = date_now_dict["aaaa"]
        date_cible_dict["mm"] = date_now_dict["mm"]
        date_cible_dict["jj"] = date_now_dict["jj"]
    else:
        date_cible_lst = date_cible.split("/")
        date_cible_dict["aaaa"] = date_cible_lst[2]
        date_cible_dict["mm"] = date_cible_lst[1]
        date_cible_dict["jj"] = date_cible_lst[0]
    heure_cible_dict = {}
    if str(heure_cible) == str(0):
        heure_cible_dict["hh"] = heure_now_dict["hh"]
        heure_cible_dict["mm"] = heure_now_dict["mm"]
        heure_cible_dict["ss"] = heure_now_dict["ss"]
    else:
        heure_cible_lst = heure_cible.split(":")
        heure_cible_dict["hh"] = heure_cible_lst[0]
        heure_cible_dict["mm"] = heure_cible_lst[1]
        heure_cible_dict["ss"] = heure_cible_lst[2]
    '''
    print("")
    print("date now = ", date_now_dict)
    print("heure now = ", heure_now_dict)
    print("")
    print("date cible = ", date_cible_dict)
    print("heure cible = ", heure_cible_dict)
    print("")
    '''
    r = 0
    sec = int(heure_cible_dict["ss"]) - int(heure_now_dict["ss"])
    if sec < 0:
        sec += 60
        r += 1
    min = int(heure_cible_dict["mm"]) - int(heure_now_dict["mm"]) - r
    r = 0
    if min < 0:
        min += 60
        r += 1
    hou = int(heure_cible_dict["hh"]) - int(heure_now_dict["hh"]) - r
    r = 0
    if hou < 0:
        hou += 24
        r += 1
    day = int(date_cible_dict["jj"]) - int(date_now_dict["jj"]) - r
    r = 0
    if day < 0:
        day += 30
        r += 1
    month =int(date_cible_dict["mm"]) - int(date_now_dict["mm"]) - r
    r = 0
    if month < 0:
        month += 12
        r += 1
    year = int(date_cible_dict["aaaa"]) -  int(date_now_dict["aaaa"]) - r
    a = 0

    temps = {"aaaa":year, "mm":month, "jj":day, "h":hou, "min":min, "s":sec}
    # print(temps)
    if year < 0:
        r = 0
        sec = int(heure_now_dict["ss"]) - int(heure_cible_dict["ss"])
        if sec < 0:
            sec += 60
            r += 1
        min = int(heure_now_dict["mm"]) - int(heure_cible_dict["mm"]) - r
        r = 0
        if min < 0:
            min += 60
            r += 1
        hou = int(heure_now_dict["hh"]) - int(heure_cible_dict["hh"]) - r
        r = 0
        if hou < 0:
            hou += 24
            r += 1
        day = int(date_now_dict["jj"]) - int(date_cible_dict["jj"]) - r
        r = 0
        if day < 0:
            day += 30
            r += 1
        month = int(date_now_dict["mm"]) - int(date_cible_dict["mm"]) - r
        r = 0
        if month < 0:
            month += 12
            r += 1
        year = int(date_now_dict["aaaa"]) - int(date_cible_dict["aaaa"]) - r
        temps = {"aaaa": year, "mm": month, "jj": day, "h": hou, "min": min, "s": sec}
        # print(temps)
        a += 1

    fmt = input(Fore.LIGHTCYAN_EX + "Unité de sortie [j] / [h] / [all] : " + Fore.RESET)
    print("" + Style.RESET_ALL)
    print(Back.GREEN + "")
    print("" + Style.RESET_ALL)
    if a == 0:
        print(Fore.CYAN + " Dans : ")
    elif a == 1:
        print(Fore.WHITE + " Il y a : ")
    if fmt == "a" or fmt == "all":
        print(temps["aaaa"], "année(s)")
        print(temps["mm"], "mois")
        print(temps["jj"], "jour(s)")
        print("")
        print(temps["h"], "heure(s)")
        print(temps["min"], "minute(s)")
        print(temps["s"], "seconde(s)")
    elif fmt == "j":
        day += 365.25*year + 30.44*month + hou/24 + min/(60*24)
        print(day, " jour(s)")
    elif fmt == "h":
        hou += min/60 + day*24 + month*24*30.44 + year*24*30.44*12
        print(hou, " heure(s)")
    else:
        print(temps)
    print("" + Style.RESET_ALL)
    print(Back.GREEN + "")
    print("" + Style.RESET_ALL)
    main()


def multiplication_table():
    serie = int(input(Fore.LIGHTCYAN_EX + "Nombre de series : " + Fore.RESET))
    score = 0
    temps_deb = time()
    for i in range(serie):
        a = randint(0, 10)
        b = randint(0, 10)
        rep = int(input(str(a)+"*"+str(b)+" = "))
        if rep == a*b:
            score += 1
        else:
            print(Fore.RED + "FAUX ! ", a, "*", b, " = ", a*b, "" + Style.RESET_ALL)
    temps_fin = time()
    temps = temps_fin - temps_deb
    if score == serie:
        print(Fore.GREEN + "BRAVO ! Tu as complété la série sans erreur !" + Fore.RESET)
    else:
        print(Fore.RED + "Dommage, tu as", score, "/", serie, ", tu feras mieux la prochaine fois :/" + Fore.RESET)
    if temps/(serie*2) <= 1:
        print(Fore.GREEN + "En ", int(temps), " secondes ! (temps de réponse < 2s")
        print("Bien joué ;)" + Fore.RESET)
    else:
        print(Fore.RED + "En ", int(temps), " secondes... (un peu lent)" + Fore.RESET)
    print(Style.RESET_ALL + "")
    main()


# __main__
def main():
    print(Fore.BLUE + "Quel fonctionnalité voulez-vous utiliser ?" + Fore.RESET)
    print(Fore.YELLOW + "ipcalc : calculatrice d'adresses IP" + Fore.RESET)
    print(Fore.YELLOW + "pow2ex : s'entrainer sur les puissances de 2" + Fore.RESET)
    print(Fore.YELLOW + "event : compter le temps qui nous sépare d'un évènement" + Fore.RESET)
    print(Fore.YELLOW + "multiplication_table : un bon exercice pour s'entrainer aux tables de multiplication" + Fore.RESET)
    f = input(Fore.LIGHTCYAN_EX + "[ipcalc] / [pow2ex] / [event] / [multiplication_table] / [exit] : " + Fore.RESET)
    if f == "ipcalc" or f == "i" or f == 1 or f == "[ipcalc]":
        ipcalc()
    elif f == "pow2ex" or f == "p" or f == 2 or f == "[pow2ex]":
        pow2ex()
    elif f == "event" or f == "e" or f == "[event]":
        event()
    elif f == "multiplication_table" or f == "multiplication" or f == "m":
        multiplication_table()
    elif f == "exit":
        print(Fore.YELLOW + "Good bye." + Fore.RESET)
        exit()
    else:
        print("Reformulez votre demande.")
        main()


main()
