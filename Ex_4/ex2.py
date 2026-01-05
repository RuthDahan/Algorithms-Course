def partition(arr, left, right, key):

    pivot = arr[right]  # בוחרים את האיבר האחרון כציר
    i = left - 1  # האינדקס של האיבר הקטן יותר

    for j in range(left, right):
        # אם האיבר הנוכחי קטן או שווה לציר
        # שימי לב לשימוש ב-key לצורך ההשוואה
        if key(arr[j]) <= key(pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # החלפה (swap)

    # בסוף שמים את הציר במקום הנכון שלו (אחרי כל הקטנים ממנו)
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def quick_kth(arr, left, right, k, key=lambda x: x):
    """
    Finds the k-th smallest element using QuickSelect algorithm.
    k is the index (0-based) in the sorted array.
    """
    # תנאי עצירה: אם נשאר רק איבר אחד, הוא חייב להיות התשובה
    if left == right:
        return arr[left]

    # מפעילים את ה-partition ומקבלים את המיקום הסופי של הציר
    pivot_index = partition(arr, left, right, key)

    # בודקים אם הציר נחת בדיוק במקום שחיפשנו (k)
    if k == pivot_index:
        return arr[k]

    # אם k קטן ממיקום הציר - מחפשים רק בצד שמאל
    elif k < pivot_index:
        return quick_kth(arr, left, pivot_index - 1, k, key)

    # אחרת, k גדול ממיקום הציר - מחפשים רק בצד ימין
    else:
        return quick_kth(arr, pivot_index + 1, right, k, key)