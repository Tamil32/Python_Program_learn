#Definition
#Object-Oriented Programming (OOP) is a programming paradigm based on the concept of “objects”, which contain data (attributes) and methods (functions) to operate on the data. 
# Python is an object-oriented programming language that supports OOP principles.



#Key Concepts
#✅ 1. Class:
#A class is a blueprint or template for creating objects. It defines the structure and behavior of its objects.

#✅ 2. Object:
#An object is an instance of a class. It has its own unique data and can use the methods defined in the class.

#✅ 3. Method:
#A method is a function defined inside a class that operates on its attributes.

#✅ 4. __init__ Method (Constructor):
#The __init__ method is automatically called when an object is created. It initializes the object’s attributes.

#✅ 5. self Keyword:
#Refers to the instance of the class. It is used to access attributes and methods of the class in Python.



#Pillars of OOP
#1️⃣ Encapsulation:
#Binding data and methods into a single unit (class) and restricting direct access to some components. Example: Using private variables.

#2️⃣ Abstraction:
#Hiding the internal details and showing only necessary information. Example: Using abstract classes/methods.

#3️⃣ Inheritance:
#One class (child/derived) can inherit properties and behaviors from another class (parent/base). Promotes code reuse.

#4️⃣ Polymorphism:
#The ability of a method to take many forms. Same method name behaves differently based on context (method overriding/overloading).



# class
# class is a blueprint or template for creating objects. It defines the structure and behavior of its objects

class Students:

# Constructor
    def __init__(self, name, age, weight):
        print("Constructor called")
        self.name = name
        self.age = age
        self.weight = weight

    def eating(self):
        print(f"{self.name} is eating food")

#object creation

student1 = Students("Tamilselvan", 22, 65)  
student2 = Students("kavi", 22, 55)        
student3 = Students("karthik", 22, 75)   

#class object calling

student1.eating() 
student2.eating()
student3.eating()

#output
#Tamilselvan is eating food
#kavi is eating food
#karthik is eating food
    