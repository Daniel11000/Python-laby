from random import randint


def generate_pseudo_random_list(count, min, max):
    randomTab = []
    for i in range(0, count):
        randomTab.append(randint(min, max))

    # while count > 0:
    #     randomTab.append(randint(min, max))
    #     count -= 1

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



def merge_sort(elements, asc):   # Sortowanie Przez Scalanie
    if len(elements) < 2:
        return elements
    result = []
    mid = len(elements) // 2   # dzielenie całkowite (floor division)
    left = merge_sort(elements[:mid], asc)
    right = merge_sort(elements[mid:], asc)

    if asc == True:   # asc = rosnąco
        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))

    if asc == False:
        while len(left) > 0 and len(right) > 0:
            if left[0] > right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))

    result += left
    result += right

    # -----
    # aby można było używać: merge_sort(rTab1, True) zamiast rTab1 = merge_sort(rTab1, True)
    for i in range(0, len(result)):
        elements[i] = result[i]
    # -----

    return result




tab1 = [1, 10, 2, 3, 8, 10, 12, 0, 50]
tab1s = tab1
tab1s.sort(reverse=True)
print("\nTablica przed sortowaniem: \n", tab1)
#bubble_sort(tab1, True)
bubble_sort(tab1, False)
print("\nTablica po sortowaniu: \n", tab1)
    #print("\nTab: \n", tab1s)
print("\n\tCzy algorytm działa poprawnie ? \t ", (tab1s == tab1))

print("\n------------------------------------\n")

rTab1 = generate_pseudo_random_list(11, 0, 100)
print("\nTablica przed sortowaniem: \n", rTab1)
#bubble_sort(rTab1, True)
#rTab1 = merge_sort(rTab1, True)
rTab1s = rTab1
rTab1s.sort()
merge_sort(rTab1, True)
print("\nTablica po sortowaniu: \n", rTab1)
print("\n\tCzy algorytm działa poprawnie ? \t ", (rTab1s == rTab1))

