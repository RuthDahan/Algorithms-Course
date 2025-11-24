
import random
import string

# ---------------------------
# סעיף א - פונקציה find_min
# ---------------------------
def find_min(a, key):
    if not a:
        raise ValueError("List is empty")

    min_item = a[0]
    max_item = a[0]
    min_key = key(a[0])
    max_key = key(a[0])

    for item in a[1:]:
        current_key = key(item)

        if current_key < min_key:
            min_key = current_key
            min_item = item

        if current_key > max_key:
            max_key = current_key
            max_item = item

    return min_item, max_item


# פונקציה ליצירת מחרוזת אקראית
def random_string(length=5):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


# יצירת 100 tuples מסוג (int, float, str)
def create_random_tuples(n):
    arr = []
    for _ in range(n):
        num_int = random.randint(0, 1000)
        num_float = random.random() * 100
        s = random_string()
        arr.append((num_int, num_float, s))
    return arr


# ---------------------------
# סעיף ב - main
# ---------------------------
def main():
    arr = create_random_tuples(100)
    min_item, max_item = find_min(arr, key=lambda x: x[2])

    print("min=", min_item)
    print("max=", max_item)


if __name__ == "__main__":
    main()
