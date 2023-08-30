# Description: Sorting Comparison (Insertion Sort vs. Merge Sort)
# Author: Kenyon Geetings & Sam Scholz
# Class: COSC-330 Algorithms

import time
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

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

def measure_time(sort_func, array, size):
    start_time = time.time()
    sort_func(array)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Array size: {size}, Elapsed time: {elapsed_time:.6f} seconds for {sort_func.__name__}")
    return elapsed_time

def plot_runtimes(sizes, runtimes_actual, runtimes_theoretical, title):
    plt.plot(sizes, runtimes_actual, marker='o', label='Actual Runtime')
    plt.plot(sizes, runtimes_theoretical, linestyle='dotted', label='Theoretical Runtime')
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    array_start = 100
    array_step = 750
    array_max = 18850
    array_max = 10000

    array_sizes = list(range(array_start, array_max + 1, array_step))
    execution_times_insertion = []
    execution_times_merge = []
    n_squared_values = []
    n_log_n_values = []

    runtime_data = pd.DataFrame(columns=['Array Size', 'Insertion Sort Time', 'Merge Sort Time'])

    for size in array_sizes:
        random_array = generate_random_array(size)
        
        random_array_insertion = random_array.copy()
        time_taken_insertion = measure_time(insertion_sort, random_array_insertion, size)
        execution_times_insertion.append(time_taken_insertion)
        
        random_array_merge = random_array.copy()
        time_taken_merge = measure_time(merge_sort, random_array_merge, size)
        execution_times_merge.append(time_taken_merge)
        n_squared = size ** 2
        n_log_n = size * np.log2(size)
        n_squared_values.append(n_squared)
        n_log_n_values.append(n_log_n)

        runtime_data = pd.concat([runtime_data, pd.DataFrame({'Array Size': [size], 'Insertion Sort Time': [time_taken_insertion], 'Merge Sort Time': [time_taken_merge], 'n^2': [n_squared], 'n log n': [n_log_n]})], ignore_index=True)
    
    # Fit curves and plot results for both algorithms
    p_insertion = np.polyfit(array_sizes, execution_times_insertion, 2)
    theoretical_fit_insertion = np.polyval(p_insertion, array_sizes)
    
    p_merge = np.polyfit(array_sizes, execution_times_merge, 1)
    theoretical_fit_merge = np.polyval(p_merge, array_sizes)

    plot_runtimes(array_sizes, execution_times_insertion, theoretical_fit_insertion, 'Insertion Sort Runtimes')
    plot_runtimes(array_sizes, execution_times_merge, theoretical_fit_merge, 'Merge Sort Runtimes')

    # Plot both runtimes on the same graph
    plt.plot(array_sizes, execution_times_insertion, marker='o', label='Insertion Sort')
    plt.plot(array_sizes, execution_times_merge, marker='o', label='Merge Sort')
    plt.plot(array_sizes, theoretical_fit_insertion, linestyle='dotted', label='Insertion Sort Theoretical')
    plt.plot(array_sizes, theoretical_fit_merge, linestyle='dotted', label='Merge Sort Theoretical')
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Insertion Sort vs. Merge Sort Runtimes')
    plt.grid(True)
    plt.legend()
    plt.show()

    excel_filename = 'sorting_comparison.xlsx'
    runtime_data.to_excel(excel_filename, index=False)
    print(f"Runtime data saved to {excel_filename}")

if __name__ == "__main__":
    main()
