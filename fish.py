from animal import animal

class fish(animal):
  def __init__(self, name, species, age, weight,gender, preferred_food, personality):
    super().__init__(name, species, age, weight,gender)
    self.preferred_food = preferred_food
    self.personality = personality

  def make_sound(self, sound = "glub"):
    print(f'*The fish lets out a {sound} upon approach.*')

  def be_friendly(self):
    print(f'*{self.name} swiftly swims around in a circle a few times \n with excitement of potentially coming with you.*')

  def info(self):
    print(f'This is {self.name}, a {self.personality} {self.gender} {self.species}. They are {self.age} \n year(s) old, and {self.weight} pound(s). They love to eat \n {self.preferred_food}.')