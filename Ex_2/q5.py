# Partition with two pivots - ready for submission

def partition_two_pivots(a, key, pivot1, pivot2):
    """
    מחלק את המערך לשלושה אזורים באמצעות שני פיבוטים:
    1. איברים שקטנים מ-pivot1
    2. איברים בין pivot1 ל-pivot2 כולל
    3. איברים שגדולים מ-pivot2

    הפונקציה עובדת בזמן O(n) וללא שימוש בזיכרון נוסף (in-place).
    הפונקציה מחזירה את הגבולות של האזור האמצעי.
    """

    # במקרה שהפיבוטים הפוכים – נחליף ביניהם
    if pivot1 > pivot2:
        pivot1, pivot2 = pivot2, pivot1

    low = 0
    mid = 0
    high = len(a) - 1

    while mid <= high:
        if key(a[mid]) < pivot1:
            a[low], a[mid] = a[mid], a[low]
            low += 1
            mid += 1
        elif key(a[mid]) > pivot2:
            a[mid], a[high] = a[high], a[mid]
            high -= 1
        else:
            mid += 1

    return low, high


# דוגמה לשימוש:
if __name__ == "__main__":
    arr = [7, 2, 9, 1, 5, 8, 3, 6, 4]
    l, h = partition_two_pivots(arr, key=lambda x: x, pivot1=3, pivot2=6)
    print("Array after partition:", arr)
    print("Middle segment borders:", (l, h))
