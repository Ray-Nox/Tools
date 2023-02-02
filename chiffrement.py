"""
Autor : Ray-Nox
Date (create) : ??/10/2022
Date (last version) : 02/02/2023
from random import randint

''' 
--> Help for me so maybe for u too ;)

--- 2 fonctions utiles ---
>>> ord("a")
97
>>> chr(97)
'a'
'''


# 1 Ecrire une fonction  qui va convertir une variable  de type unsigned char en variable de type string
def cesar(mot, cle):  # cesar encoding
    mot_chiffre = ""
    mode = int(input("alphabet lowercase (1) or all Unicode table (2) : "))
    for i in range(len(mot)):  # parcours les caracteres du mot a chiffrer
        l = ord(mot[i])  # recupere le code ASCII du caractere
        if mode == 1:  # only lowercase alphabet
            cle = cle % 26
            if l == 32:  # si c'est un espace, on le garde
                pass
            else:
                l += cle  # modifie le code ascii selon la cle
                if l > 122:  # si on depasse z (=122 en ASCII), on revient a a (=97)
                    l -= 26
                if l < 97:  # si on depasse a, on remonte a z
                    l += 26
        elif mode == 2:  # all ASCII table
            l += cle
        a = chr(l)  # on reconvertit le code ASCII en caractere
        mot_chiffre += a  # on ajoute le nouveau caractere obtenu dans la liste

    return str(mot_chiffre)  # affiche le mot chiffre sous forme de chaine de caracteres


def substitution(mot, alphabet_de_chiffrement): # substitution encoding
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    mot_chiffre = ""
    for i in range(len(mot)):
        lettre_chiffree = alphabet_de_chiffrement[alphabet.index(mot[i])]  # la lettre chiffree correspond a la lettre dans le nouvel alphabet d indice egal a l index de la lettre de base dans l alphabet
        mot_chiffre += lettre_chiffree
    return mot_chiffre


def vigenere(mot, mot_cle): # vigenere encoding
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    mot_chiffre = ""
    phrase_clee = mot_cle * (len(mot) // (len(mot_cle)) + 1)  # fait en sorte que la phrase clee soit plus longue que la phrase a chiffrer
    for i in range(len(mot)):
        if mot[i] == ' ':  # quand on croise un espace, rajouter un espace dans le chiffrement
            mot_chiffre += ' '
        else:
            lettre_chiffree = alphabet[(alphabet.index(mot[i]) + alphabet.index(phrase_clee[i])) % 26]  # on prend dans l alphabet l indice egal a la somme de l indice du mot et de l indice du mot cle, le tout modulo 26 pour rester dans l alphabet
            mot_chiffre += lettre_chiffree
    return mot_chiffre


''' - aide pour le mot cle de vigenere - 
a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z  <-- si on rentre ca en cle pour chiffrer
a | z | y | x | w | v | u | t | s | r | q | p | o | n | m | l | k | j | i | h | g | f | e | d | c | b  <-- il faudra ca en cle pour dechiffrer
'''


def asymetrique(message, cle):
    print("Nothing for this time")
    return message


def rand_alphabet():  # generate a random alphabet
    alphabet_orig = list("abcdefghijklmnopqrstuvwxyz")
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    rand_alpha = []
    for i in range(len(alphabet_orig)):
        rand_alpha.append(alphabet.pop(randint(0, len(alphabet) - 1)))
    return rand_alpha
