import os

def wypisz_pliki_w_katalogu(sciezka):

    #print(os.listdir(sciezka))
    for sciezka_katalogu, podkatalogi, pliki in os.walk(sciezka):
                #for plik in pliki:
                    #sciezka_pelna = os.path.join(sciezka_katalogu,plik)
                    # print(sciezka_pelna)
                print(sciezka_katalogu, "\t\t", os.listdir(sciezka_katalogu))


sciezka = input("\nWprowaz sciezke: ")
# sciezka = r'C:\Student\JSWH\LAB1\test'

wypisz_pliki_w_katalogu(sciezka)
