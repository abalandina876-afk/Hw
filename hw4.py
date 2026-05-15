class Person:

    def init(self, name, age):
        self.name = name
        self.age = age


class Driver(Person):

    def init(self, name, age, driving_license):
        super().init(name, age)
        self.driving_license = driving_license


name = input("name:")
age = input("age:")
dl = input("drivind_license")

driver = Driver(name, age, dl)