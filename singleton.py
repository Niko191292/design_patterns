class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Create the instance")
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class car:
    name = None


if __name__ == "__main__":
    singleton1 = Singleton()
    singleton2 = Singleton()

    print(singleton1 == singleton2)  # True
