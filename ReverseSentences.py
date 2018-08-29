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


s = Stack()
filename = "file.txt"
with open(filename) as f:
  while True:
    c = f.read(1)
    if not c:
        #print("End of file")
        break
    s.push(c)
    if c == ".":
        while s.size() > 0:
            print(s.pop(), end='')
        print()
    
