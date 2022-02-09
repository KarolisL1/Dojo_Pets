from file_pet import Pet

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