import random

# returns a new array of given size with random elements 
# @input size of array to be created
def randomizer(n, upperlimit=9999999999):
    arr = []
    random.seed(365)
    # take array input
    for i in range(n):
        # myarray.append(int(input('Enter Element {}: '.format(str(i+1)))))
        arr.append(int(random.randint(0,upperlimit)))

    return arr

