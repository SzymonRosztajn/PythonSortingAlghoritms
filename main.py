import sys
import time

import numpy as np

from random_array import random_array
from sorting_alghoritms.heapsort import heapsort
from sorting_alghoritms.mergesort import merge_sort
from sorting_alghoritms.quicksort_lomuto import quicksort

sys.setrecursionlimit(10_000)

# Wykonanie algorytmów sortowania dla tablicy losowych liczb
start_time = time.time()
quicksort(random_array.copy(), 0, len(random_array) - 1)
end_time = time.time()
quicksort_time = end_time - start_time

start_time = time.time()
heapsort(random_array.copy())
end_time = time.time()
heapsort_time = end_time - start_time

start_time = time.time()
merge_sort(random_array.copy())
end_time = time.time()
merge_sort_time = end_time - start_time

print("Czas wykonania dla tablicy losowych liczb:")
print("QuickSort:", quicksort_time)
print("Heap Sort:", heapsort_time)
print("Merge Sort:", merge_sort_time)
print()

# Generowanie tablicy odwrotnie posortowanych liczb
reverse_sorted_array = np.sort(random_array)[::-1]

# Wykonanie algorytmów sortowania dla tablicy odwrotnie posortowanych liczb
start_time = time.time()
quicksort(reverse_sorted_array.copy(), 0, len(reverse_sorted_array) - 1)
end_time = time.time()
quicksort_time = end_time - start_time

start_time = time.time()
heapsort(reverse_sorted_array.copy())
end_time = time.time()
heapsort_time = end_time - start_time

start_time = time.time()
merge_sort(reverse_sorted_array.copy())
end_time = time.time()
merge_sort_time = end_time - start_time

print("Czas wykonania dla tablicy odwrotnie posortowanych liczb:")
print("QuickSort:", quicksort_time)
print("Heap Sort:", heapsort_time)
print("Merge Sort:", merge_sort_time)
print()

# Generowanie tablicy posortowanych liczb
sorted_array = np.sort(random_array)

# Wykonanie algorytmów sortowania dla tablicy posortowanych liczb
start_time = time.time()
quicksort(sorted_array.copy(), 0, len(sorted_array) - 1)
end_time = time.time()
quicksort_time = end_time - start_time

start_time = time.time()
heapsort(sorted_array.copy())
end_time = time.time()
heapsort_time = end_time - start_time

start_time = time.time()
merge_sort(sorted_array.copy())
end_time = time.time()
merge_sort_time = end_time - start_time

print("Czas wykonania dla tablicy posortowanych liczb:")
print("QuickSort:", quicksort_time)
print("Heap Sort:", heapsort_time)
print("Merge Sort:", merge_sort_time)
print()