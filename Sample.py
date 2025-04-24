class Sample_class:
    value = 2025

    def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place = place
        print("This is constructor" + name + age + place)

    def display_data(self):
        print(
            "Name = "
            + self.name
            + "\n"
            + "Age = "
            + self.age
            + "\n"
            + "Place = "
            + self.place
        )

    @classmethod
    def update_year(cls):
        cls.value = cls.value + 1

    @staticmethod
    def display():
        print("Hello, Welcome!")


x = Sample_class(name="Thasleem", age=str(67), place="MPM")
y = Sample_class(age=str(4), name="Muthu", place="PMuri")
x.display()
x.display_data()
x.update_year()
print(y.value)
