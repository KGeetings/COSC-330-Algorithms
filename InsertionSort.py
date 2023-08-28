# Description: Insertion Sort Algorithm
# Author: Kenyon Geetings
# Class: COSC-330 Algorithms

import time
import random
import numpy as np
import matplotlib.pyplot as plt

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def measure_time(array, size):
    start_time = time.time()
    insertion_sort(array)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Array size: {size}, Elapsed time: {elapsed_time:.6f} seconds")
    return elapsed_time

def plot_runtimes(sizes, runtimes, theoretical_fit):
    plt.plot(sizes, runtimes, marker='o', label='Actual Runtime')
    plt.plot(sizes, theoretical_fit, linestyle='dotted', label='Theoretical O(n^2)')
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Insertion Sort Runtimes')
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    array_sizes = [10, 50, 100, 500, 1000, 2500, 5000, 7500, 10000]
    execution_times = []

    for size in array_sizes:
        random_array = generate_random_array(size)
        time_taken = measure_time(random_array, size)
        execution_times.append(time_taken)

    # Fit a quadratic curve to measured runtimes
    p = np.polyfit(array_sizes, execution_times, 2)
    theoretical_fit = np.polyval(p, array_sizes)

    # Print and plot results
    plot_runtimes(array_sizes, execution_times, theoretical_fit)

if __name__ == "__main__":
    main()
