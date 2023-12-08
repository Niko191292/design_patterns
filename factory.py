from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def drive(self):
        pass


class Car(Vehicle):
    def drive(self):
        return f"{self.name} is driving on the road."

    def spez(self):
        return f"{self.name} special ability"


class Ship(Vehicle):
    def drive(self):
        return f"{self.name} is sailing on the water."


class Plane(Vehicle):
    def drive(self):
        return f"{self.name} is flying in the sky."


class Jet(Vehicle):
    def drive(self):
        return f"{self.name} is flying very very fast in the sky."

    def spez(self):
        return f"{self.name} makes a looping."


class VehicleFactory:
    _myGarage: list[Vehicle] = []

    _legitTypes = [Car, Ship, Plane, Jet]

    def createVehicle(self, typ: type, name: str) -> Vehicle:
        if (typ in self._legitTypes):
            vehicle = typ(name)
            self._myGarage.append(vehicle)
            return vehicle
        else:
            raise NotImplementedError(f"Unknown vehicle: {typ}")

    def deleteVehicleFromGarage(self, vehicle: Vehicle):
        self._myGarage.remove(vehicle)

    def printGarage(self):
        for vehicle in self._myGarage:
            print(vehicle.drive())

            if hasattr(vehicle, 'spez'):
                print(vehicle.spez())


if __name__ == "__main__":
    factory = VehicleFactory()

    myCar = factory.createVehicle(Car, "Volkswagen Golf")
    MyShip = factory.createVehicle(Ship, "Big yacht")
    MyPlane = factory.createVehicle(Plane, "Boeing 747")
    MyJet = factory.createVehicle(Jet, "F-12")

    factory.deleteVehicleFromGarage(MyShip)
    factory.printGarage()
