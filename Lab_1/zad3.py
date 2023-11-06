from typing import List
import re

def usun_slowa_z_tekstu(tekst_p, slowa_p):

    f_tx = open(tekst_p, "r")
    zawartosc_tekst = f_tx.read()
    f_tx.close()

    f_slowa = open(slowa_p, "r")
    zawartosc_slowa = f_slowa.read()
    #f_slowa.close()
    #zawartosc_slowa = [l.split(',') for l in zawartosc_slowa]  # 2 podziel po wierszach
    zawartosc_slowa = zawartosc_slowa.split(", ")
    #zawartosc_slowa = [l.split(',') for l in zawartosc_slowa]  # 2 podziel po wierszach
    slowa: List[str] = zawartosc_slowa
    #print("\n", zawartosc_slowa, "\n")
    #print("\n", slowa, "\n")

    print("\n", "\t \tOryginalny Tekst: \n \n",  zawartosc_tekst, "\n \n \n", "\t \tPrzerobiony tekst:")


    for word in slowa:
        zawartosc_tekst = re.sub(word, '', zawartosc_tekst)
    print("\n", zawartosc_tekst, "\n")
    return zawartosc_tekst


sciezka_tekst = "zad3_tekst.txt"
sciezka_slowa = "zad3_slowa.txt"
usun_slowa_z_tekstu(sciezka_tekst, sciezka_slowa)
