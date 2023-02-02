from turtle import *
from time import *
from math import sqrt


# ////////// Fonctions //////////
def rails():
    nbl = len(let)
    down()
    right(180)
    fd(nbl * taille)
    up()
    right(90)
    fd(taille)
    right(90)
    down()
    fd(nbl * taille)


# ////////// MAJUSCULES //////////
def A():
    down()
    setheading(0)
    left(75)
    forward(taille)
    right(150)
    forward(taille)
    backward(taille / 2)
    right(105)
    forward(taille / 4)
    bk(taille / 4)
    left(105)
    fd(taille / 2)
    up()
    setheading(0)
    fd(taille / 10)


def B():
    down()
    setheading(0)
    circle(taille / 4, 180)
    right(180)
    circle(taille / 4, 180)
    left(90)
    fd(taille)
    up()
    left(90)
    fd(taille / 4)
    fd(ecart)


def C():
    setheading(0)
    fd(taille / 2)
    left(90)
    fd(taille)
    right(90)
    down()
    right(180)
    circle(taille / 2, 180)
    up()
    fd(ecart)


def D():
    setheading(0)
    down()
    circle(taille / 2, 180)
    left(90)
    fd(taille)
    left(90)
    up()
    fd(taille / 2)
    fd(ecart)


def E():
    down()
    setheading(0)
    left(90)
    fd(taille)
    right(90)
    fd(taille / 2)
    up()
    right(90)
    fd(taille / 2)
    right(90)
    fd(taille / 6)
    down()
    fd(taille / 3)
    left(90)
    fd(taille / 2)
    left(90)
    fd(taille / 2)
    up()
    fd(ecart)


def F():
    setheading(0)
    left(90)
    down()
    fd(taille)
    right(90)
    fd(taille / 2)
    bk(taille / 2)
    left(90)
    bk(taille / 2)
    right(90)
    fd(taille / 3)
    up()
    bk(taille / 3)
    right(90)
    fd(taille / 2)
    left(90)
    fd(taille / 2)
    fd(ecart)


def G():
    setheading(0)
    fd(taille / 2)
    down()
    circle(taille / 2, -180)
    up()
    left(90)
    fd(taille)
    down()
    bk(taille / 4)
    left(90)
    bk(taille / 6)
    fd(2 * taille / 6)
    up()
    right(90)
    fd(taille / 4)
    left(90)
    fd(ecart)


def H():
    setheading(0)
    down()
    left(90)
    fd(taille)
    bk(taille / 2)
    right(90)
    fd(taille / 3)
    left(90)
    fd(taille / 2)
    bk(taille)
    right(90)
    up()
    fd(ecart)


def I():
    setheading(0)
    fd(taille / 3)
    down()
    left(90)
    fd(taille)
    right(90)
    fd(taille / 3)
    bk(2 * taille / 3)
    up()
    right(90)
    fd(taille)
    down()
    left(90)
    fd(2 * taille / 3)
    up()
    fd(ecart)


def J():
    setheading(0)
    left(90)
    fd(taille / 3)
    down()
    right(180)
    circle(taille / 3, 180)
    fd(taille * 2 / 3)
    right(90)
    fd(taille / 3)
    bk(taille * 2 / 3)
    up()
    fd(taille * 2 / 3 + ecart)
    right(90)
    fd(taille)
    left(90)


def K():
    setheading(0)
    down()
    left(90)
    fd(taille)
    bk(taille / 2)
    right(30)
    fd(taille * 1.15 / 2)
    bk(taille * 1.15 / 2)
    right(120)
    fd(taille * 1.15 / 2)
    up()
    left(60)
    fd(ecart)


def L():
    setheading(0)
    down()
    left(90)
    fd(taille)
    bk(taille)
    right(90)
    fd(taille / 3)
    up()
    fd(ecart)


def M():
    setheading(0)
    down()
    left(90)
    fd(taille)
    right(150)
    fd(taille / 2)
    left(120)
    fd(taille / 2)
    right(150)
    fd(taille)
    up()
    left(90)
    fd(ecart)


def N():
    setheading(0)
    down()
    left(90)
    fd(taille)
    right(150)
    fd(1.15 * taille)
    left(150)
    fd(taille)
    up()
    bk(taille)
    right(90)
    fd(ecart)


def O():
    setheading(0)
    fd(taille / 2)
    down()
    circle(taille / 2)
    up()
    fd(taille / 2)
    fd(ecart)


def P():
    setheading(0)
    down()
    left(90)
    fd(taille)
    left(90)
    circle(taille / 3, -180)
    up()
    right(90)
    fd(taille / 3)
    left(90)
    fd(taille / 4)
    fd(2 * ecart)


def Q():
    setheading(0)
    fd(taille / 2)
    down()
    circle(taille / 2)
    up()
    left(90)
    fd(taille / 2)
    right(135)
    fd(taille / 4)
    down()
    fd(taille / 2)
    up()
    left(45)
    fd(ecart)


def R():
    setheading(0)
    down()
    left(90)
    fd(taille)
    left(90)
    circle(taille / 3, -180)
    right(45)
    fd(1.05 * taille / 2)
    up()
    left(45)
    fd(ecart)


def S():
    setheading(0)
    left(90)
    fd(taille / 3)
    down()
    right(180)
    circle(taille / 3, 180)
    left(60)
    fd(0.7 * taille)
    right(240)
    circle(taille / 3, -180)
    up()
    right(180)
    fd(taille - taille / 3)
    left(90)
    fd(ecart)


def T():
    setheading(0)
    fd(taille / 3)
    left(90)
    down()
    fd(taille)
    right(90)
    bk(taille / 3)
    fd(taille * 2 / 3)
    up()
    right(90)
    fd(taille)
    left(90)
    fd(ecart)


def U():
    setheading(0)
    left(90)
    fd(taille)
    right(180)
    down()
    fd(taille * 2 / 3)
    circle(taille / 3, 180)
    fd(taille * 2 / 3)
    up()
    bk(taille)
    right(90)
    fd(ecart)


def V():
    setheading(0)
    left(90)
    fd(taille)
    right(165)
    down()
    fd(1.04 * taille)
    left(150)
    fd(1.04 * taille)
    right(165)
    up()
    fd(taille)
    left(90)
    fd(ecart)


def W():
    setheading(0)
    left(90)
    fd(taille)
    right(165)
    down()
    fd(1.04 * taille)
    left(150)
    fd(1.04 * taille / 2)
    right(150)
    fd(1.04 * taille / 2)
    left(150)
    fd(1.04 * taille)
    right(165)
    up()
    fd(taille)
    left(90)
    fd(ecart)


def X():
    setheading(0)
    left(60)
    down()
    fd(sqrt((taille / 3) ** 2 + (taille) ** 2))
    up()
    left(120)
    fd(taille / 2)
    left(120)
    down()
    fd(sqrt((taille / 3) ** 2 + (taille) ** 2))
    up()
    left(60)
    fd(ecart)


def Y():
    setheading(0)
    left(90)
    fd(taille)
    right(150)
    down()
    fd(taille / 2)
    right(30)
    fd(taille / 2)
    right(180)
    fd(taille / 2)
    right(30)
    fd(taille / 2)
    up()
    right(150)
    fd(taille)
    left(90)
    fd(ecart)


def Z():
    setheading(0)
    left(90)
    fd(taille)
    right(90)
    down()
    fd(taille / 2)
    right(120)
    fd(sqrt((taille) ** 2 + (taille / 2) ** 2))
    left(120)
    fd(taille / 2)
    up()
    fd(ecart)


# MAJUSCULES ------------------------------
# ////////// minuscules //////////
def a():
    setheading(0)
    fd(taille / 2)
    left(90)
    fd(taille / 4)
    down()
    circle(taille / 4)
    fd(taille / 4)
    bk(taille / 2)
    right(90)
    up()
    fd(ecart)


def b():
    setheading(0)
    fd(taille / 2)
    left(90)
    fd(taille / 4)
    down()
    circle(taille / 4)
    up()
    left(90)
    fd(taille / 2)
    right(90)
    down()
    fd(2 * taille / 3)
    bk(2 * taille / 3 + taille / 4)
    right(90)
    up()
    fd(taille / 2)
    fd(ecart)


def c():
    setheading(0)
    fd(taille / 4)
    left(90)
    fd(taille / 2)
    right(90)
    down()
    right(180)
    circle(taille / 4, 180)
    up()
    fd(ecart)


def d():
    setheading(0)
    fd(taille / 2)
    left(90)
    fd(taille / 4)
    down()
    circle(taille / 4)
    fd(2 * taille / 3)
    bk(2 * taille / 3 + taille / 4)
    right(90)
    up()
    fd(ecart)


def e():
    setheading(0)
    fd(taille / 4)
    down()
    circle(taille / 4, -270)
    left(90)
    fd(taille / 2)
    up()
    right(180)
    fd(taille / 4)
    right(90)
    fd(taille / 4)
    left(90)
    down()
    fd(taille / 4)
    up()
    fd(ecart)


def f():
    setheading(0)
    left(90)
    down()
    fd(taille * 2 / 3)
    right(180)
    circle(taille / 3, -90)
    up()
    left(90)
    fd(taille / 2)
    right(90)
    fd(taille / 8)
    down()
    fd(taille / 4)
    up()
    bk(3 * taille / 8)
    left(90)
    fd(taille / 2)
    left(90)
    fd(ecart)


def g():
    setheading(0)
    fd(taille / 2)
    left(90)
    fd(taille / 4)
    down()
    circle(taille / 4)
    fd(taille / 4)
    bk(taille * 3 / 4)
    circle(taille / 6, -200)
    circle(taille / 6, 200)
    fd(taille / 4)
    up()
    right(90)
    fd(ecart)


def h():
    setheading(0)
    left(90)
    down()
    fd(taille)
    bk(taille * 2 / 3)
    right(180)
    circle(taille / 6, -180)
    bk(taille / 3)
    up()
    right(90)
    fd(ecart)


def i():
    setheading(0)
    fd(ecart)
    left(90)
    down()
    fd(taille / 2)
    up()
    fd(taille / 4)
    width(size * 2)
    right(90)
    down()
    circle(taille / 100)
    right(90)
    up()
    fd(taille * 3 / 4)
    left(90)
    width(size)
    fd(2 * ecart)


def j():
    setheading(0)
    fd(taille / 6)
    left(90)
    down()
    fd(taille / 2)
    up()
    fd(taille / 4)
    width(size * 2)
    right(90)
    down()
    circle(taille / 100)
    right(90)
    up()
    fd(taille * 3 / 4)
    width(size)
    down()
    fd(taille / 3)
    right(180)
    circle(taille / 6, -180)
    up()
    circle(taille / 6, 180)
    fd(taille / 3)
    right(90)
    fd(ecart)


def k():
    setheading(0)
    left(90)
    down()
    fd(taille)
    bk(taille * 2 / 3)
    right(30)
    fd(1.15 * taille / 3)
    bk(1.15 * taille / 3)
    right(120)
    fd(1.15 * taille / 3)
    bk(1.15 * taille / 3)
    up()
    right(30)
    fd(taille / 3)
    left(90)
    fd(taille / 3)
    fd(ecart)


def l():
    setheading(0)
    fd(taille / 10)
    left(90)
    fd(taille)
    down()
    left(90)
    fd(taille / 10)
    bk(taille / 10)
    right(90)
    bk(taille - taille / 8)
    right(180)
    circle(taille / 8, 90)
    up()
    fd(ecart)


def m():
    setheading(0)
    left(90)
    down()
    fd(taille / 2 + taille / 10)
    bk(taille / 10)
    right(180)
    circle(taille / 8, -180)
    bk(taille / 2)
    fd(taille / 2)
    right(180)
    circle(taille / 8, -180)
    bk(taille / 2)
    right(90)
    up()
    fd(ecart)


def n():
    setheading(0)
    left(90)
    down()
    fd(taille / 2 + taille / 10)
    bk(taille / 10 + taille / 8)
    right(180)
    circle(taille * 2 / 8, -180)
    bk(taille / 2 - taille / 8)
    right(90)
    up()
    fd(ecart)


def o():
    setheading(0)
    fd(taille / 4)
    down()
    circle(taille / 4)
    up()
    fd(taille / 4)
    fd(ecart)


def p():
    setheading(0)
    fd(taille / 2)
    left(90)
    fd(taille / 4)
    down()
    circle(taille / 4)
    up()
    left(90)
    fd(taille / 2)
    right(90)
    down()
    fd(taille / 4)
    bk(2 * taille / 3 + taille / 4)
    fd(2 * taille / 3 - taille / 4)
    right(90)
    up()
    fd(taille / 2)
    fd(ecart)


def q():
    setheading(0)
    fd(taille / 2)
    left(90)
    fd(taille / 4)
    down()
    circle(taille / 4)
    fd(taille / 4)
    bk(2 * taille / 3 + taille / 4)
    fd(2 * taille / 3 - taille / 4)
    right(90)
    up()
    fd(ecart)


def r():
    setheading(0)
    left(90)
    down()
    fd(taille / 2 + taille / 10)
    bk(taille / 6 + taille / 10)
    right(180)
    circle(taille / 4, -180)
    up()
    right(180)
    fd(taille / 3)
    left(90)
    fd(ecart)


def s():
    setheading(0)
    left(90)
    fd(taille / 4)
    down()
    right(180)
    circle(taille / 4, 180)
    left(60)
    fd(0.58 * taille)
    right(240)
    circle(taille / 4, -180)
    up()
    right(180)
    fd(0.58 * taille)
    left(90)
    fd(ecart)


def t():
    setheading(0)
    left(90)
    fd(taille / 2)
    fd(taille / 5)
    right(90)
    down()
    fd(taille / 3)
    bk(taille / 4)
    left(90)
    fd(taille / 4)
    bk(taille / 2 + taille / 4)
    right(180)
    circle(taille / 5, 90)
    up()
    fd(taille / 12)
    fd(ecart)


def u():
    setheading(0)
    left(90)
    fd(taille / 2)
    right(180)
    down()
    fd(taille / 3)
    circle(taille / 6, 180)
    fd(taille / 3)
    bk(taille / 2)
    up()
    right(90)
    fd(ecart)


def v():
    pass


def w():
    pass


def x():
    pass


def y():
    pass


def z():
    pass


# minuscules ------------------------------
# Fonctions ------------------------------

mode = str(input("mode [auto/manuel] : "))
if mode == "auto" or mode == "a":
    taille = 50
    ecart = 10
    size = 5
    vitesse = 10
    let = list(input("mot : "))
    rail = "OFF"
elif mode == "manuel" or mode == "m":
    taille = int(input("taille de la police : "))
    ecart = int(input("écart entre les lettres : "))
    size = int(input("épaisseur du trai : "))
    vitesse = int(input("vitesse de la tortue : "))
    let = list(input("mot : "))
    rail = str(input("rails ? ON,OFF : [OFF] "))
else:
    print("Erreur : Réponse non prise en compte.")
    exit()
up()
width(size)
speed(vitesse)
for elt in range(len(let)):
    if let[elt] == 'A':
        A()
    if let[elt] == 'B':
        B()
    if let[elt] == 'C':
        C()
    if let[elt] == 'D':
        D()
    if let[elt] == 'E':
        E()
    if let[elt] == 'F':
        F()
    if let[elt] == 'G':
        G()
    if let[elt] == 'H':
        H()
    if let[elt] == 'I':
        I()
    if let[elt] == 'J':
        J()
    if let[elt] == 'K':
        K()
    if let[elt] == 'L':
        L()
    if let[elt] == 'M':
        M()
    if let[elt] == 'N':
        N()
    if let[elt] == 'O':
        O()
    if let[elt] == 'P':
        P()
    if let[elt] == 'Q':
        Q()
    if let[elt] == 'R':
        R()
    if let[elt] == 'S':
        S()
    if let[elt] == 'T':
        T()
    if let[elt] == 'U':
        U()
    if let[elt] == 'V':
        V()
    if let[elt] == 'W':
        W()
    if let[elt] == 'X':
        X()
    if let[elt] == 'Y':
        Y()
    if let[elt] == 'Z':
        Z()

    if let[elt] == 'a':
        a()
    if let[elt] == 'b':
        b()
    if let[elt] == 'c':
        c()
    if let[elt] == 'd':
        d()
    if let[elt] == 'e':
        e()
    if let[elt] == 'f':
        f()
    if let[elt] == 'g':
        g()
    if let[elt] == 'h':
        h()
    if let[elt] == 'i':
        i()
    if let[elt] == 'j':
        j()
    if let[elt] == 'k':
        k()
    if let[elt] == 'l':
        l()
    if let[elt] == 'm':
        m()
    if let[elt] == 'n':
        n()
    if let[elt] == 'o':
        o()
    if let[elt] == 'p':
        p()
    if let[elt] == 'q':
        q()
    if let[elt] == 'r':
        r()
    if let[elt] == 's':
        s()
    if let[elt] == 't':
        t()
    if let[elt] == 'u':
        u()
    if let[elt] == 'v':
        v()
    if let[elt] == 'w':
        w()
    if let[elt] == 'x':
        x()
    if let[elt] == 'y':
        y()
    if let[elt] == 'z':
        z()

if rail == 'ON':
    rails()
else:
    pass

# ////////// remarques //////////
# 2e possibilité pour les minuscules :
#	if l[i]=='a':
#		taille_bk=taille
#		taille=taille/2
#		A()
#		taille=taille_bk
#

# ////////// exit //////////
up()
# alt+F4
# sc=Screen()
# sc.mainloop()

# clique sur la fenêtre
exitonclick()

# attendre
# sleep(10)
