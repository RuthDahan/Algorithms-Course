# Question 3 - merge k sorted lists
from q2 import merge

def merge_sorted_lists(lists, key):
    if not lists:
        return []
    if len(lists) == 1:
        return lists[0]
    
    # שיטת "הפרד ומשול" - יעילה יותר
    mid = len(lists) // 2
    left_merged = merge_sorted_lists(lists[:mid], key)
    right_merged = merge_sorted_lists(lists[mid:], key)
    
    # אם אחת מהקריאות רקורסיביות החזירה None (כי הרשימה לא ממוינת), נחזיר None
    if left_merged is None or right_merged is None:
        return None
        
    return merge(left_merged, right_merged, key)