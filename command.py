from abc import ABC, abstractmethod


class Light:
    def turn_on(self):
        print("Light ON")

    def turn_off(self):
        print("Light OFF")


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class TurnOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_on()


class TurnOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_off()


class RemoteControl:
    def submit(self, command: Command):
        command.execute()


if __name__ == "__main__":
    light = Light()

    turn_on_command = TurnOnCommand(light)
    turn_off_command = TurnOffCommand(light)

    remote = RemoteControl()

    remote.submit(turn_on_command)
    remote.submit(turn_off_command)
