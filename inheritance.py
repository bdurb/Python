
class Animal():

  def __init__(self):
    print("Animal created")

  def who_am_i(self):
    print("Animal")

  def eat(self):
    print("Eating")

my_animal = Animal()
my_animal.who_am_i()

class Dog(Animal):

  def __init__(self):
    print("Dog Created")

  def bark(self):
    print("Woof!")

  def eat(self):
    print("Dog Eating")


dog = Dog()
dog.who_am_i()
dog.eat()