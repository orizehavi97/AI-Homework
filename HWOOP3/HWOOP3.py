class RubberDuck:

    __color: str = "yellow"

    def __init__(self, quack_volume=5):
        print('New RubberDuck created!')
        self.__quack_volume = quack_volume

    @staticmethod
    def squeak():
        print("duck is squeaking...")

    @classmethod
    def get_color(cls):
        return cls.__color

    def boost_volume(self):
        self.__quack_volume *= 2

    @property
    def quack_volume(self):
        return self.__quack_volume

    @quack_volume.setter
    def quack_volume(self, value: int):
        self.__quack_volume = value

    def __str__(self) -> str:
        return f"RubberDuck quack_volume={self.__quack_volume} color={RubberDuck.get_color()}"

    def __del__(self):
        print(f"RubberDuck is being removed!")


if __name__ == "__main__":
    duck = RubberDuck()
    print(duck)  # שימוש ב-__str__
    RubberDuck.squeak()

    duck.quack_volume = 10
    print("🔊 New volume:", duck.quack_volume)

    duck.boost_volume()
    print("🚀 Boosted volume:", duck.quack_volume)

    print("🎨 Default color:", RubberDuck.get_color())