from file_ninja import Ninja

ninja_1 = Ninja("Ninga", "lastname", "treats", "random food", "dog", "Buldog", "jumping")

print(ninja_1.pet.health)
ninja_1.walk().feed().bathe()
print(ninja_1.pet.health)