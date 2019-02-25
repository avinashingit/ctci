def merge_sorted_arrays(list1, list2):
    total_length = len(list1) + len(list2)
    sorted_array = []
    i, j = 0, 0
    while i+j < total_length:
        if i == len(list1):
            if j != len(list2):
                sorted_array.append(list2[j])
                j += 1
        elif j == len(list2):
            sorted_array.append(list1[i])
            i += 1
        elif list1[i] < list2[j]:
            sorted_array.append(list1[i])
            i += 1
        elif list1[i] >= list2[j]:
            sorted_array.append(list2[j])
            j += 1
    return sorted_array


def merge_multiple_arrays(arrays):
    if len(arrays) == 1:
        return arrays
    else:
        new_arrays = []
        for i in range(0, len(arrays), 2):
            if i == len(arrays)-1:
                new_arrays.append(arrays[i])
            else:
                new_arrays.append(merge_sorted_arrays(arrays[i], arrays[i+1]))
        return merge_multiple_arrays(new_arrays)


l1 = [3, 4, 6, 10, 11, 15]
l2 = [1, 5, 8, 12, 14, 16]
l3 = [1, 2, 3, 4, 5, 50]
l4 = [23, 24, 25, 29, 30, 31]
print(merge_multiple_arrays([l1, l2, l3, l4]))
