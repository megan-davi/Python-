import random

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items)-1]

line = Queue()
servicing = []
customerWait = Queue()


class Customer:
    totalTime = 0
    numberOfItems = random.randrange(1,30)
    serviceTime = (numberOfItems * 30) / 60

class Cashier:
    def busy(self):
        if len(servicing) == 0:
            return False
        else:
            return True
    
def oneCashier():
    numberOfCustomers = 0
    while numberOfCustomers < 10:
        line.enqueue(Customer())
        Customer.totalTime += 1

    while not line.isEmpty() & Cashier.busy(False):
        servicing.append(line.dequeue())
    
        #customerWait.peek + 1  
        #numberOfCustomers -= 1
    
    
    print(line.items)
    print(customerWait.items)
    print(servicing.items)

### generate a line of ten customers
##numberOfCustomers = 0
##while numberOfCustomers < 10:
##  line.enqueue(round(random.randrange(1,31) * 0.3, 2))
##  numberOfCustomers += 1
##print(line.items)
##
### scenario 1: 
##while numberOfCustomers > 0:
##    line.dequeue()
##    numberOfCustomers -= 1
##    print(line.items)

oneCashier()





    one cashier

- generate line queue
- add one customer and arrival time
- give customers to service queue and add service time
- finish line when queue < 10

While there are customers AND cashier is not busy
- pop customer off line queue and add to cashier queue
- while service time != 0, subtract 1 from service time
- when service time = 0, pop customer off queue
- accept next customer



- arrivalTime + serviceTime + waitTime = totalTime



