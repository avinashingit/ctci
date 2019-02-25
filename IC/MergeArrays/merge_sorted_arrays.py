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


l1 = [3, 4, 6, 10, 11, 15]
l2 = [1, 5, 8, 12, 14, 16]
print(merge_sorted_arrays(l1, l2))
