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




# import json
import os
import inspect

def cache_result(filename):
    def decorator(func):
        def wrapped(*args, **kwargs):
            arguments = inspect.getcallargs(func, *args, **kwargs)
            # Sprawdzamy, czy plik z wynikiem istnieje
            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    # result = json.load(file)
                    #result = file.read()
                    napis = str(arguments) + '\n'
                    z_pliku = file.readline()
                    if(napis == z_pliku): # jeśli argumenty funkcji są takie same jak te z pliku
                        result = file.read()
                        #result = file.readline()
                    else:
                        result = func(*args, **kwargs)
                        with open(filename, 'w') as file:
                            file.write(str(arguments))
                            file.write('\n')
                            file.write(result)
                # if not result:  # Jeśli plik jest pusty
                #     result = func(*args, **kwargs)
                #     with open(filename, 'w') as file:
                #         file.write(result)
            else:
                # Jeśli plik nie istnieje, obliczamy wynik funkcji i zapisujemy go
                result = func(*args, **kwargs)
                with open(filename, 'w') as file:
                    # json.dump(result, file)
                    #file.write(str((args, kwargs)))
                    #file.write(str((kwargs)))
                    file.write(str(arguments))
                    file.write('\n')
                    file.write(result)
            return result
        return wrapped
    return decorator



# Dekorator cache_result zapisuje i odczytuje wynik z pliku 'cached_result.pkl'
@cache_result('result.txt')
def fibonacci(n):
    if n <= 1:
        # return n
        return str(n)
    else:
        # return fibonacci(n-1) + fibonacci(n-2)
        return str(int(fibonacci(n - 1)) + int(fibonacci(n - 2)))

# Wywołanie funkcji fibonacci
result = fibonacci(10)
print("Wynik obliczeń:", result)

# Ponowne wywołanie funkcji fibonacci
result = fibonacci(10)
print("Wynik wczytany z cache:", result)

# result = fibonacci(12)
# print("Wynik: ", result)






