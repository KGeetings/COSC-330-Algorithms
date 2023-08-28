# Description: Merge Sort Algorithm
# Author: Kenyon Geetings
# Class: COSC-330 Algorithms

import time
import random
import numpy as np
import matplotlib.pyplot as plt

def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def measure_time(array, size):
    start_time = time.time()
    merge_sort(array)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Array size: {size}, Elapsed time: {elapsed_time:.6f} seconds")
    return elapsed_time

def plot_runtimes(sizes, runtimes, theoretical_fit):
    plt.plot(sizes, runtimes, marker='o', label='Actual Runtime')
    plt.plot(sizes, theoretical_fit, linestyle='dotted', label='Theoretical O(n log n)')
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Merge Sort Runtimes')
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    array_start = 100
    array_step = 5000
    array_max = 200000

    array_sizes = list(range(array_start, array_max + 1, array_step))
    execution_times = []

    for size in array_sizes:
        random_array = generate_random_array(size)
        time_taken = measure_time(random_array, size)
        execution_times.append(time_taken)

    # Fit a linear curve to measured runtimes (O(n log n))
    p = np.polyfit(array_sizes, execution_times, 1)
    theoretical_fit = np.polyval(p, array_sizes)

    # Print and plot results
    plot_runtimes(array_sizes, execution_times, theoretical_fit)

if __name__ == "__main__":
    main()