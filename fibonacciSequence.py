'''

Prompt: 
Write a Python class with methods that use recursion to calculate
the Fibonacci number sequence with and without dynamic programming.
Include a count of how many times the recursive function is called to
show how dynamic programming improves the performance.
What is the complexity of the algorithm with and without
dynamic programming?

'''


class Fibonacci:
    def __init__(self, n):
       #self.counter = 0
       self.n = n


    def fibonacci(self):
        "Determine fibonacci sequence recursively"
        if self.n == 0:      # n represents number of elements for fib. sequence
            return 0
        elif self.n == 1:
            return 1   
        else:
            return fibonacci(self.n-1) + fibonacci(self.n-2)

    def print(self):
        for i in range(self.n):
            return print(self.fibonacci(i))
        
        

##print("Fibonacci sequence:")
##i = fibonacci()
##    for i in range(n):
##    print(fibonacci(i))


##    def recursiveCalls(n):
##        "Determine number of recursive calls for fib sequence"
##        global counter
##        counter = 0
##        if n <= 1:
##            counter += 1
##            return counter
##        else:
##            return 1 + recursiveCalls(n-1) + recursiveCalls(n - 2)
  

f = Fibonacci(10)
Fibonacci.print(10)


#print("Number of recursive iterations:", recursiveCalls(10))

#Fibonacci()




##n = 10
##def fibonacci(n):
##    "Determine fibonacci sequence recursively"
##    if n == 0:      # n represents number of elements for fib. sequence
##        return 0
##    elif n == 1:
##        return 1   
##    else:
##        return fibonacci(n-1) + fibonacci(n-2)
##
##
##print("Fibonacci sequence:")
##for i in range(n):
##    print(fibonacci(i))


'''
Complexity of dynamic is O(2^n)
Complexity of non-dynamic is O(n) (linear)
'''
