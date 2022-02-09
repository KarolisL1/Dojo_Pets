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
