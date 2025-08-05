#!/usr/bin/python3

class Farm:

    def __init__(self, animal_type, feeds):
        self.animal_type = animal_type
        self.feeds = feeds

    def describe(self):
        print("This farm has {} and they eat {}".format(self.animal_type, self.feeds))

farm1 = Farm("goats", "grass")
farm2 = Farm("Pigs", "sow and weaner")

farm1.describe()
farm2.describe()
