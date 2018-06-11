import pdb
from copy import copy

class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    
    def __repr__(self):
        return f"Human name {self.first} {self.last} age {self.age}"

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(self, Human) and isinstance(other, Human):
            return Human(first="Newborn", last=self.last, age=0)
        return "You can't add that"

    def __mul__(self, count):
        if isinstance(count, int):
            return [copy(self) for i in range(count)]
        return "You can't do that"


j = Human("Jon", "Smith", 23)
k = Human("Linda", "Larsen", 28)

clones = (j * 3)
clones[1].first = "Jessica"
print(clones)
# pdb.set_trace()
