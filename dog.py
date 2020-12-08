from animal import animal

class dog(animal):
  def __init__(self, name, species, age, weight,gender, preferred_food, personality):
    super().__init__(name, species, age, weight,gender)
    self.preferred_food = preferred_food
    self.personality = personality

  def make_sound(self, sound = "arf"):
    print(f'*The dog lets out an {sound} upon approach.*')

  def be_friendly(self):
    print(f'*{self.name} puts their front paws against the glass \n excitedly, their tail wagging swiftly in delight.*')

  def info(self):
    print(f'This is {self.name}, a {self.personality} {self.gender} {self.species}. \n They are {self.age} year(s) old, and {self.weight} pound(s). They love to \n eat {self.preferred_food}.')