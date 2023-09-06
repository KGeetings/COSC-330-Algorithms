# Description: Quicksort Algorithm that proves we got the answer right
# Author: Kenyon Geetings
# Class: COSC-330 Algorithms

def quicksort(arr):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                print("After partition step:", arr)
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quicksort_helper(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            quicksort_helper(arr, low, pivot_index - 1)
            quicksort_helper(arr, pivot_index + 1, high)

    quicksort_helper(arr, 0, len(arr) - 1)

#arr = [2, 8, 7, 1, 3, 5, 6, 7]
arr = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]

print("Initial array:", arr)
quicksort(arr)
print("Sorted array:", arr)
