from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        raise NotImplementedError("Observer has to implement the update method")


class Subject:
    def __init__(self):
        self._observers: list[Observer] = []

    def register_observer(self, observer: Observer):
        self._observers.append(observer)

    def unregister_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self, message: str):
        for observer in self._observers:
            observer.update(message)


class Flyer:
    title: str = None
    text: str = None

    def __init__(self, title: str, text: str) -> None:
        self.title = title
        self.text = text

    def __str__(self) -> str:
        return f"\nToday: {self.title}\n{self.text}"


class ConcreteObserverA(Observer):
    def update(self, message: str):
        print(f"ConcreteObserverA got the msg: {message}\n")


class ConcreteObserverB(Observer):
    def update(self, message: str):
        print(f"ConcreteObserverB got the msg: {message}\n")


if __name__ == "__main__":
    subject = Subject()

    observer_a = ConcreteObserverA()
    observer_b = ConcreteObserverB()

    subject.register_observer(observer_a)
    subject.register_observer(observer_b)

    subject.notify_observers(Flyer("Here a Flyer", "Once upon a time.."))

    subject.unregister_observer(observer_a)

    subject.notify_observers("Where is A ?")
