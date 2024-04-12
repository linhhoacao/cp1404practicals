from car import Car


class Taxi(Car):
    def __init__(self, fuel, name, price_per_km):
        super().__init__(fuel, name)
        self.price_per_km = price_per_km
        self.current_fare_distance = 0

    def __str__(self):
        return super().__str__() + ", price_per_km={}".format(self.price_per_km)

    def get_fare(self):
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        self.current_fare_distance = 0

    def drive(self, distance):
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven

