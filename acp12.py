class Vehicle:
    def __init__(self,taxi_fare):
        self.taxi_fare = taxi_fare

class Bus(Vehicle):
    def __init__(self,taxi_fare):
        self.taxi_fare = taxi_fare

Bus_ride = Bus("Bus and vehicle Ride fare ",50 , 120)
print("bus and taxi ride fare : ", Bus_ride.taxi_fare)
