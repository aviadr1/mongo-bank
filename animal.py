from dataclasses import dataclass

@dataclass
class Animal:
    species: str

@dataclass
class Dog(Animal):
    name: str
    color: str

    def eat_dog_food(self):
        print('yummy!')

@dataclass
class TV:
    color: str

elephant = Animal(species='elephant')
poodle = Dog(species='dog', name='rexi', color='black')

tv = TV(color='black')

print(elephant)
print(poodle)
print(tv)

things = [elephant, poodle, tv]
for thing in things:
    if isinstance(thing, Animal):
        print(thing, 'what should I give you to eat')

    if isinstance(thing, Dog):
        thing.eat_dog_food()


