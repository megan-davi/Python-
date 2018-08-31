class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def divideBy2(decimal):
    rstack = Stack()    # remainder stack

    while decimal > 0:
        remainder = decimal % 2
        rstack.push(remainder)
        decimal = decimal // 2

    binary = ""
    while not rstack.isEmpty():
        binary = binary + str(rstack.pop())
    return binary

print(divideBy2(42))
