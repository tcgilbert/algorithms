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
    result = []
    combined_list_length = len(left) + len(right)
    while len(result) < combined_list_length:

        if len(left) == 0:
            result += right
            right = []
        elif len(right) == 0:
            result += left
            left = []
        elif left[0] < right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    return result



print(merge_sort(array_to_sort))

    