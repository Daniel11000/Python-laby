# 3. Dekoratory
#   a. wzbogać klasę Tree o dekorator @property do odczytywania najmniejszej
#       wartości w całym drzewie
#   b. Zaimplementuj funkcję do obliczania kolejnych elementów ciągu
#       Fibonacciego w sposób rekurencyjny, zmierz jej czas działania używając
#       biblioteki timeit, następnie użyj dekoratora @lru_cache, i zmierz czas
#       ponownie
#   c. napisz własny dekorator który zapisze na dysku wynik działania funkcji i przy
#       kolejnym użyciu wczyta go z dysku zamiast obliczać ponownie (mogą to być
#       obliczenia na tabeli z poprzedniego zadania)
#   d. * dodaj argument dekoratora decydujący o formacie zapisu (pickle, csv, excel,
#       …)




import timeit
from functools import lru_cache

# Funkcja obliczająca ciąg Fibonacciego w sposób rekurencyjny
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Pomiar czasu dla obliczania ciągu Fibonacciego w sposób rekurencyjny
time_recursive = timeit.timeit("fibonacci_recursive(30)", globals=globals(), number=1)
print(f"Czas obliczania Fibonacciego rekurencyjnie: {time_recursive} sekundy")

# Dekorator @lru_cache do funkcji obliczającej ciąg Fibonacciego
@lru_cache(maxsize=None)
def fibonacci_cached(n):
    if n <= 1:
        return n
    else:
        return fibonacci_cached(n-1) + fibonacci_cached(n-2)

# Pomiar czasu dla obliczania ciągu Fibonacciego z użyciem cache
time_cached = timeit.timeit("fibonacci_cached(30)", globals=globals(), number=1)
print(f"Czas obliczania Fibonacciego z użyciem cache: {time_cached} sekundy")




