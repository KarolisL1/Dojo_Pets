class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food, pet_name, pet_type, pet_trick):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet(pet_name, pet_type, pet_trick)

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self

class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 0
        self.energy = 0
    
    def sleep(self):
        #increase energy by 25
        self.energy += 25
        return self

    def eat(self):
        #increase energy by 5 and healt by 10
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        #increase healt by 25
        self.health += 5
        return self

    def noise(self):
        return "Barking" #testing this

ninja_1 = Ninja("Ninga", "lastname", "treats", "random food", "dog", "Buldog", "jumping")

print(ninja_1.pet.health)
ninja_1.walk().feed().bathe()
print(ninja_1.pet.health)