from abc import abstractmethod


class IVehicle:
    def __init__(self, name: str):
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
    _myGarage: list[IVehicle] = []

    _vehicleTyps = {
        Car: Car,
        Ship: Ship,
        Plane: Plane
    }

    def createVehicle(self, typ, name):
        if typ in self._vehicleTyps:
            vehicle = self._vehicleTyps[typ](name)
            self._myGarage.append(vehicle)
            return vehicle
        else:
            raise ValueError(f"Unknown vehicle: {typ}")

    def deleteVehicleFromGarage(self, vehicle: IVehicle):
        self._myGarage.remove(vehicle)

    def printGarage(self):
        for vehicle in self._myGarage:
            print(vehicle.drive())


if __name__ == "__main__":
    factory = FahrzeugFactory()

    myCar = factory.createVehicle(Car, "Volkswagen Golf")
    MyShip = factory.createVehicle(Ship, "Big yacht")
    MyPlane = factory.createVehicle(Plane, "Boeing 747")
    factory.deleteVehicleFromGarage(MyShip)
    factory.printGarage()
