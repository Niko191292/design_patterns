class Light:
    def turn_on(self):
        print("Light ON")

    def turn_off(self):
        print("Light OFF")


class TV:
    def switch_on(self):
        print("TV ON")

    def switch_off(self):
        print("TV OFF")


class SoundSystem:
    def start(self):
        print("Soundsystem ON")

    def stop(self):
        print("Soundsystem OFF")


class SmartHomeFacade:
    def __init__(self):
        self.light = Light()
        self.tv = TV()
        self.sound_system = SoundSystem()

    def watch_movie(self):
        print("\n")
        print("Movie starts...")
        self.light.turn_off()
        self.tv.switch_on()
        self.sound_system.start()
        print("\n")

    def end_movie(self):
        print("\n")
        print("Movie ends...")
        self.light.turn_on()
        self.tv.switch_off()
        self.sound_system.stop()
        print("\n")


if __name__ == "__main__":
    smart_home = SmartHomeFacade()

    smart_home.watch_movie()
    smart_home.end_movie()
