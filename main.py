from voicelines import voicelines
from cat import cat
from dog import dog
from fish import fish
from hamster import hamster
from turtle import turtle

class PetShop:

  def __init__(self):
    self.available_animals = {}
    self.add_available_animal()
    self.start()

  def add_available_animal(self):
    Selena = cat("Selena", "calico cat", 1, 10, "female", "tuna", "loving")
    Wuffles = dog("Wuffles", "yorkshire terrier dog", 2, 12, "male", "beef-flavored dog food", "playful")
    Roddy = fish("Roddy", "goldfish", 1/2, 1, "male", "fish flakes", "docile")
    Chipper = hamster("Chipper", "syrian hamster", 3, 5, "male", "sunflower seeds", "hyper")
    Lisa = turtle("Lisa", "box turtle", 30, 2, "female", "fresh vegetables and bugs", "curious")

    self.available_animals = {
      'cat': Selena,
      'dog': Wuffles,
      'fish': Roddy,
      'hamster': Chipper,
      'turtle':  Lisa
    }

  # Animal being cute dialouge
  def pet_intro(self):

    animal_choice = input(voicelines.animal_of_interest()).lower()
    while animal_choice not in self.available_animals:
      print("\n")
      voicelines.didnt_catch_that()
      print("\n")
      animal_choice = input(voicelines.animal_of_interest()).lower()

    print("\n")
    voicelines.follow_me()
    print("\n")
    self.available_animals[animal_choice].make_sound()
    print("\n")
    self.available_animals[animal_choice].info()
    print("\n")
    self.available_animals[animal_choice].be_friendly()

  def start(self):
    voicelines.greeting()
    print("\n")

    self.pet_intro()
    print("\n")

    # Asking for adoption
    adopt = input(voicelines.want_to_adopt()).lower()
    while adopt not in ['y', 'n']:
      print("\n")
      voicelines.didnt_catch_that()
      print("\n")
      adopt = input(voicelines.want_to_adopt()).lower()

    if adopt == "y":
      voicelines.goodbye1()
    else:
      print("\n")
      still_looking = input(voicelines.still_looking()).lower()

      while still_looking not in ['y', 'n']:
        print("\n")
        voicelines.didnt_catch_that()
        print("\n")
        still_looking = input(voicelines.still_looking()).lower()

      if still_looking == 'y':
        self.pet_intro()

        # Asking for adoption
        adopt = input(voicelines.want_to_adopt()).lower()
        while adopt not in ['y', 'n']:
          voicelines.didnt_catch_that()
          print("\n")
          adopt = input(voicelines.want_to_adopt()).lower()

        if adopt == 'n':
          print("\n")
          voicelines.goodbye2()
        else:
          print("\n")
          voicelines.goodbye1()
      else:
        print("\n")
        voicelines.goodbye2()
    
PetShop()

# still_looking = input(voicelines.still_looking())

# still_looking = "y"
# adopt = "n"

# while still_looking == "y" and adopt == "n":

#   if animal_choice == "cat" or animal_choice == "Cat":
#     voicelines.follow_me()
#     print("\n")
#     Selena.make_sound()
#     print("\n")
#     Selena.info()
#     print("\n")
#     Selena.be_friendly()
#     print("\n")
#     adopt = input(voicelines.want_to_adopt())
#     if adopt == "n":
#       print("\n")
#       still_looking = input(voicelines.still_looking())
#       if still_looking == "y":
#         print("\n")
#         animal_choice = input(voicelines.animal_of_interest())
#         print("\n")
#       elif still_looking != "y" and still_looking != "n":
#         while still_looking != "y" and still_looking != "n":
#           print("\n")
#           voicelines.didnt_catch_that()
#           print("\n")
#           still_looking = input(voicelines.still_looking())
#     elif adopt != "n" and adopt != "y":
#       while adopt != "n" and adopt != "y":
#         print("\n")
#         voicelines.didnt_catch_that()
#         print("\n")
#         adopt = input(voicelines.want_to_adopt())
#       print("\n")
#       still_looking = input(voicelines.still_looking())
#       if still_looking == "y":
#         print("\n")
#         animal_choice = input(voicelines.animal_of_interest())
#       elif still_looking != "y" and still_looking != "n":
#         while still_looking != "y" and still_looking != "n":
#           print("\n")
#           voicelines.didnt_catch_that()
#           print("\n")
#           still_looking = input(voicelines.still_looking())
#         animal_choice = input(voicelines.animal_of_interest())


#   elif animal_choice == "dog" or animal_choice == "Dog":
#     voicelines.follow_me()
#     print("\n")
#     Wuffles.make_sound()
#     print("\n")
#     Wuffles.info()
#     print("\n")
#     Wuffles.be_friendly()
#     print("\n")
#     adopt = input(voicelines.want_to_adopt())
#     if adopt == "n":
#       print("\n")
#       still_looking = input(voicelines.still_looking())
#       if still_looking == "y":
#         print("\n")
#         animal_choice = input(voicelines.animal_of_interest())
#         print("\n")
#       elif still_looking != "y" and still_looking != "n":
#         while still_looking != "y" and still_looking != "n":
#           print("\n")
#           voicelines.didnt_catch_that()
#           print("\n")
#           still_looking = input(voicelines.still_looking())
#     elif adopt != "n" and adopt != "y":
#       while adopt != "n" and adopt != "y":
#         print("\n")
#         voicelines.didnt_catch_that()
#         print("\n")
#         adopt = input(voicelines.want_to_adopt())
#   elif animal_choice == "fish" or animal_choice == "Fish":
#     voicelines.follow_me()
#     print("\n")
#     Roddy.make_sound()
#     print("\n")
#     Roddy.info()
#     print("\n")
#     Roddy.be_friendly()
#     print("\n")
#     adopt = input(voicelines.want_to_adopt())
#     if adopt == "n":
#       print("\n")
#       still_looking = input(voicelines.still_looking())
#       if still_looking == "y":
#         print("\n")
#         animal_choice = input(voicelines.animal_of_interest())
#         print("\n")
#       elif still_looking != "y" and still_looking != "n":
#         while still_looking != "y" and still_looking != "n":
#           print("\n")
#           voicelines.didnt_catch_that()
#           print("\n")
#           still_looking = input(voicelines.still_looking())
#     elif adopt != "n" and adopt != "y":
#       while adopt != "n" and adopt != "y":
#         print("\n")
#         voicelines.didnt_catch_that()
#         print("\n")
#         adopt = input(voicelines.want_to_adopt())
#   elif animal_choice == "hamster" or animal_choice == "Hamster":
#     voicelines.follow_me()
#     print("\n")
#     Chipper.make_sound()
#     print("\n")
#     Chipper.info()
#     print("\n")
#     Chipper.be_friendly()
#     print("\n")
#     adopt = input(voicelines.want_to_adopt())
#     if adopt == "n":
#       print("\n")
#       still_looking = input(voicelines.still_looking())
#       if still_looking == "y":
#         print("\n")
#         animal_choice = input(voicelines.animal_of_interest())
#         print("\n")
#       elif still_looking != "y" and still_looking != "n":
#         while still_looking != "y" and still_looking != "n":
#           print("\n")
#           voicelines.didnt_catch_that()
#           print("\n")
#           still_looking = input(voicelines.still_looking())
#     elif adopt != "n" and adopt != "y":
#       while adopt != "n" and adopt != "y":
#         print("\n")
#         voicelines.didnt_catch_that()
#         print("\n")
#         adopt = input(voicelines.want_to_adopt())
#   elif animal_choice == "turtle" or animal_choice == "Turtle":
#     voicelines.follow_me()
#     print("\n")
#     Lisa.make_sound()
#     print("\n")
#     Lisa.info()
#     print("\n")
#     Lisa.be_friendly()
#     print("\n")
#     adopt = input(voicelines.want_to_adopt())
#     if adopt == "n":
#       print("\n")
#       still_looking = input(voicelines.still_looking())
#       if still_looking == "y":
#         print("\n")
#         animal_choice = input(voicelines.animal_of_interest())
#         print("\n")
#       elif still_looking != "y" and still_looking != "n":
#         while still_looking != "y" and still_looking != "n":
#           print("\n")
#           voicelines.didnt_catch_that()
#           print("\n")
#           still_looking = input(voicelines.still_looking())
#     elif adopt != "n" and adopt != "y":
#       while adopt != "n" and adopt != "y":
#         print("\n")
#         voicelines.didnt_catch_that()
#         print("\n")
#         adopt = input(voicelines.want_to_adopt())
#   else:
#     voicelines.didnt_catch_that()
#     print("\n")
#     animal_choice = input(voicelines.animal_of_interest())
#     print("\n")

# print("\n")
# if adopt == "y":
#  voicelines.goodbye1()
# elif adopt == "n":
#  voicelines.goodbye2()