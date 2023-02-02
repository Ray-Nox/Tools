"""
Autor : Ray-Nox
Date (create) : ??/11/2022
Date (laste update) : 10/12/2022
Utilities : From your requirements, 
  the python script will generate a script written in SQL*Plus (for databases).
  The script requires a lot of precision and is only suitable for 
  those who have a precise plan of their table(s) to be created 
  in SQL*Plus and who do not know the SQL*Plus syntax or are lazy to write a script.
Requirement : colorama (or delete all lines using colorama)
"""
from colorama import init, Fore, Back, Style

global file
global name
init()


def ecrire(phrase):
    global file
    fichier = open(file, "a")
    fichier.write("\n" + phrase)
    fichier.close()


def keys():
    global name
    phrase = ""
    cle = input(Fore.LIGHTYELLOW_EX + "primary or foreign key [p] OR [f] : " + Style.RESET_ALL)
    if str(cle) == "p":
        phrase = "\tconstraint pk_" + name + " primary key (" + str(input(Fore.YELLOW + "clé primaire : "
                                                                          + Style.RESET_ALL)) + ")"
    elif str(cle) == "f":
        fk = str(input(Fore.MAGENTA + "clé étrangère : " + Style.RESET_ALL))
        table_ref = str(input(Fore.MAGENTA + "table de référence : " + Style.RESET_ALL))
        pk_ref = str(input(Fore.YELLOW + "clé primaire de référence : " + Style.RESET_ALL))
        phrase = "\tconstraint fk_" + name + " foreign key (" + fk + ") references " + table_ref + " (" + pk_ref + ")"
    else:
        print(Fore.RED + "[p] pour 'primary' | [f] pour 'foreign'..." + Style.RESET_ALL)
        keys()
    return phrase


def new_table():
    global file
    global name
    if not "file" in globals():
        print(Fore.RED + "Pas de fichier ciblé..." + Style.RESET_ALL)
        main()
    types = ["number", "varchar2", "date"]
    name = input(Fore.LIGHTGREEN_EX + "nom de la table    : " + Style.RESET_ALL)
    columns = int(input(Fore.LIGHTBLUE_EX + "nombre de colonnes : " + Style.RESET_ALL))
    name_column = []
    for i in range(columns):
        val_col = "colonne" + str(i) + " : "
        name_column.append(input(val_col))
    # print(name_column)
    type_column = []
    print("types : ", types)
    print(Fore.YELLOW + "            [0]  ,      [1]   ,  [2]" + Style.RESET_ALL)
    for i in range(columns):
        typ_int_col = int(input(Fore.LIGHTBLUE_EX + "type_colonne " + str(name_column[i]) + " : " + Style.RESET_ALL))
        typ_col = types[typ_int_col]
        if typ_int_col == 1:
            typ_col = str(typ_col) + "(" + str(input(Fore.LIGHTMAGENTA_EX + "Nombre de caractères : "
                                                     + Style.RESET_ALL)) + ")"
        type_column.append(typ_col)
    # print(type_column)

    phrase = "CREATE TABLE " + name + "("
    ecrire(phrase)
    for i in range(columns + 1):
        if i == columns:
            nb_cle = int(input(Fore.LIGHTYELLOW_EX + "nb_clé : " + Style.RESET_ALL))
            for j in range(nb_cle):
                if j == nb_cle - 1:
                    phrase = str(keys())
                else:
                    phrase = str(keys()) + ","
                ecrire(phrase)
        else:
            if 0 < len(name_column[i]) < 8:
                tab = "\t\t"
            elif 7 < len(name_column[i]) < 16:
                tab = "\t"
            elif 15 < len(name_column[i]) < 24:
                tab = "\t\t\t"
            else:
                tab = "\t\t\t\t"
            phrase = "\t" + name_column[i] + tab + type_column[i] + ","
            ecrire(phrase)
    ecrire(")")
    ecrire("/")
    ecrire("COMMIT;")
    ecrire("")
    ecrire("")
    print("")
    main()


def new_line():
    global file
    if not "file" in globals():
        print(Fore.RED + "Pas de fichier ciblé..." + Style.RESET_ALL)
        main()
    table = input(Fore.LIGHTGREEN_EX + "nom de la table : " + Style.RESET_ALL)
    nb_col = int(input(Fore.LIGHTBLUE_EX + "nombre de colonnes [<class int>] : " + Style.RESET_ALL))
    col_lst = []
    col_value = []
    for i in range(nb_col):
        col_lst.append(input(Fore.LIGHTGREEN_EX + "nom colonne " + str(i) + " : " + Style.RESET_ALL))
        col_value.append(input(Fore.LIGHTMAGENTA_EX + "valeur (penser aux '') : " + Style.RESET_ALL))
    phrase = "INSERT INTO " + str(table) + " (" + str(', '.join(col_lst)) + ")"
    ecrire(phrase)
    phrase = "VALUES (" + str(', '.join(col_value)) + ")"
    ecrire(phrase)
    ecrire("/")
    ecrire("COMMIT;")
    ecrire("")
    ecrire("")
    main()


def new_sequence():
    global file
    if not "file" in globals():
        print(Fore.RED + "Pas de fichier ciblé..." + Style.RESET_ALL)
        main()
    seq_name = input(Fore.GREEN + "Nom de la séquence : " + Style.RESET_ALL)
    val_min = int(input(Fore.LIGHTBLUE_EX + "Veleur min : " + Style.RESET_ALL))
    val_max = int(input(Fore.LIGHTBLUE_EX + "Valeur max ( [0] -> pas de max ) : " + Style.RESET_ALL))
    increment = int(input(Fore.LIGHTCYAN_EX + "Incrementation : " + Style.RESET_ALL))

    ecrire("CREATE SEQUENCE " + str(seq_name))
    ecrire("START WITH " + str(val_min))
    ecrire("INCREMENT BY " + str(increment))
    if val_max == 0:
        ecrire("NOMAXVALUE")
    else:
        pass
    ecrire("CACHE 10")
    ecrire(";")
    ecrire("COMMIT;")
    ecrire("")
    main()


def new_view():
    global file
    if not "file" in globals():
        print(Fore.RED + "Pas de fichier ciblé..." + Style.RESET_ALL)
        main()
    view_name = input(Fore.GREEN + "Nom de la vue : " + Style.RESET_ALL)
    content = []
    a = True
    while a:
        content.append(input(Fore.GREEN + ">>> " + Style.RESET_ALL))
        if str(content[-1])[-1] == ";":
            a = False
    ecrire("CREATE OR REPLACE VIEW " + view_name)
    for i in range(len(content)):
        ecrire(content[i])
    ecrire("COMMIT;")
    ecrire("")
    main()


def main():
    global file
    f = input(
        Fore.LIGHTCYAN_EX + "[file] | [new_table] | [new_line] | [new_sequence] | [new_view] | [exit] : "
        + Style.RESET_ALL)
    if f == "file":
        file = str(input(Fore.LIGHTWHITE_EX + Back.RED + "fichier : " + Style.RESET_ALL))
        main()
    elif f == "new_table" or f == "t":
        new_table()
    elif f == "new_line" or f == "l":
        new_line()
    elif f == "new_sequence" or f == "s":
        new_sequence()
    elif f == "new_view" or f == "v":
        new_view()
    elif f == "exit" or f == "e":
        exit()
    else:
        main()


main()
