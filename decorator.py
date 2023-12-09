class Vehicle:
    def description(self):
        return "This is a vehicle"


class CarDecorator:
    def __init__(self, vehicle: Vehicle):
        self._vehicle = vehicle

    def description(self):
        return self._vehicle.description() + " as a car implementation"


class ElectricDecorator:
    def __init__(self, vehicle: Vehicle):
        self._vehicle = vehicle

    def description(self):
        return self._vehicle.description() + " with an electric engine"


if __name__ == "__main__":
    vehicle = Vehicle()
    print(vehicle.description())

    car = CarDecorator(vehicle)
    print(car.description())

    electric_car = ElectricDecorator(car)
    print(electric_car.description())
