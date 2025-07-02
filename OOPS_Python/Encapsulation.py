#📚 Encapsulation — Theory
#✅ Definition:
#Encapsulation is one of the core principles of Object-Oriented Programming (OOP).
#It means binding data (variables) and methods (functions) that operate on that data together into a single unit (a class) and restricting direct access to some parts of an object.

#🔒 Key Points:
#1️⃣ Data Hiding:
#Encapsulation allows you to hide the internal state of an object. This means the internal variables can’t be accessed directly from outside the class.

#2️⃣ Access Modifiers:
#To achieve encapsulation, languages use access modifiers:

#Private: The data can only be accessed within the class.

#Public: The data/method can be accessed from anywhere.

#Protected: Can be accessed within the class and by subclasses.

#3️⃣ Getters and Setters:
#We use getter methods to read private data and setter methods to update private data safely.
#This controls how data is accessed or changed, adding a layer of security and validation.

#4️⃣ Benefits of Encapsulation:
#✅ Security: Protects data from unintended or harmful changes.
#✅ Control: You can validate data before updating it.
#✅ Flexibility: Internal code can be changed without affecting external code.
#✅ Maintenance: Makes code easier to maintain and debug.


class BankAccount:


# creating a constructor

    def __init__(self, Balance):
        self.__Balance = Balance  # Private variable
    
    def deposit(self, amount):
        if amount > 0:
            self.__Balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__Balance:
            self.__Balance -= amount
        else:
            print("Insufficient Balance")

    def get_Balance(self):
        return self.__Balance
    

user = float(input("Enter your balance: "))
 
acc = BankAccount(user)
acc.deposit(15000)
acc.withdraw(2500)
print(acc.get_Balance())    
 
        
    
