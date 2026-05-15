class Pet:
    def __init__(self, name, animal):
        self.name = name
        self.animal = animal
        self.hunger = 5
        self.energy = 5
        self.happiness = 5

    def eat(self):
        self.hunger -= 2
        self.happiness += 1
        print(f"{self.name} is eating and feels full.")

    def sleep(self):
        self.energy += 3
        print(f"{self.name} is sleeping and resting.")

    def play(self):
        self.energy -= 2
        self.happiness += 2
        print(f"{self.name} is playing and having fun.")

    def status(self):
        print("\nPet status:")
        print("Name:", self.name)
        print("Animal:", self.animal)
        print("Hunger:", self.hunger)
        print("Energy:", self.energy)
        print("Happiness:", self.happiness)

pet1 = Pet("Milo", "Cat")

pet1.status()
pet1.eat()
pet1.play()
pet1.sleep()
pet1.status()