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
        self.dynamicCount = 0
        self.recursiveCount = 0

    def recursive(self, n):
        "Determine fibonacci sequence recursively"
        self.recursiveCount += 1
        if n == 0:  # n represents number of elements for fib. sequence
            return 0
        elif n == 1:
            return 1
        else:
            return self.recursive(n - 1) + self.recursive(n - 2)

    def dynamic(self, n):
        "Determine fibonacci sequence dynamically"
        self.dynamicCount += 1
        values = [0,1]
        for i in range(2,n+1):
          values.append(values[i - 1] + values[i - 2])
        return values[n]



n = 10
f = Fibonacci()

print("Printed recursively")
for i in range(n):
    print(f.recursive(i))

print()
print("Printed dynamically")
for i in range(n):
    print(f.dynamic(i))

print()
print("Number of iterations in recursive function: " + str(f.recursiveCount))
print("Number of iterations in dynamic function: " + str(f.dynamicCount))

'''
Complexity of dynamic is O(2^n) (exponential)
Complexity of non-dynamic is O(n) (linear)
'''
