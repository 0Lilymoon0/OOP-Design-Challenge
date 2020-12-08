class voicelines:
  @classmethod
  def greeting(cls):
    print("Hello and welcome to Furever Pals, San Francisco's \n newest pet adoption center. As you can guess being \n newer means we have less options to choose from, but \n I hope we can find your perfect new pet regardless.")

  @classmethod
  def animal_of_interest(cls):
    animal_of_interest = ("Which of our animals would you like to look at? We \n currently have a cat, dog, fish, hamster, and turtle \n available: ")
    return animal_of_interest

  @classmethod
  def didnt_catch_that(cls):
    print("I'm sorry, I didn't quite catch that.")

  @classmethod
  def follow_me(cls):
    print ("Alright then, follow me.")

  @classmethod
  def want_to_adopt(cls):
    want_to_adopt = ("So, would you like to adopt this pet? (y/n) ")
    return want_to_adopt

  @classmethod
  def still_looking(cls):
    still_looking = ("Would you still like to look for a pet? \n (y/n) ")
    return still_looking

  @classmethod
  def goodbye1(cls):
    print("Thank you so much for visiting Furever Pals, I hope you have a nice rest of your day and enjoy your new pet.")

  @classmethod
  def goodbye2(cls):
    print("Thank you so much for visiting Furever Pals. I'm sorry \n we couldn't find a pet for you, but I hope you have a \n nice rest of your day.")