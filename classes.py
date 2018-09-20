
# class Dog():

#   species = "mammal"

#   def __init__(self, breed, name):
#     self.breed = breed
#     self.name = name

# mydog = Dog("Lab", "charlie")


class Circle():

  pi = 3.14

  def __init__(self, radius = 1):
    self.radius = radius

  def area(self):
    return self.radius * self.radius * Circle.pi

  def set_radius(self, new_radius):
    self.radius = new_radius

myc = Circle(7)
print(myc.area())
myc.set_radius(45)
print(myc.area())