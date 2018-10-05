"""
Prompt:
Write a multi-threaded Python program to simulate a one-lane
bridge with traffic coming from both directions.
Each car should consist of a thread. There should be 20 cars total.
The bridge can hold a maximum of 4 cars at one time.
Half of the cars should following pattern.
1. Drive to the bridge for a random time between 0 and 15 ms
(time.sleep()).
2. Cross the bridge right to left for a random time of 3 to 10
ms.
3. Drive in a loop to turn around for a random time between 5 and
15 ms.
4. Cross the bridge left to right for a random time of 3 to 10 ms.
5. Repeat the first four steps 5 times.
The other ten cars will do the same, except they will first cross
left to rightand then right to left after turning around. The program
should report the number of cars on the bridge and their direction
whenever a car exits from the bridge.
"""

import threading
import logging
import time
from random import uniform, random

logging.basicConfig(level=logging.DEBUG,
                    format='[%(threadName)s] %(message)s',
                    )

class OneLaneBridge():
    def __init__(self):
        self.carNumber = 0
        self.leftOK = threading.Condition()   # monitor
        self.rightOK = threading.Condition()  # monitor
        self.mutex = threading.Lock()

    def busy(self):
        return True if self.carNumber > 0 else False

    def leftCar(self):
        print()
        logging.debug("Starting")

        # car drives to bridge
        driveUp = round(uniform(0, 0.015), 3) # convert s to ms for sleep function
        time.sleep(driveUp)
        msg = "Car took %s ms to drive to bridge" %round(driveUp * 1000) # convert back so it is easy to read
        logging.debug (msg)

        # car drives across bridge
        self.leftOK.acquire()
        self.mutex.acquire()
        
        while self.busy == False or self.carNumber > 0:
            self.mutex.release()
            self.leftOK.wait()
            self.mutex.acquire()
        while self.carNumber < 4:
            self.carNumber = self.carNumber + 1
        self.mutex.release()
        self.leftOK.notify()
        self.leftOK.release()
        # Once one car can cross, 3 follow
        #----------------------------
        # critical section
        #----------------------------
        driveAcross = round(uniform(0.003, 0.013), 3) # convert s to ms
        msg = "Car took %s ms to drive across bridge 1st time" %round(driveAcross * 1000)
        logging.debug (msg)
        #----------------------------
        # end critical section
        #----------------------------
        self.leftOK.acquire()
        self.mutex.acquire()
        while self.carNumber != 0:
            self.carNumber = self.carNumber - 1
        if self.carNumber == 0:
            self.leftOK.acquire()
            self.leftOK.notify()
            self.leftOK.release()
        self.mutex.release()
        self.leftOK.release()
         
        logging.debug("Exiting")

    def rightCar(self):
        logging.debug("Starting")
        
        driveUp = round(uniform(0, 0.015), 3) # convert s to ms for sleep function
        time.sleep(driveUp)
        msg = "Car took %s ms to drive to bridge" %round(driveUp * 1000) # convert back so it is easy to read
        logging.debug (msg)

        logging.debug("Exiting")




def main():
    bridge = OneLaneBridge() # call class 

    carList = [] # create empty list for cars

    carID = 1
    # create 20 cars, 10 from the left and 10 from the right; start cars
    for i in range(10):
        car = threading.Thread(target = bridge.leftCar, name = ("Car %s" % carID))
        carList.append(car)
        carID += 1
        car.start()
    for i in range(10):
        car = threading.Thread(target = bridge.rightCar, name = ("Car %s" % carID))
        carList.append(car)
        carID += 1
        car.start()

    # cars can run without waiting for the others to finish
    for car in carList:
        car.join()



if __name__ == "__main__":
    main()

