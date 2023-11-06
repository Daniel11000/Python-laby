from typing import List
import re

#def usun_zlowa_z_tekstu(tekst_p, slowa_p):\


def usun_zlowa_z_tekstu(tekst_p):
    f = open(tekst_p, "r")
    zawartosc = f.read()
    f.close
    print("\n",zawartosc, "\n")

#sciezka = "C:\Student\Arturro_Michal\lab1_zadania\zad3_tekst.txt"
sciezka = "zad3_tekst.txt"
usun_zlowa_z_tekstu(sciezka)

