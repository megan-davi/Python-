def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)

# merge and quicksort (two versions)
# merge is a stable sort
def partition(alist,first,last):
   mid = (first + last) // 2

   if alist[first] <= alist[mid] <= alist[last] or alist[last] <= alist[mid] <= alist[first]:
       alist[first], alist[mid] = alist[mid], alist[first]
   elif alist[first] <= alist[last] <= alist[mid] or alist[mid] <= alist[last] <= alist[first]:
       alist[first], alist[last] = alist[last], alist[first]
   
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

alist = [54,26,93,17,77,31,44,55,20]
print(alist)
quickSort(alist)
print(alist)
