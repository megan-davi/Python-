__author__ = "Megan"

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

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
        "adds item to opposite end of list that add() does"
        current = self.head
        while current.getNext() != None:
            current = current.getNext()
        temp = Node(item)
        temp.setNext(current.getNext())
        current.setNext(temp)

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
        if current == None:
            print ("Index out of range - insertion failed")

    
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


    def remove_list_item_by_id(self, item_id):
        "remove the list item with the item id"

        current_id = 1
        current_node = self.head
        previous_node = None

        while current_node is not None:
            if current_id == item_id:
                # if this is the first node (head)
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                    # we don't have to look any further
                    return

            # needed for the next iteration
            previous_node = current_node
            current_node = current_node.next
            current_id = current_id + 1

        return

    def removeNode2(self, item):
        self.head.getNext = self.head.getNext.getNext
        return self
        


    def removeNode(self, item):
        head = self.head

        if (head is not None):
            if (head.data == item):
                self.head = head.next
                head = None
                return
        while (head is not None):
            if head.data == item:
                break
            prev = head
            head = head.next
        if (head == None):
            return
        prev.next = head.next
        head = None
        
    # pop item off end of list
    #def pop(pos=None)
     #   if pos = None:
      #      should be the last item in the list
      # pop should pop off the end not the head

# --- OUTPUT ----
myList = UnorderedList()
print ("List creation:")
myList.add(1)
print ("Added", 1)
myList.add(2)
print ("Added", 2)
myList.add(3)
print ("Added", 3)
myList.append(4)
print ("Appended", 4)
myList.insert(2, "new")
print ("Inserted", "'new' @ index:", 2)
myList.remove(2)
print ("Removed", 2)
print ()
print ("List Output:" )
print (myList.listPrint())
print ()
print ("Size of list is:", myList.size())
print ("Index of number 4 is:", myList.index(4))
