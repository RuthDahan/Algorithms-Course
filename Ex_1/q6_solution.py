# Merge Sort implementation reading from data.txt

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Recursive calls
        merge_sort(left)
        merge_sort(right)

        # Merge
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Remaining elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# Read numbers from data.txt
with open("data.txt", "r") as f:
    numbers = [int(line.strip()) for line in f]

# Sort
merge_sort(numbers)

# Print result
for num in numbers:
    print(num)
