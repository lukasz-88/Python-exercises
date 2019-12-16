"""
Exercise 20: Element Search
Write a function that takes an ordered list of
numbers (a list where the elements are in order from
smallest to largest) and another number. The function decides whether
or not the given number is inside the list and returns (then prints)
an appropriate boolean.

Extras:
Use binary search.
"""

a = [1, 3, 5, 30, 42, 43, 500, 1000]
elem = 9


def binary_search(elements, element):

    start = 0
    end = len(elements) - 1
    result = False

    while (end - start) >= 0 and result is False:
        mid = (start + end) // 2
        if element == elements[mid]:
            result = True
        elif element < elements[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return result


binary_search(a, elem)
