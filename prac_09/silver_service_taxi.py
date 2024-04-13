from taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, price_per_km, fanciness):
        super().__init__(name, fuel, price_per_km)
        self.fanciness = fanciness

    def get_fare(self):
        return super().get_fare() + self.flagfall

    def __str__(self):
        return super().__str__() + ", plus flagfall of ${:.2f}".format(self.flagfall)