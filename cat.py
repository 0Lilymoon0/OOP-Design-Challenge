from animal import animal

class cat(animal):
  def __init__(self, name, species, age, weight,gender, preferred_food, personality):
    super().__init__(name, species, age, weight,gender)
    self.preferred_food = preferred_food
    self.personality = personality

  def make_sound(self, sound = "meow"):
    print(f'*The cat lets out a {sound} upon approach.*')

  def be_friendly(self):
    print(f'*{self.name} nuzzles against the glass, trying to show \n affinity towards you.*')

  def info(self):
    print(f'This is {self.name}, a {self.personality} {self.gender} {self.species}. They are {self.age} \n year(s) old, and {self.weight} pound(s). They love to eat {self.preferred_food}.')