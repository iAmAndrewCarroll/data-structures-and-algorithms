from data_structures.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.queue = []

    def enqueue(self, animal):
        if animal.species == "dog":
            self.queue.append(animal)
        elif animal.species == "cat":
            self.queue.append(animal)
        else:
            raise ValueError("Animal must be a dog or a cat")

    def dequeue(self, pref):
        if pref == "dog":
            for animal in self.queue:
                if animal.species == "dog":
                    self.queue.remove(animal)
                    return animal
        elif pref == "cat":
            for animal in self.queue:
                if animal.species == "cat":
                    self.queue.remove(animal)
                    return animal
        else:
            return None

class Dog:
    def __init__(self):
        self.species = "dog"

class Cat:
    def __init__(self):
        self.species = "cat"

