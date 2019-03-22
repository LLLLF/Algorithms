#!/usr/bin/python3
list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# insertion sort


def insertion_sort(list):
    for j in range(1, len(list)):
        key = list[j]
        i = j - 1
        while (i >= 0) & (list[i] > key):
            list[i+1] = list[i]
            i = i - 1
        list[i + 1] = key
    return list


#print(insertion_sort(list))


# merge sort

def merge(r, l):
    c = []
    h = j = 0
    while j < len(r) and h < len(l):
        if r[j] < l[h]:
            c.append(r[j])
            j += 1
        else:
            c.append(l[h])
            h += 1

    if j == len(r):
        for i in l[h:]:
            c.append(i)
    else:
        for i in r[j:]:
            c.append(i)

    return c


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists)//2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)



print(merge_sort(list))

