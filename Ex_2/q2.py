# Question 2 - merge + is_sorted

def is_sorted(a, key):
    for x, y in zip(a, a[1:]):
        if key(x) > key(y):
            return False
    return True

def merge(a, b, key):
    if not is_sorted(a, key) or not is_sorted(b, key):
        return None

    i = j = 0
    result = []

    while i < len(a) and j < len(b):
        if key(a[i]) <= key(b[j]):
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result.extend(a[i:])
    result.extend(b[j:])
    return result
