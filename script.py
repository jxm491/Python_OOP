class Dog:
  def __init__(self, name, breed):
      self.name = name
      self.breed = breed

  def bark(self):
    print("Woof woof")

dog1 = Dog("Bruce", "Scottish Terrior")
dog1.bark()

dog2 = Dog("Freya", "Greyhound")
dog2.bark()