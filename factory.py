from abc import abstractmethod


class IVehicle:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def drive(self):
        pass


class Car(IVehicle):
    def drive(self):
        return f"{self.name} is driving on the road."


class Ship(IVehicle):
    def drive(self):
        return f"{self.name} is sailing on the water."


class Plane(IVehicle):
    def drive(self):
        return f"{self.name} is flying in the sky."


class FahrzeugFactory:
    _vehicleTyps = {
        Car: Car,
        Ship: Ship,
        Plane: Plane
    }

    def createVehicle(self, typ, name):
        if typ in self._vehicleTyps:
            return self._vehicleTyps[typ](name)
        else:
            raise ValueError(f"Unknown vehicle: {typ}")


if __name__ == "__main__":
    factory = FahrzeugFactory()

    myCar = factory.createVehicle(Car, "Volkswagen Golf")
    MyShip = factory.createVehicle(Ship, "Big yacht")
    MyPlane = factory.createVehicle(Plane, "Boeing 747")

    print(myCar.drive())
    print(MyShip.drive())
    print(MyPlane.drive())
