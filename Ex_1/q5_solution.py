
import random
import string

def random_string(length=5):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def create_random_tuples(n, types=[int, float, str]):
    output = []
    for _ in range(n):
        t = []
        for tp in types:
            if tp == int:
                t.append(random.randint(0, 1000))
            elif tp == float:
                t.append(random.random() * 1000)
            elif tp == str:
                t.append(random_string())
        output.append(tuple(t))
    return output

def insertion_sort(a, key):
    for i in range(1, len(a)):
        current = a[i]
        current_key = key(current)
        j = i - 1

        while j >= 0 and key(a[j]) > current_key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = current

    return a

def main():
    arr = create_random_tuples(10)

    print("Original:")
    for x in arr:
        print(x)

    print("\nSort by item 0:")
    sorted0 = insertion_sort(arr.copy(), key=lambda x: x[0])
    for x in sorted0:
        print(x)

    print("\nSort by item 1:")
    sorted1 = insertion_sort(arr.copy(), key=lambda x: x[1])
    for x in sorted1:
        print(x)

    print("\nSort by item 2:")
    sorted2 = insertion_sort(arr.copy(), key=lambda x: x[2])
    for x in sorted2:
        print(x)

if __name__ == "__main__":
    main()
