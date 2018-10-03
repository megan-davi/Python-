
"""
Prompt: Determine which sorting algorithm is faster on average:
Shell sort or insertion sort
"""

import random
from timeit import default_timer as timer
from copy import deepcopy



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


            
alist = [random.randrange(1, 101) for i in range(1000)]
alistShell = deepcopy(alist)
alist2 = [random.randrange(1, 101) for i in range(500)]
alist2Shell = deepcopy(alist2)
alist3 = [random.randrange(1, 101) for i in range(100)]
alist3Shell = deepcopy(alist3)

print("For a random list with numbers ranging from 1 to 100:")
print()

## Insertion Sorting

# 100 items
start = 0
end = 0
count = 0
average = []
while count < 10:
    start = timer()
    insertionSort(alist3)
    end = timer()
    count += 1
    runtime = end - start
    average.append(runtime)
avg = (sum(average) / 10)
print("Average runtime for insertion sorting 100 elements is", round(avg * 1000000, 4), "microseconds.")


# 500 items
start = 0
end = 0
count = 0
average = []
while count < 10:
    start = timer()
    insertionSort(alist2)
    end = timer()
    count += 1
    runtime = end - start
    average.append(runtime)
avg = (sum(average) / 10)
print("Average runtime for insertion sorting 500 elements is", round(avg * 1000000, 4), "microseconds.")


# 1000 items
start = 0
end = 0
count = 0
average = []
while count < 10:
    start = timer()
    insertionSort(alist)
    end = timer()
    count += 1
    runtime = end - start
    average.append(runtime)
avg = (sum(average) / 10)
print("Average runtime for insertion sorting 1000 elements is", round(avg * 1000000, 4), "microseconds.")
print()

## Shell Sorting

# 100 items
start = 0
end = 0
count = 0
average = []
while count < 10:
    start = timer()
    insertionSort(alist3Shell)
    end = timer()
    count += 1
    runtime = end - start
    average.append(runtime)
avg = (sum(average) / 10)
print("Average runtime for Shell sorting 100 elements is", round(avg * 1000000, 4), "microseconds.")


# 500 items
start = 0
end = 0
count = 0
average = []
while count < 10:
    start = timer()
    insertionSort(alist2Shell)
    end = timer()
    count += 1
    runtime = end - start
    average.append(runtime)
avg = (sum(average) / 10)
print("Average runtime for Shell sorting 500 elements is", round(avg * 1000000, 4), "microseconds.")


# 1000 items
start = 0
end = 0
count = 0
average = []
while count < 10:
    start = timer()
    insertionSort(alistShell)
    end = timer()
    count += 1
    runtime = end - start
    average.append(runtime)
avg = (sum(average) / 10)
print("Average runtime for Shell sorting 1000 elements is", round(avg * 1000000, 4), "microseconds.")


