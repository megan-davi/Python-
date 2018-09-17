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
    def __init__(self, counter):
       self.counter = 0

# n represents number of elements for fib. sequence
    def sequence(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1   
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    def recursiveCalls(n):
        global counter
        counter = 0
        if n <= 1:
            counter += 1
            return counter
        else:
            return 1 + recursiveCalls(n-1) + recursiveCalls(n - 2)
  

f = Fibonacci(10)

print("Number of recursive iterations:", recursiveCalls(10))
print("Fibonacci sequence:")
for i in range(n):
    print(fibonacci(i))

# complexity of dynamic is O(2^n)
# complexity of non-dynamic is O(n) (linear)
