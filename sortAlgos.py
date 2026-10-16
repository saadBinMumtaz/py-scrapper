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

def heapify(a, n, i):
    global cmp, swp

    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n:
        cmp += 1
        if a[left][0] > a[largest][0]:
            largest = left

    if right < n:
        cmp += 1
        if a[right][0] > a[largest][0]:
            largest = right

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        swp += 1
        heapify(a, n, largest)


def heapSort(a):
    global cmp, swp
    n = len(a)

    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)

    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        swp += 1
        heapify(a, i, 0)

    return a

def shellSort(a):
    global cmp, swp
    n = len(a)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            j = i

            while j >= gap:
                cmp += 1

                if a[j - gap][0] <= temp[0]:
                    break

                a[j] = a[j - gap]
                swp += 1
                j -= gap

            a[j] = temp

        gap //= 2

    return a

def countingSort(arr):
    global cmp, swp

    lo = min(arr)
    hi = max(arr)
    count = [0] * (hi - lo + 1)
    output = [0] * len(arr)

    for x in arr:
        count[x - lo] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for x in reversed(arr):
        count[x - lo] -= 1
        output[count[x - lo]] = x
        swp += 1

    return output

def countSortByDigit(arr, exp):
    global cmp, swp

    count = [0] * 10
    output = [0] * len(arr)

    for x in arr:
        digit = (x // exp) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for x in reversed(arr):
        digit = (x // exp) % 10
        count[digit] -= 1
        output[count[digit]] = x
        swp += 1

    return output


def radixSort(arr):
    global cmp, swp

    exp = 1
    biggest = max(arr)

    while biggest // exp > 0:
        arr = countSortByDigit(arr, exp)
        exp *= 10

    return arr

def bucketSort(arr):
    global cmp, swp

    n = len(arr)
    buckets = [[] for i in range(n)]

    for x in arr:
        buckets[int(n * x)].append(x)

    for b in buckets:
        insertionSort(b)

    result = []

    for b in buckets:
        result.extend(b)

    return result