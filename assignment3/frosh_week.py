from random import randint, sample
from pprint import pprint
def mergeSort(arr, n):
    # A temp_arr is created to store
    # sorted array in merge function
    temp_arr = [0]*n
    return _mergeSort(arr, temp_arr, 0, n-1)
 
# This Function will use MergeSort to count inversions
 
 
def _mergeSort(arr, temp_arr, left, right):
 
    # A variable inv_count is used to store
    # inversion counts in each recursive call
 
    inv_count = 0
 
    # We will make a recursive call if and only if
    # we have more than one elements
 
    if left < right:
 
        # mid is calculated to divide the array into two subarrays
        # Floor division is must in case of python
 
        mid = (left + right)//2
 
        # It will calculate inversion
        # counts in the left subarray
 
        inv_count += _mergeSort(arr, temp_arr,
                                left, mid)
 
        # It will calculate inversion
        # counts in right subarray
 
        inv_count += _mergeSort(arr, temp_arr,
                                mid + 1, right)
 
        # It will merge two subarrays in
        # a sorted subarray
 
        inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count
 
# This function will merge two subarrays
# in a single sorted subarray
 
 
def merge(arr, temp_arr, left, mid, right):
    i = left     # Starting index of left subarray
    j = mid + 1  # Starting index of right subarray
    k = left     # Starting index of to be sorted subarray
    inv_count = 0
 
    # Conditions are checked to make sure that
    # i and j don't exceed their
    # subarray limits.
 
    while i <= mid and j <= right:
 
        # There will be no inversion if arr[i] <= arr[j]
 
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            # Inversion will occur.
            temp_arr[k] = arr[j]
            inv_count += (mid-i + 1)
            k += 1
            j += 1
 
    # Copy the remaining elements of left
    # subarray into temporary array
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1
 
    # Copy the remaining elements of right
    # subarray into temporary array
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1
 
    # Copy the sorted subarray into Original array
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]
 
    return inv_count















####################################################
def r_merge(a1, a_1swaps, a2, a_2swaps):
    a1 = a1[::-1]
    a2 = a2[::-1]
    a3 = []
    swaps = 0
    while len(a1) != 0 and len(a2) !=0:
        if a1[-1] < a2[-1]:
            a3.append(a1.pop())
        else:
            a3.append(a2.pop())  
            swaps += len(a1)
    a3.extend(a1[::-1])
    a3.extend(a2[::-1])



    return a3, (swaps + a_1swaps + a_2swaps)

def merge_sort_count(students):
    n = len(students)
    if n == 1:
        return students, 0
    mid = n//2
    a1, a_1swaps = merge_sort_count(students[:mid])
    a2, a_2swaps = merge_sort_count(students[mid:])
    return r_merge(a1, a_1swaps, a2, a_2swaps)

def get_students():
    return [int(input()) for _ in range(int(input())) ]

def generate_test_cases(k):
    min_int = 1
    max_int = 10**(9) + 1
    max_list_size = 5
    return [sample(range(min_int, max_int), max_list_size) for _ in range(k)]
    
    

students = get_students()
print(merge_sort_count(students)[1])
