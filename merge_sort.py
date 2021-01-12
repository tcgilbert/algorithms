# break down array until you cannot anymore


array_to_sort = [1, 6, 2, 4, 6, 3, 8, 6, 9, 0, 8, 6, 4, 11]


def merge_sort(l):
    if len(l) <= 1:
        return l
    
    midpoint = int(len(l) / 2)
    left = merge_sort(l[:midpoint])
    right = merge_sort(l[midpoint:])

    return merge(left, right)

def merge(left, right):
    results = []
    if left[0] >= right[0]:
        results.append(left[0])
        results.append(right[0])
    else:
        results.append(right[0])
        results.append(left[0])
    return results


    
print(merge_sort(array_to_sort))