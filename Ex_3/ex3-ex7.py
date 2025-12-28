
# --- Question 3---

def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


# --- Question 4---

def is_max_heap(arr, i=0, key=lambda x: x):

    n = len(arr)
    for k in range(i + 1, n):
        p = parent(k)

        #   Check only if parent is within the checked range
        if p >= i:
            # If child is greater than parent -> It's not a max-heap
            if key(arr[k]) > key(arr[p]):
                return False

    return True


# ---Question 5---

def max_heapify(arr, i, heap_size, key=lambda x: x):

    l = left(i)
    r = right(i)
    largest = i

    # Check if left child exists and is greater than current node
    if l < heap_size and key(arr[l]) > key(arr[largest]):
        largest = l

    # Check if right child exists and is greater than current largest
    if r < heap_size and key(arr[r]) > key(arr[largest]):
        largest = r

    # If the root is not the largest, swap and continue recursively
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, heap_size, key)


# --- Question 6 ---

def build_max_heap(arr, key=lambda x: x):

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, i, n, key)


# --- שאלה 7: מיון ערימה (Heap Sort) ---

def heap_sort(arr, key=lambda x: x):

    # 1. Build the heap
    build_max_heap(arr, key)

    heap_size = len(arr)

    # 2. Extract elements one by one
    for i in range(len(arr) - 1, 0, -1):
        # Move current root (maximum) to the end
        arr[i], arr[0] = arr[0], arr[i]

        # Reduce heap size
        heap_size -= 1

        # Fix the heap with the new root
        max_heapify(arr, 0, heap_size, key)


# ---  ---
if __name__ == "__main__":
    test_arr = [12, 11, 13, 5, 6, 7]
    print("המערך המקורי:", test_arr)

    heap_sort(test_arr)

    print("המערך הממוין:", test_arr)

    # בדיקה אם המיון הצליח
    if test_arr == [5, 6, 7, 11, 12, 13]:
        print(" הבדיקה עברה בהצלחה!")
    else:
        print(" נכשל.")

