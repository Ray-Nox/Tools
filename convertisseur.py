"""
Autor : Ray-Nox
Date (create) : ??/02/2022
Date (last update) : 02/02/2023
Utilities : Convert a base number 2, 10, 16 on another base number (2, 10, 16)
"""


# convert binary to decimal
def bin2dec():
    lst_bin = list(input("Enter a binary number: "))
    nb_bin = []
    nb_dec = 0

    for i in range(len(lst_bin)):
        nb_bin.append(int(lst_bin.pop(0)))

    for i in range(len(nb_bin)):
        nb_dec += nb_bin[i] * 2 ** (len(nb_bin) - 1 - i)

    print(nb_dec)
    main()
    # return nb_dec


# convert decimal to binary
def dec2bin():
    nb_dec = int(input("Enter a decimal number: "))
    lst_bin = []
    # find the 2^n
    n = 0
    while 2 ** n < nb_dec:
        n += 1
    # build the list lst_bin
    for i in range(n + 1):
        if 2 ** (n - i) <= nb_dec:
            lst_bin.append(1)
            nb_dec -= 2 ** (n - i)
        else:
            lst_bin.append(0)
    # convert lst_bin to nb_bin
    nb_bin = int(''.join(str(elt) for elt in lst_bin))

    print(nb_bin)
    main()
    # return nb_bin


# convert decimal to hexadecimal
def dec2hex():
    nb_dec = int(input("Enter a decimal number: "))
    lst_hex = []
    hexa = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    # find the n rank for 16^n > nb_dec
    n = 0
    while 16 ** n < nb_dec:
        n += 1
    for i in range(n + 1):
        m = nb_dec // (16 ** (n - i))
        nb_dec -= m * (16 ** (n - i))
        lst_hex.append(m)
    for i in range(len(lst_hex)):
        lst_hex[i] = hexa[lst_hex[i]]
    nb_hex = "".join(lst_hex)

    print(nb_hex)
    main()
    # return nb_hex


# convert hexadecimal to decimal
def hex2dec():
    nb_hex = str(input("Enter an hexadecimal number: "))
    nb_hex = nb_hex.upper()
    dico_dec = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11,
                "D": 13, "C": 12, "E": 14, "F": 15}
    nb_dec = 0
    lst_hex = []
    for i in range(len(nb_hex)):
        lst_hex.append(nb_hex[i])
    for i in range(len(lst_hex)):
        nb_dec += dico_dec[lst_hex[i]] * 16 ** (len(lst_hex) - i - 1)
    print(nb_dec)
    main()


# convert binary to hexadecimal
def bin2hex():
    lst_bin = list(input("Enter a binary number: "))
    nb_bin = []
    nb_dec = 0

    for i in range(len(lst_bin)):
        nb_bin.append(int(lst_bin.pop(0)))

    for i in range(len(nb_bin)):
        nb_dec += nb_bin[i] * 2 ** (len(nb_bin) - 1 - i)

    lst_hex = []
    hexa = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    # find the n rank for 16^n > nb_dec
    n = 0
    while 16 ** n < nb_dec:
        n += 1
    for i in range(n + 1):
        m = nb_dec // (16 ** (n - i))
        nb_dec -= m * (16 ** (n - i))
        lst_hex.append(m)
    for i in range(len(lst_hex)):
        lst_hex[i] = hexa[lst_hex[i]]
    nb_hex = "".join(lst_hex)

    print(nb_hex)
    main()
    # return nb_hex


# convert hexadecimal to binary
def hex2bin():
    nb_hex = str(input("Enter an hexadecimal number: "))
    nb_hex = nb_hex.upper()
    dico_dec = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11,
                "D": 13, "C": 12, "E": 14, "F": 15}
    nb_dec = 0
    lst_hex = []
    for i in range(len(nb_hex)):
        lst_hex.append(nb_hex[i])
    for i in range(len(lst_hex)):
        nb_dec += dico_dec[lst_hex[i]] * 16 ** (len(lst_hex) - i - 1)

    lst_bin = []
    # find the 2^n
    n = 0
    while 2 ** n < nb_dec:
        n += 1
    # build the list lst_bin
    for i in range(n + 1):
        if 2 ** (n - i) <= nb_dec:
            lst_bin.append(1)
            nb_dec -= 2 ** (n - i)
        else:
            lst_bin.append(0)
    # convert lst_bin to nb_bin
    nb_bin = int(''.join(str(elt) for elt in lst_bin))

    print(nb_bin)
    main()
    # return nb_bin


def main():
    f = input("[bin2dec] | [bin2hex] | [dec2bin] | [dec2hex] | [hex2bin] | [hex2dec] : ")
    if f == "bin2dec":
        bin2dec()
    elif f == "dec2bin":
        dec2bin()
    elif f == "dec2hex":
        dec2hex()
    elif f == "hex2dec":
        hex2dec()
    elif f == "bin2hex":
        bin2hex()
    elif f == "hex2bin":
        hex2bin()
    elif f == "exit" or f == "e":
        exit()
    else:
        main()


main()
