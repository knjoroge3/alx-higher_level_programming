#!/usr/bin/python3

class Farm:
    def __init__(self, animal_type, number_of_animals, owner, _vet_name, __secret_formula):
        self.animal_type = animal_type
        self.number_of_animals = number_of_animals
        self.owner = owner
        self._vet_name = _vet_name
        self.__secret_formula = __secret_formula
    
    def __str__(self):
        return f"Farm with {self.number_of_animals} {self.animal_type}(s) {self.owner} {self._vet_name} {self.__secret_formula}"


farm1 = Farm("cow", 5, "Kariuki", "Daudi", "method twenty two")
farm2 = Farm("chicken", 10, "Kariuki", "Daudi", "method twenty two")
farm3 = Farm("goat", 7, "Kariuki", "Daudi", "method twenty two")

print(farm1)
print(farm2)
print(farm3)
