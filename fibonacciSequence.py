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
    
    def __init__(self):
        "Constructor"
        print("Fibonacci object created.")
        print()

   
    def recursive(self, n):
        "Determine fibonacci sequence recursively"
        if n == 0:      # n represents number of elements for fib. sequence
            return 0   
        elif n == 1:
            return 1
        else:
            return self.recursive(n - 1) + self.recursive(n - 2)

    def iterative(self, n):
        "Determine fibonacci sequence iteratively"
        a, b = 0, 1
        for i in range(0, n):
            a, b = b, a + b
        return a

n = 10
f = Fibonacci()

print("Printed recursively")
for i in range(n):
    print(f.recursive(i))
    
print()
print("Printed iteratively")
for i in range(n):
    print(f.iterative(i))

'''
Complexity of dynamic is O(2^n)
Complexity of non-dynamic is O(n) (linear)
'''





