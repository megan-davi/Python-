'''
Multipies a matrix using multithreading
'''

import threading

def matrixMultiply(row, column, inner): # one term only
    global a, b, c, lock
    sum = 0
    for r in range(inner):
        sum = sum + a[row][r] * b[r][column]
    lock.acquire()
    c[row][column] = sum
    lock.release()

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

b = [[10, 11, 12],
     [13, 14, 15],
     [16, 17, 18]]

c = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

lock = threading.Lock()
threads = []

for row in range(3):       
    for column in range(3):
        thread1 = threading.Thread(target = matrixMultiply, args = [row, column, 3])
        #matrixMultiply(row, column, 3)
        threads.append(thread1)
        thread1.start()
        
for thread1 in threads:
    thread1.join()

print(c)
