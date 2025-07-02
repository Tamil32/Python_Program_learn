# Inheritance 

#📚 Inheritance in Object-Oriented Programming (OOP)

#✅ Definition
#Inheritance is one of the four fundamental principles of Object-Oriented Programming (OOP),
#  along with Encapsulation, Polymorphism, and Abstraction.

#Inheritance allows a new class (child or subclass) to acquire the properties and behaviors (methods and attributes) of an existing class (parent or superclass).
#This promotes code reusability, extensibility, and hierarchical classification.

#🔑 Key Points
#1️⃣ Parent (Super) Class: The class whose properties and methods are inherited.
#2️⃣ Child (Sub) Class: The class that inherits the parent’s features. 
 #  It can also have its own additional properties and methods.
#3️⃣ Reusability: Inheritance enables code written once in the parent class to be reused in multiple child classes.
#4️⃣ Method Overriding: A child class can provide its own implementation of a method defined in the parent class.
 #  This supports polymorphism.
#5️⃣ Hierarchical Relationship: Inheritance forms an “is-a” relationship.
 #  For example, a Dog is an Animal.


#🗂️ Types of Inheritance
#Single Inheritance: A child class inherits from one parent class.

#Multiple Inheritance: A child class inherits from more than one parent class (supported in some languages like Python; not directly in Java).

#Multilevel Inheritance: A class inherits from a child class, creating a chain. (e.g., Grandparent → Parent → Child)

#Hierarchical Inheritance: Multiple child classes inherit from one parent class.


#parent class

class Telepjone:
    def call (self):
        print("call using telephonr......")
        print("Wired__")


#child class

class Mobile(Telepjone):
    def massage(self):
        print("send message using mobile......")
        print("Wireless__")


#Another cihld class


class Smartphone(Mobile):
    def Internet(self):
        print("use internet to browesing......")
    
    def call (self):
        print("5G_")


# Creating objects of the classes

using = Smartphone()

using.massage()
using.Internet()
using.call()


