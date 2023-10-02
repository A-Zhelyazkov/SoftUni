class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        if species == "fish":
            self.fishes.append(name)
        if species == "bird":
            self.birds.append(name)

        zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            return f"Mammals in {zoo_name}: {', '.join(self.mammals)}\nTotal animals: {self.__animals}"
        if species == "fish":
            return f"Fishes in {zoo_name}: {', '.join(self.fishes)}\nTotal animals: {self.__animals}"
        if species == "bird":
            return f"Birds in {zoo_name}: {', '.join(self.birds)}\nTotal animals: {self.__animals}"


zoo_name = input()
n = int(input())
zoo = Zoo(zoo_name)
for _ in range(n):
    animal = input().split()
    species = animal[0]
    animal_name = animal[1]
    zoo.add_animal(species, animal_name)

species_info = input()
print(zoo.get_info(species_info))
