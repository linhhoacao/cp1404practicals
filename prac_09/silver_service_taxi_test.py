from silver_service_taxi import SilverServiceTaxi

# Create a SilverServiceTaxi object with name, fuel, price_per_km, and fanciness
my_taxi = SilverServiceTaxi("Hummer", 200, 4.92, 4)  # Fanciness of 4

# Drive the taxi for 18 km
my_taxi.drive(18)

# Calculate and print the fare
fare = my_taxi.get_fare()
print("Fare:", fare)

# Test the fare using an assert statement
expected_fare = 4.92 * 18 + 4.50
assert fare == expected_fare, "Incorrect fare calculation"
print("Fare calculation test passed!")