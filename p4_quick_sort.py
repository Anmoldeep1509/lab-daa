from util import randomizer as r
from p3_merge_sort import merge_sort
import time

# Python program for implementation of quick sort

def partition( arr, low, high):
    pivot = arr[high] # pivot 
    i = (low - 1) # Index of smaller element and indicates the right position of pivot found so far
 
    j = low
    while( j <= high - 1 ): 
        # If current element is smaller than the pivot 
        if (arr[j] < pivot):
            i += 1  # increment index of smaller element 
            arr[i], arr[j] = arr[j], arr[i] 
        j += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1] 
    return (i + 1)



#  The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low --> Starting index, 
# high --> Ending index 
def quick_sort( arr, low, high):
    if (low < high):

        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr, low, high)

        #  Separately sort elements before 
        #  partition and after partition 
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high) 


# Driver Code
if __name__ == '__main__':
  
    nums =  [5000,20000, 50000, 100000]
    print()
    print("Number of Elements \t|\t Time (QuickSort) \t|\t Time (MergeSort)")
    print("------------------------------------------------------------------------------------")
    for n in nums:
        print('\t' + str(n) + '\t', end=' ')
        array = r.randomizer(n)
        
       
        # quick sort - execution and time check
        start = time.process_time()
        quick_sort(array, 0, len(array) - 1)
        end = time.process_time()
        print("\t|\t {:.5f} \t".format(end - start), end=' ') 

        # merge sort - execution and time check
        start = time.process_time()
        merge_sort(array)
        end = time.process_time()
        # for each in myarray:
        #     print(str(each) + ' -> ' )

        # print('Start Time = ' + str(start))
        # print('End Time = ' + str(end))
        print("\t|\t {:.5f}".format(end - start)) 
        print("\t\t\t|\t\t\t\t|")

    print('END\n')

 