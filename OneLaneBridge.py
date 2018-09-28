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
                    format='(%(threadName)s) %(message)s',
                    )

class OneLaneBridge():
    def __init__(self):
        self.cars = 0
        self.bridgeBusy = False
        self.left = threading.Condition()   # monitor
        self.right = threading.Condition()  # monitor
        self.mutex = threading.Lock()

    def car(self):
        print()
        logging.debug("Starting")
        
        driveUp = round(uniform(0, 0.015), 3) # convert s to ms for sleep function
        time.sleep(driveUp)
        msg = "Car took %s ms to drive to bridge" %round(driveUp * 1000) # convert back so it is easy to read
        logging.debug (msg)
        
        self.left.acquire()
        self.mutex.acquire()
        if self.cars == 0:
            self.left.acquire()
            self.left.notify()
            self.left.release()
        self.mutex.release()
        self.left.release()
        logging.debug("Exiting")


bridge = OneLaneBridge()          
c1 = threading.Thread(name = 'Car 1', target = bridge.car)
c2 = threading.Thread(name = 'Car 2', target = bridge.car)
c3 = threading.Thread(name = 'Car 3', target = bridge.car)
c4 = threading.Thread(name = 'Car 4', target = bridge.car)
c5 = threading.Thread(name = 'Car 5', target = bridge.car)
c6 = threading.Thread(name = 'Car 6', target = bridge.car)
c7 = threading.Thread(name = 'Car 7', target = bridge.car)
c8 = threading.Thread(name = 'Car 8', target = bridge.car)
c9 = threading.Thread(name = 'Car 9', target = bridge.car)
c10 = threading.Thread(name = 'Car 10', target = bridge.car)

c1.start()
c2.start()
c3.start()
c4.start()
c5.start()
c6.start()
c7.start()
c8.start()
c9.start()
c10.start()
