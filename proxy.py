from abc import ABC, abstractmethod


class IBroker(ABC):
    @abstractmethod
    def request(self):
        pass


class Broker(IBroker):
    def request(self):
        print("Broker: Do some Stuff")


class Proxy(IBroker):
    def __init__(self, broker: IBroker):
        self._broker = broker

    def request(self):
        if self._check_access():
            self._broker.request()
            self._log_access()

    def _check_access(self):
        print("Proxy: Access Control")
        return True

    def _log_access(self):
        print("Proxy: Logging")


if __name__ == "__main__":
    my_broker = Broker()
    proxy = Proxy(my_broker)
    proxy.request()
