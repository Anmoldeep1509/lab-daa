from util.print_list import print_list
from util.randomizer import randomizer
import time

# Python program for implementation of merge_sort
def merge_sort(arr):
    if len(arr) > 1:
         # Find mid of the array
        mid = len(arr)//2
 
        # left half
        L = arr[:mid]
 
        # right half
        R = arr[mid:]
 
        # perform mergerSort on left half
        merge_sort(L)
 
        # perform merge_sort on right half
        merge_sort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays from L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
 

# Driver Code
if __name__ == '__main__':
    
    # print("Given array is", end="\n")
    # print_list(arr)

    i=1
    for n in [5000,20000, 50000, 100000]:

        arr = randomizer(n)
        print('Iteration #'+str(i))
        print('Number of elements:' + str(n))   
        start = time.process_time()

        merge_sort(arr)
        end = time.process_time()

        # print("Sorted array is: ", end="\n")
        print("Time elapsed =", str(end - start)) 
        print()
        i += 1

    # print_list(arr)
 