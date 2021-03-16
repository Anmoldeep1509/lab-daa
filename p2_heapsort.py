import util.randomizer as r
import time
from p1_insert_sort import insertion_sort

# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(arr, n, i): 
    largest = i  # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 
  
# The main function to sort an array of given size 
def heap_sort(arr): 
    iters = 1
    # Build a maxheap. 
    # Since last parent will be at ((n//2)-1) we can start at that location. 
    for i in range(n // 2 - 1, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   # swap 
        heapify(arr, i, 0) 
        iters += 1

    return iters
  

# Driver Code
if __name__ == '__main__':
    
    # print("Given array is", end="\n")
    # print_list(arr)

    i=1
    nums = [100,500,1000,2000,3000,4000,5000]
    print()
    print("Number of Elements \t|\t Time (HeapSort) \t|\t Time (InsertionSort)")
    print("------------------------------------------------------------------------------------")
    for n in nums:
        print('\t' + str(n) + '\t', end=' ')
        array = r.randomizer(n)
        
        # *********** DEBUG statements *********
        # n = int(input('Enter number of elements:'))    
        # print(n)
        # myarray = list({55,23,61,77,12,1})
        # n = len(myarray)
        # print(myarray)
        # **************************************

        # heap sort - execution and time check
        start = time.process_time()
        heap_sort(array)
        end = time.process_time()
        print("\t|\t {:.5f} \t".format(end - start), end=' ') 

        # insertion sort - execution and time check
        start = time.process_time()
        insertion_sort(n,array)
        end = time.process_time()
        # for each in myarray:
        #     print(str(each) + ' -> ' )

        # print('Start Time = ' + str(start))
        # print('End Time = ' + str(end))
        print("\t|\t {:.5f}".format(end - start)) 
        print("\t\t\t|\t\t\t\t|")

    print('END\n')
        
# Driver code to test above 
# arr = [ 12, 11, 13, 5, 6, 7] 
# arr = list()
# r.randomizer(arr, 10, upperlimit=200)
# iters = heap_sort(arr) 
# n = len(arr) 
# # print ("Sorted array is") 
# # for i in range(n): 
# #     print ("%d->" %arr[i], end=" ")
# print()
# print('Iterations = ' + str(iters))