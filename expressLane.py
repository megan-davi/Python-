from random import randint

class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()
   
    def size(self):
        return len(self.items)
    
    def getInternalList(self):
        return self.items


class Customer:
    def __init__(self,n):
        self.numberOfItems=n

    # return the data in the form of string
    def __str__(self):
        return str(self.numberOfItems)

    def getNumberOfItems(self):
        return self.numberOfItems


class Expresschecker:
    def __init__(self,n):
        self.numberOfItems=n

    def __str__(self):
        return str(self.numberOfItems)

    def getNumberOfItems(self):
        return self.numberOfItems


def checkOut(Expresschecker):
    items = Expresschecker.getNumberOfItems()
    
    if items <= 10:
        return randint(2, 5)

    if items <= 20:
        return randint(6, 9)

    return randint(10, 14)


Expresschecker = Queue()

totalcheckoutCustomers = 10

    # --- express lane ---

for i in range(totalcheckoutCustomers):
    randomItemsQty = randint(1, 25)      # customer getting between 1-25 items

    customer = Customer(randomItemsQty)

    Expresschecker.enqueue(customer)     # add customer to checkout queue
    

totalTimetaken = 0   # initialize time


totalcheckoutCustomers = Expresschecker.size()   # size of queue


while not(Expresschecker.isEmpty()):
    totalTimetaken += randint(1,5)
    
    expresscustomer = Expresschecker.dequeue()
    
    timeTaken = checkOut(expresscustomer)
    
    totalTimetaken += timeTaken

   

# --- express lane output ---
avgWaitingtime = totalTimetaken/totalcheckoutCustomers

print("Average waiting time for the express customer queue is "+str(avgWaitingtime)+" minutes ")
print("Remaining Custimers in the express customer Queue is: ",Expresschecker.size())

# returns random checkout time, based on number of items

def checkOut(customer):
    items = customer.getNumberOfItems()
    if items <= 10:
        return randint(1, 5)

    if items <= 20:
        return randint(6, 10)

    return randint(11, 15)


    # --- normal lane ---

customersQueue = Queue()

totalCustomers = 20

for i in range(totalCustomers):
    randomItemsQty = randint(1, 25)    # customer getting between 1-25 items

    customer = Customer(randomItemsQty)

    customersQueue.enqueue(customer)   # add customer to checkout queue


totalTimetaken = 0  # initialize time

totalCustomers = customersQueue.size()


while not(customersQueue.isEmpty()):
    totalTimetaken += randint(1,5)

    customer = customersQueue.dequeue()

    timeTaken = checkOut(customer)

    totalTimetaken += timeTaken

   

    # --- normal lane output ---

averageWaitTime = totalTimetaken/totalCustomers

print("Average wait time for the customer queue is " + str(averageWaitTime) + " minutes ")
print("Remaining Customers in the customer Queue is: ", customersQueue.size())
