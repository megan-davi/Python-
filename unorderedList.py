__author__ = "Megan"

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        self.prev = None
    
    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        "constructor"
        self.head = None
        self.tail = None

    def __iter__(self):
        "prints the list"
        node = self.head
        while node:
            yield node
            node = node.next

    def listPrint(self):
        "prints list"
        printVal = self.head
        while printVal is not None:
            print(printVal.data)
            # jump to the linked node
            printVal = printVal.next 

    def isEmpty(self):
        "tests if list is empty"
        return self.head == None

    def add(self,item):
        "adds item to end of list"
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        print ("Added", item)

    def size(self):
        "returns the number of list items"
        current = self.head
        count = 0
        while current != None:
            # increase counter by one
            count = count + 1
            # jump to the linked node
            current = current.getNext() 
        return count


    def search(self,item):
        "searches for item"
        # define current node
        current = self.head 
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                # jump to linked node
                current = current.getNext() 
        return found

    def append(self, item):
        "adds item to tail end of list"
        if self.size == 0:
            temp = Node(item)
            temp.setNext(self.head)
            self.head = temp
            print ("List was empty, item added instead of appended")
            return
        else:
            current = self.head
            while current.getNext() != None:
                current = current.getNext()
            temp = Node(item)
            temp.setNext(current.getNext())
            current.setNext(temp)
            print ("Appended", item)

    def index(self, item):
        "determine index of item"
        index = 0
        current = self.head
        found = False
        while current != None:
            if current.getData() == item:
                found = True
                break
            else:
                current = current.getNext()
                index += 1
        if not found:
            index = None
        return index

    def insert(self, index, item):
        "insert item based on index"
        current = self.head
        for i in range(index):
            current = current.getNext()

        if current != None:
            temp = Node(item)
            temp.setNext(current.getNext())
            current.setNext(temp)
            print ("Inserted", item, "@ index:", 2)
            return True
        if current == None:
            print ("Index out of range - insertion failed")
            return False

    def remove(self,item):
        "remove the list item"
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            print ("Removed", item)

    def pop(self):
        "pops item off list"
        current = self.head
        previous = None
        while current != None:
            if current.getNext() == None:
                if previous != None:
                    previous.setNext(None)
                else:
                    self.head = None
                self.size -= 1
                return current.getData()
            previous = current
            current = current.getNext()
       
    def popNode(self, index):
        "pops item off list based on index"
        prev = None
        node = self.head
        i = 0

        while ( node != None ) and ( i < index ):
            prev = node
            node = node.next
            i += 1

        if prev == None:
            self.head = node.next
            print ("Popped at index", index)
        else:
            print ("Index does not exist, pop failed")
            return None
            

    def bubbleSort(self):
        return None


bubble = UnorderedList()

print ("List creation:")
bubble.add(50)
bubble.add(80)
bubble.add(70)
bubble.add(10)
bubble.add(20)
bubble.add(90)
bubble.add(40)
bubble.add(100)
bubble.add(30)
print()
print([item.data for item in bubble])

bubble.bubbleSort()
print([item.data for item in bubble])


    
    

