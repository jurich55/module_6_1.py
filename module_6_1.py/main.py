class Animal:
    alive = True
    fed = False
    def __init__(self, name):
        self.name = name
    def eat(self, food):
        if food.edible == True:
            Animal.fed = True
            print(f'{self.name} съел {food.name}')
        else:
            Animal.alive = False
            print(f'{self.name} не стал есть {food.name}')

class Plant:
    edible = False
    def __init__(self, name):
        self.name = name
class Mammal(Animal):
    pass
class Predator(Animal):
    pass
class Flower(Plant):
    edible = False

class Fruit(Plant):
    edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Завадной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# class Animal:
#     alive = True  # жив
#     fed = False  # сыт
#     def __init__(self, name):
#         self.name = name
#
# class Mammal(Animal):
#     def eat(self, food):
#         self.food = food
#         if food.edible == True:   # если еда съедобная
#             Animal.fed = True     # животное - сытое
#             print(f'{self.name} съела {food.name}')
#         else:
#             Animal.fed = False    # животное - голодное
#             print(f'{self.name} не стала есть {food.name}')
#
#
# class Predator(Animal):
#     def eat(self, food):
#         self.food = food
#         if food.edible == True:   # если еда съедобная
#             Animal.fed = True     # животное - сытое
#             print(f'{self.name} съел {food.name}')
#         else:
#             Animal.alive = False   # животное - погибло
#             print(f'{self.name} не стал есть {food.name}')
#
# class Plant:
#     edible = False    # не съедобный
#     def __init__(self, name):
#         self.name = name
#
# class Flower(Plant):
#     edible = False   # не съедобный
#
# class Fruit(Plant):
#     edible = True    # съедобный
#
# a1 = Predator('Шерхан')
# a2 = Mammal('Буренка')
# p1 = Flower('Цветик семицветик')
# p2 = Fruit('Зеленый апельсин')
#
# print(a1.name)
# print(p1.name)
#
# print(a1.alive)
# print(a2.fed)
# a1.eat(p1)
# a2.eat(p2)
# print(a1.alive)
# print(a2.fed)
# """ Нужно попробовать метод  ==def eat(self, food)== вставить в родительский класс, а из дочерних  - убрать!!:
#  - код будет короче"""

