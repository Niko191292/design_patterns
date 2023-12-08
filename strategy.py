from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self, data):
        pass


class ConcreteStrategyA(Strategy):
    def execute(self, data):
        return f"Strategie A mit Daten {data}"


class ConcreteStrategyB(Strategy):
    def execute(self, data):
        return f"Strategie B mit Daten {data}"


class ConcreteStrategyC(Strategy):
    def execute(self, data):
        return f"Strategie C mit Daten {data}"


class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute_strategy(self, data):
        return self._strategy.execute(data)

    def execute_with_specific_strategy(self, data, strategy: Strategy):
        self.set_strategy(strategy)
        return self.execute_strategy(data)


if __name__ == "__main__":
    data = "Beispiel"

    # Kontext mit Strategie A
    context = Context(ConcreteStrategyA())
    print(context.execute_strategy(data))

    # Wechsel zu Strategie B
    context.set_strategy(ConcreteStrategyB())
    print(context.execute_strategy(data))

    # Wechsel zu Strategie C
    context.set_strategy(ConcreteStrategyC())
    print(context.execute_strategy(data))

    print(context.execute_with_specific_strategy(data, ConcreteStrategyA()))
