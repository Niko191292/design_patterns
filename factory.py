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


class Garage():
    _vehicles: list[Vehicle] = []

    def deliverVehicleToGarage(self, vehicle: Vehicle):
        self._vehicles.append(vehicle)

    def deleteVehicleFromGarage(self, vehicle: Vehicle):
        self._vehicles.remove(vehicle)

    def printGarage(self):
        for vehicle in self._vehicles:
            print(vehicle.drive())

            if hasattr(vehicle, 'spez'):
                print(vehicle.spez())


class VehicleFactory:
    _legitTypes = [Car, Ship, Plane, Jet]
    _deliverTo: Garage

    def setDelivery(self, garage: Garage):
        self._deliverTo = garage

    def createVehicle(self, typ: type, name: str) -> Vehicle:
        if (typ in self._legitTypes):
            vehicle = typ(name)
            self._deliverTo.deliverVehicleToGarage(vehicle)
            return vehicle
        else:
            raise NotImplementedError(f"Unknown vehicle: {typ}")


if __name__ == "__main__":
    factory = VehicleFactory()
    myGarage = Garage()

    factory.setDelivery(myGarage)

    myCar = factory.createVehicle(Car, "Volkswagen Golf")
    MyShip = factory.createVehicle(Ship, "Big yacht")
    MyPlane = factory.createVehicle(Plane, "Boeing 747")
    MyJet = factory.createVehicle(Jet, "F-12")

    myGarage.deleteVehicleFromGarage(MyShip)
    myGarage.printGarage()
