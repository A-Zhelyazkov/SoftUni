class Zoo:
    def __init__(self, name, budget, animal_capacity, worker_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        if self.__budget <= price and self.__animal_capacity > len(self.animals):
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = sum([w.salary for w in self.workers])

        if self.__budget >= salaries:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        costs = sum([a.money_for_care for a in self.animals])

        if self.__budget >= costs:
            self.__budget -= costs
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        lions = [l for l in self.animals if l.__class__.__name__ == "Lion"]
        cheetahs = [c for c in self.animals if c.__class__.__name__ == "Cheetah"]
        tigers = [t for t in self.animals if t.__class__.__name__ == "Tiger"]

        result += f"----- {len(lions)} Lions:"
        for l in lions:
            result += f"\n{l}"

        result += f"\n----- {len(tigers)} Tigers:"
        for t in tigers:
            result += f"\n{t}"

        result += f"\n----- {len(cheetahs)} Cheetahs:"
        for c in cheetahs:
            result += f"\n{c}"

        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        keepers = [w for w in self.workers if w.__class__.__name__ == "Keeper"]
        caretakers = [w for w in self.workers if w.__class__.__name__ == "Caretaker"]
        vets = [w for w in self.workers if w.__class__.__name__ == "Vet"]

        result += f"----- {len(keepers)} Keepers:"
        for k in keepers:
            result += f"\n{k}"

        result += f"\n----- {len(caretakers)} Caretakers:"
        for c in caretakers:
            result += f"\n{c}"

        result += f"\n----- {len(vets)} Vets:"
        for v in vets:
            result += f"\n{v}"

        return result







