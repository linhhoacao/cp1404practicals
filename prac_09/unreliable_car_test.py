from unreliable_car import UnreliableCar

# Create an UnreliableCar object with name, fuel, and reliability
my_car = UnreliableCar("Unreliable Car", 100, 50)  # 50% reliability

# Drive the car 50 km (reliability is 50%, so it may or may not drive)
distance_driven = my_car.drive(50)

# Print the distance driven
print("Distance driven:", distance_driven)

# Drive the car 100 km (reliability is 50%, so it may or may not drive)
distance_driven = my_car.drive(100)

# Print the distance driven
print("Distance driven:", distance_driven)