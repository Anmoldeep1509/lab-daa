from util import randomizer as r 
import time

# test_cases = int(input('Enter number of Test cases:'))


def insertion_sort(n,arr):
    # Perform the step for every element
    for i in range(n):
        # keeps the value seperately, to compare and keep safe
        # because pushing elements one index ahead, will destroy the key value in array
        key = arr[i]

        # Move elements of arr[0..i-1], that are  
        #     greater than key, to one position ahead  
        #     of their current position
        j = i-1
        while(j>=0 and arr[j]> key):
            arr[j+1] = arr[j]
            j= j-1
        arr[j+1] = key


def drive_algo(algo, nums = [100,500,1000,2000,3000,4000,5000]):
    print()
    print("Number of Elements \t|\t Time elapsed")
    print("----------------------------------------------")
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


        start = time.process_time()

        algo(n,array)
        end = time.process_time()
        # for each in myarray:
        #     print(str(each) + ' -> ' )

        # print('Start Time = ' + str(start))
        # print('End Time = ' + str(end))
        print("\t|\t", str(end - start)) 
        print("\t\t\t|\t")

    print('END\n')

# driver code
# drive_algo(algo=insertion_sort)
