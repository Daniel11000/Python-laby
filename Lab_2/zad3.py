import unittest
from zad2 import bubble_m
from zad2 import bubble_sort
from zad2 import generate_pseudo_random_list

import timeit
import matplotlib.pyplot as plt

class TestBubble_m(unittest.TestCase):

    # Te listy nie powinny by losowane w tescie, tylko powinny by podane parametry
    def test_bubble_m_ascending(self):
        input_list = generate_pseudo_random_list(500, -100, 1000)


        expected_output = sorted(input_list)
        # time_sort = timeit.timeit("expected_output = sorted(input_list)", globals=globals(), number=1)
        # print(f"Czas time_sort: {time_sort} sekundy")

        il = input_list[:]

        # bubble_m(input_list, True)
        time_bubble_m = timeit.timeit(lambda: bubble_m(input_list, True), globals=globals(), number=1)
        print(f"Czas time_bubble_m: {time_bubble_m} sekundy")

        # bubble_sort(il, True)
        time_bubble_sort = timeit.timeit(lambda: bubble_sort(il, True), globals=globals(), number=1)
        print(f"Czas time_bubble_sort: {time_bubble_sort} sekundy")

        # WYKRES Słupkowy
        dane = [time_bubble_m, time_bubble_sort]
        nazwy = ("time_bubble_m", "time_bubble_sort")
        plt.bar(nazwy, dane)
        plt.title("Dane dla sortowania 500 elementów")
        plt.show()

        self.assertEqual(input_list, expected_output)
        #print("Sort")


    def test_bubble_m_descending(self):
        # REVERSED
        input_list_r = generate_pseudo_random_list(9000, -100, 10000)

        expected_output_r = sorted(input_list_r, reverse=True)
        # time_sort_r = timeit.timeit("expected_output_r = sorted(input_list_r, reverse=True)", globals=globals(), number=1)
        # print(f"Czas time_sort_r: {time_sort_r} sekundy")

        il_r = input_list_r[:]

        # bubble_m(input_list_r, False)
        time_bubble_m_r = timeit.timeit(lambda: bubble_m(input_list_r, False), globals=globals(), number=1)
        print(f"Czas time_bubble_m_r: {time_bubble_m_r} sekundy")

        # bubble_sort(il_r, False)
        time_bubble_sort_r = timeit.timeit(lambda: bubble_sort(il_r, False), globals=globals(), number=1)
        print(f"Czas time_bubble_sort_r: {time_bubble_sort_r} sekundy")

        # WYKRES Słupkowy
        dane = [time_bubble_m_r, time_bubble_sort_r]
        nazwy = ("time_bubble_m_r", "time_bubble_sort_r")
        plt.bar(nazwy, dane)
        plt.title("Dane dla sortowania 9000 elementów")
        plt.show()

        self.assertEqual(input_list_r, expected_output_r)
        # print("Reversed Sort")


if __name__ == '__main__':
    unittest.main()
