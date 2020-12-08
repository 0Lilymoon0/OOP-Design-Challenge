from animal import animal

class turtle(animal):
  def __init__(self, name, species, age, weight,gender, preferred_food, personality):
    super().__init__(name, species, age, weight,gender)
    self.preferred_food = preferred_food
    self.personality = personality

  def make_sound(self, sound = "tiny grunt"):
    print(f'*The turtle lets out a {sound} upon approach.*')

  def be_friendly(self):
    print(f'*{self.name} puts their right front foot against the glass, \n aknowledging you.*')

  def info(self):
    print(f'This is {self.name}, a {self.personality} {self.gender} {self.species}. They are \n {self.age} year(s) old, and {self.weight} pound(s). They love to eat \n {self.preferred_food}.')