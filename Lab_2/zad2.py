import multiprocessing
from multiprocessing import Process, Manager
from random import randint
import os


def generate_pseudo_random_list(count, min, max):
    randomTab = []
    for i in range(0, count):
        randomTab.append(randint(min, max))

    return randomTab



def bubble_sort(elements, asc):

    for i in range(len(elements)):
        for j in range(0, len(elements) - i - 1):

            if asc == True:   # asc = rosnąco
                if elements[j] > elements[j+1]:
                    elements[j], elements[j+1] = elements[j+1], elements[j]

            if asc == False:
                if elements[j] < elements[j+1]:
                    elements[j], elements[j+1] = elements[j+1], elements[j]

    return elements



def bubble_m(elements, asc):

    elements_1_5 = len(elements) // 5

    mid_e = len(elements) // 2
    elem1 = elements[:mid_e]
    elem2 = elements[mid_e:]
    mid1 = len(elem1) // 2
    mid2 = len(elem2) // 2
    elem11 = elem1[:mid1]
    elem12 = elem1[mid1:]
    elem21 = elem2[:mid2]
    elem22 = elem2[mid2:]

    '''
    # Element kontrolny
    print ("\tasc: ", asc)
    print("\telem1: ", elem1)
    print("\telem2: ", elem2)
    print("\telem11: ", elem11)
    print("\telem12: ", elem12)
    print("\telem21: ", elem21)
    print("\telem22: ", elem22)
    '''

    #  Użycie Managera
    # manager = Manager()
    # pre_sort = manager.list()
    processes = []
    #numbers = [1, 2, 3, 4, 5]
    elem_s = [elem11, elem12, elem21, elem22]

    for elem in elem_s:
        process = Process(target=bubble_sort, args=(elem, asc))
        processes.append(process)
        process.start()
        # process.join()

    for process in processes:
        process.join()


    pre_sort = elem11 + elem12 + elem21 + elem22
    # pre_sort.extend(elem11 + elem12 + elem21 + elem22)
    #print("\tpre_sort: ", pre_sort)
    bubble_sort(pre_sort, asc)
    #print("\tpost_sort: ", pre_sort)

    # Używamy elements[:], aby skopiować zawartość pre_sort, a nie tylko przypisać referencję.
    #  To zapobiega utracie referencji do oryginalnej listy elements.
    elements[:] = pre_sort





if __name__ == '__main__':

    tab1 = [1, 10, 2, 3, 8, 10, 12, 0, 50]
    tab1s = tab1
    #tab1s.sort(reverse=True)
    print("\nTablica przed sortowaniem: \n", tab1)
    #bubble_sort(tab1, True)
    bubble_m(tab1, False)
    print("\nTablica po sortowaniu: \n", tab1)
        #print("\nTab: \n", tab1s)
    #print("\n\tCzy algorytm działa poprawnie ? \t ", (tab1s == tab1))


'''
rTab1 = generate_pseudo_random_list(11, 0, 100)
print("\nTablica przed sortowaniem: \n", rTab1)
#bubble_sort(rTab1, True)
#rTab1 = merge_sort(rTab1, True)
rTab1s = rTab1
rTab1s.sort()
bubble_m(rTab1, True)
print("\nTablica po sortowaniu: \n", rTab1)
print("\n\tCzy algorytm działa poprawnie ? \t ", (rTab1s == rTab1))
'''
