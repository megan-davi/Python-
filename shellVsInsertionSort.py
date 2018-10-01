"""
Prompt: Determine which sorting alogorithm is faster on average:
Shell sort or insertion sort
"""

import random
import time
from copy import deepcopy
from statistics import mean


def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)


      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue


# 100 list items
            
alist = [random.randrange(1, 101) for i in range(100)]
alist2 = deepcopy(alist)
alist3 = deepcopy(alist)
alist4 = deepcopy(alist)
alist5 = deepcopy(alist)
alist6 = deepcopy(alist)
alist7 = deepcopy(alist)
alist8 = deepcopy(alist)
alist9 = deepcopy(alist)
alist10 = deepcopy(alist)


start = time.time()
insertionSort(alist)
insertionSort(alist2)
insertionSort(alist3)
insertionSort(alist4)
insertionSort(alist5)
insertionSort(alist6)
insertionSort(alist7)
insertionSort(alist8)
insertionSort(alist9)
insertionSort(alist10)
end = time.time()

# decided to not use a while loop because it would just loop over sorting the same
#     list that it had already sorted

print("Time it took to sort 100 items via insertion was", round(end/10 - start/10, 5), "seconds.")
# divided by ten to get an average

start = time.time()
shellSort(alist)
shellSort(alist2)
shellSort(alist3)
shellSort(alist4)
shellSort(alist5)
shellSort(alist6)
shellSort(alist7)
shellSort(alist8)
shellSort(alist9)
shellSort(alist10)
end = time.time()

print("Time it took to sort 100 items via shell was", round(end/10 - start/10, 5), "seconds.")







## 500 list items
alist = [random.randrange(1, 101) for i in range(10000)]
alist2 = deepcopy(alist)
alist3 = deepcopy(alist)
alist4 = deepcopy(alist)
alist5 = deepcopy(alist)
alist6 = deepcopy(alist)
alist7 = deepcopy(alist)
alist8 = deepcopy(alist)
alist9 = deepcopy(alist)
alist10 = deepcopy(alist)


start = time.time()
insertionSort(alist)
insertionSort(alist2)
insertionSort(alist3)
insertionSort(alist4)
insertionSort(alist5)
insertionSort(alist6)
insertionSort(alist7)
insertionSort(alist8)
insertionSort(alist9)
insertionSort(alist10)
end = time.time()


print()
print("Time it took to sort 500 items via insertion was", round(end/10 - start/10, 5), "seconds.")


start = time.time()
shellSort(alist)
shellSort(alist2)
shellSort(alist3)
shellSort(alist4)
shellSort(alist5)
shellSort(alist6)
shellSort(alist7)
shellSort(alist8)
shellSort(alist9)
shellSort(alist10)
end = time.time()

print("Time it took to sort 500 items via shell was", round(end/10 - start/10, 5), "seconds.")

