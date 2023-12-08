from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self, data):
        pass


class ConcreteStrategyA(Strategy):
    def execute(self, data):
        return f"{self.__class__.__name__} with data '{data}'"


class ConcreteStrategyB(Strategy):
    def execute(self, data):
        return f"{self.__class__.__name__} with data '{data}'"


class ConcreteStrategyC(Strategy):
    def execute(self, data):
        return f"{self.__class__.__name__} with data '{data}'"


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
    data = "Example"

    # Strategy A
    context = Context(ConcreteStrategyA())
    print(context.execute_strategy(data))

    # Switch to Strategy B
    context.set_strategy(ConcreteStrategyB())
    print(context.execute_strategy(data))

    # Switch Strategy C
    context.set_strategy(ConcreteStrategyC())
    print(context.execute_strategy(data))

    # Switch and Execute in one Method
    print(context.execute_with_specific_strategy(data, ConcreteStrategyA()))
