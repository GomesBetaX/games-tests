# *args (to refer by position)
def add(*numbers):
    list = []
    for n in numbers:
        list.append(n)
    print(sum(list))

add(1, 2, 3, 4, 5)

# *kwargs (to refer by name)
def calculate(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")


calculate(add=3, multiply=5)

class Car():
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Wolkswagen", model="Fox")
print(my_car.make)