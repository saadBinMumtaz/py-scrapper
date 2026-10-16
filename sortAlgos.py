import sys
import time
from dataLoader import makeKey

sys.setrecursionlimit(100000)  # quick sort and merge sort recurse

cmp = 0  # compare count
swp = 0  # swap count

def bubbleSort(a):
    global cmp, swp
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            cmp += 1
            if a[j][0] > a[j + 1][0]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swp += 1
    return a

def selectionSort(a):
    global cmp, swp
    n = len(a)
    for i in range(n):
        minIndex = i
        for j in range(i + 1, n):
            cmp += 1
            if a[j][0] < a[minIndex][0]:
                minIndex = j
        if minIndex != i:
            a[i], a[minIndex] = a[minIndex], a[i]
            swp += 1
    return a

def insertionSort(a):
    global cmp, swp
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j][0] > key[0]:
            cmp += 1
            a[j + 1] = a[j]  # shift = swap
            swp += 1
            j -= 1
        a[j + 1] = key
    return a

def mergeSort(a):
    global cmp, swp
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = mergeSort(a[:mid])
    right = mergeSort(a[mid:])
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        cmp += 1
        if left[i][0] <= right[j][0]:  # <= keeps it stable
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        swp += 1  # placement = swap
    swp += (len(left) - i) + (len(right) - j)
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def partition(a, p, r):
    global cmp, swp

    pivot = a[p][0]
    i = p

    for j in range(p + 1, r + 1):
        cmp += 1

        if a[j][0] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
            swp += 1

    a[p], a[i] = a[i], a[p]
    swp += 1

    return i


def quickSort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quickSort(a, p, q - 1)
        quickSort(a, q + 1, r)

    return a

    