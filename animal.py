class animal:
  def __init__(self, name, species, age, weight, gender):
    self.name = name
    self.species = species
    self.age = age
    self.weight = weight
    self.gender = gender

  def make_sound(self, sound = "sound"):
    print(f'The animal lets out a {sound} upon approach.')

  def info(self):
    print(f'This is {self.name}, a {self.gender}{self.species}. They are {self.age} years old, and {self.weight} pounds.')