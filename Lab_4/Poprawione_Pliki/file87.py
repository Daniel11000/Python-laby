# b = 0     # Niepotrzebne
# c = 0     # Niepotrzebne


class pi_container:
    # def __init__(self, a=list()):  # Unikanie domyślnej wartości listy jako argumentu domyślnego
    def __init__(self, a=None):
        # self.a = a    # brak przypisania gdy a nie istnieje
        self.a = a if a is not None else []

    def mth(self, x):
        if type(x) == list:
            self.a += x
        else:
            self.a.append(x)


def foo(x):
    # global b  # Nie powinno się używać zmiennycg globalnych
    # global c  # Nie powinno się używać zmiennycg globalnych
    b = 0
    #c=1   # dla czytelności
    c = 1
    for hello in range(x):
        if hello % 2 == 0:
            #b += 4 / c#this is a very important operation in calculateing pi according to documentation that is provided in a seperate file in this repository, please analyse this file before using!
            b += 4 / c  # this is a very important operation in calculateing pi according to documentation
            # that is provided in a seperate file in this repository, please analyse this file before using!
        else:
            b -= 4 / c
        c += 2
        yield b
    yield 'finished'

# def enumerate(pi: pi_container):  # Unikanie konfliktu nazw z wbudowaną funkcją enumerate
def enumerate_pi(pi):
    for hello in pi.a:
        print(hello)


print('All functions are defined')
