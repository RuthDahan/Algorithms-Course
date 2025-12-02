# Question 4 - partition implementations

def partition_lomuto(a, key):
    pivot = a[-1]
    pivot_val = key(pivot)
    i = -1
    for j in range(len(a) - 1):
        if key(a[j]) <= pivot_val:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[-1] = a[-1], a[i+1]
    return i + 1

def partition_hoare(a, key):
    pivot = key(a[0])
    i = -1
    j = len(a)
    while True:
        i += 1
        while key(a[i]) < pivot:
            i += 1
        j -= 1
        while key(a[j]) > pivot:
            j -= 1
        if i >= j:
            return j
        a[i], a[j] = a[j], a[i]
