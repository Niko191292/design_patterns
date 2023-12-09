from enum import Enum


class Color(Enum):
    ROT = 1
    GRUEN = 2
    BLAU = 3
    GELB = 4
    ORANGE = 5
    VIOLETT = 6
    SCHWARZ = 7
    WEISS = 8


class Vehicle:
    def __init__(self) -> None:
        self.make: str
        self.model: str
        self.color: Color
        self.number_of_doors: int

    def __str__(self):
        return f"Vehicle({self.make}, {self.model}, {self.color.name}, {self.number_of_doors})"


class VehicleBuilder:
    def __init__(self):
        self.vehicle = Vehicle()

    def set_make(self, make):
        self.vehicle.make = make
        return self

    def set_model(self, model: str):
        self.vehicle.model = model
        return self

    def set_color(self, color: Color):
        self.vehicle.color = color
        return self

    def set_number_of_doors(self, number_of_doors):
        self.vehicle.number_of_doors = number_of_doors
        return self

    def build(self):
        return self.vehicle


# Verwendung des Builders
if __name__ == "__main__":
    builder = VehicleBuilder()
    car = (
        builder.set_make("Volkswagen")
        .set_model("Golf")
        .set_color(Color.GELB)
        .set_number_of_doors(4)
        .build()
    )

    print(car)
