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