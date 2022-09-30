#!/usr/bin/python
# -*- coding: UTF-8 -*-


def mergeSort(list):
    # sf
    if (len(list) > 1):
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]

        mergeSort(left)
        mergeSort(right)

        a, b, c = 0, 0, 0
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                list[c] = left[a]
                a = a + 1
            else:
                list[c] = right[b]
                b = b + 1
            c = c + 1
        while a < len(left):
            list[c] = left[a]
            a = a + 1
            c = c + 1
        while b < len(right):
            list[c] = right[b]
            b = b + 1
            c = c + 1
    return list

def shellSort(list):

    None



print(mergeSort([43, 2, 4, 78, 5, 3, 13, 0]))
