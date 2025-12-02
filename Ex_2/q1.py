# Question 1 - sorting random tuples
from random_tuples import create_random_tuples

def demo_sorted_random_tuples():
    lst = create_random_tuples(5, 3, [int, float, str])
    print("Original list:")
    print(lst)

    sorted_by_int = sorted(lst, key=lambda t: t[0])
    sorted_by_float = sorted(lst, key=lambda t: t[1])
    sorted_by_str = sorted(lst, key=lambda t: t[2])

    print("\nSorted by int:")
    print(sorted_by_int)

    print("\nSorted by float:")
    print(sorted_by_float)

    print("\nSorted by str:")
    print(sorted_by_str)
