from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def handle(self, context):
        pass


class OnState(State):
    def handle(self, context: State):
        context.state = OffState()
        print("Light ON")


class OffState(State):
    def handle(self, context: State):
        context.state = OnState()
        print("Light OFF")


class LightSwitch:
    def __init__(self):
        self.state = OffState()
        self.switch()

    def switch(self):
        self.state.handle(self)


if __name__ == "__main__":
    light_switch = LightSwitch()

    light_switch.switch()
    light_switch.switch()
