# An abstract class.
class Car:
    def __init__(self, name):
        self.name = name
    # A method can not be used, because it always throws an error.

    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Maruti(Car):
    # Override method of parent class
    def show(self):
        print("you are in maruti class:", self.name)


class Santro(Car):
    def show(self):
        print("you are in santro class", self.name)
# ---------------------------------------------------------------------------


carlist = [Maruti("maruti class is called"),
           Santro("santro class is called"), ]

for li in carlist:
    li.show()
