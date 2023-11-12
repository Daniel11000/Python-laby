# def enumerate(pi):        # Po co pisać tą funkcję, jak można ją zaimportować
#     for hello in pi.a:    # poza tym konfliktu nazw z wbudowaną funkcją enumerate
#         print(f'Next element: {hello}')

# from file87 import *
from file87 import pi_container, foo, enumerate_pi  # Poprawienie importów
my_pi = pi_container()  # te 3 powinny być przed blokiem try
pi_gen = foo(5)
my_pi_2 = pi_container()
try:
    # my_pi = pi_container()
    # pi_gen = foo(5)
    # my_pi.mth(pi_gen.__next__())
    # my_pi.mth(pi_gen.__next__())
    # my_pi.mth(pi_gen.__next__())
    # my_pi.mth(pi_gen.__next__())
    my_pi.mth(next(pi_gen))  # Użycie next zamiast __next__
    my_pi.mth(next(pi_gen))
    my_pi.mth(next(pi_gen))
    my_pi.mth(next(pi_gen))
    # my_pi_2 = pi_container()
    # my_pi.mth(pi_gen.__next__())
    # my_pi.mth(pi_gen.__next__())
    # my_pi.mth(pi_gen.__next__())
    my_pi.mth(next(pi_gen))
    my_pi.mth(next(pi_gen))
    my_pi.mth(next(pi_gen))
# except:
#     print('something went horribly wrong :(')
except Exception as e:  # Użycie ogólnego wyjątku i przechwytywanie informacji o błędzie
    print(f'Something went horribly wrong: {e}')

# pIgEn3 = foo(194)     # Lepiej trzymać się przyjętej nomenkaltury nazw
pi_gen_3 = foo(194)
# for the_variable_that_contains_next_approximations_of_pi_from_generator in range(23):
for _ in range(23):  # Użycie _ dla nieużywanej zmiennej
    # my_pi_2.mth(next(pIgEn3))
    my_pi_2.mth(next(pi_gen_3))
my_pi_3 = pi_container()
#pi_gen = foo(6)    # pi_gen istnieje
pi_gen_1 = foo(6)
# my_pi_3.mth([i for i in list(pi_gen)])
my_pi_3.mth([i for i in list(pi_gen_1)])    # Poprawione tak, żeby była lista od pi_gen_1
print('my first pi')
# enumerate(my_pi)
enumerate_pi(my_pi)  # Użycie poprawionej funkcji
print('my second pi')
# enumerate(my_pi_2)
enumerate_pi(my_pi_2)  # Użycie poprawionej funkcji
new_file = open('some-file.txt', 'w')
new_file.write(f'my best pi: {my_pi_3.a[-1]}')
new_file.close()
