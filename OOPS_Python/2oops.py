#creating class

class Dog():

    species = "Labared"

# Constructor
    def __init__(self, name,):
       self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

# Creating objects

dog_name = input("Enter the dog's name: ")

dog1 = Dog(dog_name)  # Create an instance of Dog with the name provided by the user

print(dog1.name)
       
