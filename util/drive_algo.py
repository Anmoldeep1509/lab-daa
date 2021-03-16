import randomizer as r
import time

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
        