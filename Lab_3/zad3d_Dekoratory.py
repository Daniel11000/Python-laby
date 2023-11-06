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




import json
import pickle
import os
import inspect

def cache_result(filename, type):
    def decorator(func):
        def wrapped(*args, **kwargs):
            arguments = inspect.getcallargs(func, *args, **kwargs)
            # Sprawdzamy, czy plik z wynikiem istnieje
            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    # result = json.load(file)
                    #result = file.read()
                    powt = False
                    if(type == "txt"):
                        napis = str(arguments) + "\n"
                        z_pliku = file.readline()
                        if (napis == z_pliku):
                            powt = True
                        else:
                            powt = False
                    elif(type == "json"):
                        napis = "\"" + str(arguments) #+ "\"" + "\"\\\n\""
                        z_pliku = file.readline()
                        if (z_pliku.startswith(napis)):
                            powt = True
                        else:
                            powt = False
                    #if(napis == z_pliku): # jeśli argumenty funkcji są takie same jak te z pliku
                    if (powt == True):  # jeśli argumenty funkcji są takie same jak te z pliku
                        if(type == 'pickle'):
                            # result = pickle.load(file)
                            with open(filename, 'rb') as file:
                                pickle.load(file)
                            result = pickle.load(open(filename, 'rb'))
                        elif (type == 'txt'):
                            result = file.read()
                        elif (type == 'json'):
                            result = json.load(file)
                            #result = file.readline()
                    else:
                        result = func(*args, **kwargs)
                        nap = str(arguments)
                        if (type == "pickle"):
                            with open(filename, 'wb') as file:
                                if (type == 'pickle'):
                                    pickle.dump(nap, file)
                                    pickle.dump('\n', file)
                                    pickle.dump(result, file)
                        else:
                            with open(filename, 'w') as file:
                                if (type == 'txt'):
                                    file.write(str(arguments))
                                    file.write('\n')
                                    file.write(result)
                                elif (type == 'json'):
                                    json.dump(str(arguments), file)
                                    json.dump('\n', file)
                                    json.dump(result, file)
                                    # json.dump({"arguments": str(arguments), "result": result}, file)  # Przekształcenie do formatu JSON

                # if not result:  # Jeśli plik jest pusty
                #     result = func(*args, **kwargs)
                #     with open(filename, 'w') as file:
                #         file.write(result)
            else:
                # Jeśli plik nie istnieje, obliczamy wynik funkcji i zapisujemy go
                result = func(*args, **kwargs)
                with open(filename, 'w') as file:
                    if (type == 'pickle'):
                        pickle.dump(str(arguments), file)
                        pickle.dump('\n', file)
                        pickle.dump(result, file)
                    elif (type == 'txt'):
                        file.write(str(arguments))
                        file.write('\n')
                        file.write(result)
                    elif (type == 'json'):
                        json.dump(str(arguments), file)
                        json.dump('\n', file)
                        json.dump(result, file)
            return result
        return wrapped
    return decorator



# Dekorator cache_result zapisuje i odczytuje wynik z pliku 'cached_result.pkl'
@cache_result('res.txt', "txt")
def fibonacci_txt(n):
    if n <= 1:
        # return n
        return str(n)
    else:
        # return fibonacci(n-1) + fibonacci(n-2)
        return str(int(fibonacci_txt(n - 1)) + int(fibonacci_txt(n - 2)))


@cache_result('res.pkl', "pickle")
def fibonacci_pickle(n):
    if n <= 1:
        return n
    else:
        return fibonacci_pickle(n-1) + fibonacci_pickle(n-2)


@cache_result('res.json', "json")
def fibonacci_json(n):
    if n <= 1:
        return n
    else:
        return fibonacci_json(n-1) + fibonacci_json(n-2)


# Wywołanie funkcji fibonacci
result = fibonacci_txt(10)
print("Wynik obliczeń:", result)

# Ponowne wywołanie funkcji fibonacci
result = fibonacci_json(10)
print("Wynik wczytany z cache:", result)

# result = fibonacci(12)
# print("Wynik: ", result)






