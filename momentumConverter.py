mass = int(input("Please enter an object's mass: "))
velocity = int(input("Please enter an object's velocity in m/sec: "))

momentum = mass * velocity
kineticEnergy = (0.5 * mass * pow(velocity,2))

print "Momentum is", momentum       
print "Kinetic energy is", kineticEnergy
