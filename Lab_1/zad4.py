from typing import List
import re

def zamien_slowa_z_tekstu(tekst_p, slowa_p):

    f_tx = open(tekst_p, "r")
    zawartosc_tekst = f_tx.read()
    f_tx.close()

    f_slowa = open(slowa_p, "r")
    zawartosc_slowa = f_slowa.read()
    #f_slowa.close()
    #zawartosc_slowa = [l.split(',') for l in zawartosc_slowa]  # 2 podziel po wierszach
    zawartosc_slowa = zawartosc_slowa.split("\n")
    #zawartosc_slowa = zawartosc_slowa.split(", ")
    zawartosc_slowa = [l.split(',') for l in zawartosc_slowa]  # 2 podziel po wierszach
    slowa: List[str] = zawartosc_slowa
    #print("\n", zawartosc_slowa, "\n")
    #print("\n", slowa, "\n")
    #print("\n", slowa[0][1], "\n")


#'''
    print("\n", "\t \tOryginalny Tekst: \n \n",  zawartosc_tekst, "\n \n \n", "\t \tPrzerobiony tekst:")

    '''
    for word in slowa:
        zawartosc_tekst = re.sub(word, slowa[word], zawartosc_tekst)
    '''

    for i in range(len(slowa)):
        for word in slowa[i]:
            zawartosc_tekst = re.sub(word, slowa[i][1], zawartosc_tekst)

    print("\n", zawartosc_tekst, "\n")
    return zawartosc_tekst
#'''

sciezka_tekst = "zad3_tekst.txt"
sciezka_slowa = "zad4_slowa.txt"
zamien_slowa_z_tekstu(sciezka_tekst, sciezka_slowa)
