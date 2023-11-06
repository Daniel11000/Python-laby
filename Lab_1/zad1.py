import os

def zlicz_ilosc_plikow(sciezka_do_katalogu):

    lp = 0
    lk = 0
    print (os.listdir(sciezka_do_katalogu))
    for element in os.listdir(sciezka_do_katalogu):
        sciezka_elementu = os.path.join(sciezka_do_katalogu, element)
        if os.path.isfile(sciezka_elementu):
            lp += 1
        else:
            lk += 1
    return lp, lk

sciezka = input("\nWprowaz sciezke: ")

#sciezka = r'C:\Student\JSWH\LAB1\test'

lp, lk = zlicz_ilosc_plikow(sciezka)



print(f'\nIlosc plikow w katalogu  \"{sciezka}\":   {lp}')
print(f'\nIlosc folderow w katalogu  \"{sciezka}\":   {lk}')