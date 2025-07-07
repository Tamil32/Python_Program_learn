#🔟 Sort a list in ascending order.

#1️⃣1️⃣ Sort a list in descending order.

#1️⃣2️⃣ Find the maximum number in a list.

#1️⃣3️⃣ Find the minimum number in a list.

#1️⃣4️⃣ Find the sum of all numbers in a list.

#1️⃣5️⃣ Find the average of numbers in a list.

#1️⃣6️⃣ Print only even numbers from a list.

#1️⃣7️⃣ Print only odd numbers from a list.

#1️⃣8️⃣ Replace the last element in a list with a new number.

#1️⃣9️⃣ Copy a list to a new list.

#2️⃣0️⃣ Clear all elements in a list.



#Ascending order

Numbers = [5, 2, 9, 1, 5, 6, 10, 3, 4, 8]

Shorted_Numbers = sorted(Numbers)


print("Its a given list:", Numbers)
print("Sorted in ascending order:", Shorted_Numbers)

#output:
# Its a given list: [5, 2, 9, 1, 5, 6, 10, 3, 4, 8]
# Sorted in ascending order: [1, 2, 3, 4, 5, 5, 6, 8, 9, 10]


#Descending order

Numbers = [5, 2, 9, 1, 5, 6, 10, 3, 4, 8]

Shorted_Numbers = sorted(Numbers, reverse=True)

print("Its a given list:", Numbers)
print("Sorted in descending order:", Shorted_Numbers)

#output:
# Its a given list: [5, 2, 9, 1, 5, 6, 10, 3, 4, 8]
# Sorted in descending order: [10, 9, 8, 6, 5, 5, 4, 3, 2, 1]



#maximum number 

Numbers = [500000, 200, 9000, 1000, 50, 60, 100, 3, 4, 8]

Max_Number = max(Numbers)

print("Its a given list:", Numbers)
print("Maximum number in the list:", Max_Number)

#output:
# Its a given list: [500000, 200, 9000, 1000, 50, 60, 100, 3, 4, 8]
# Maximum number in the list: 500000


#minimum number

Numbers = [500000, 200, 9000, 1000, 50, 60, 100, 3, 4, 8]

min_Numbers = min(Numbers)

print("Its a given list:", Numbers)
print("Minimum number in the list:", min_Numbers)

#output:
# Its a given list: [500000, 200, 9000, 1000, 50, 60, 100, 3, 4, 8]
# Minimum number in the list: 3



# sum of all numbers

 #for loop


given_List = [1, 20, 30, 40, 5, 6, 7,80,90]

count = 0
for i in given_List:
    count += i

print("Its a given list:", given_List)
print("Sum of all numbers in the list:", count)
#output:
# Its a given list: [1, 20, 30, 40, 5, 6, 7, 80, 90]
# Sum of all numbers in the list: 279


 # while loop

given_List = [1, 20, 30, 40, 5, 6, 7, 80, 90]
count = 0
i = 0
while i < len(given_List):
    count += given_List[i]
    i += 1

print("Its a given list:", given_List)
print("Sum of all numbers in the list:", count)  

#output:
# Its a given list: [1, 20, 30, 40, 5, 6, 7, 80, 90]
# Sum of all numbers in the list: 279


# function method

def sum_of_list(list):
    count = 0
    for i in list:
        count += i
    return count

# calling the function

given_List = [10, 20, 30, 40, 50, 6, 7, 80, 90]
result = sum_of_list(given_List)

print("Its a given list:", given_List)
print("Sum of all numbers in the list:", result)

#output:
# Its a given list: [10, 20, 30, 40, 50, 6, 7, 80, 90]
# Sum of all numbers in the list: 333


# average of numbers OF list

Numbers = [10, 20, 30, 40, 50, 6, 7, 80, 90]

total = sum(Numbers)
count = len(Numbers)

avarage = total / count

print("Its a given list:", Numbers)
print("Average of all numbers in the list:", avarage)

#output:
# Its a given list: [10, 20, 30, 40, 50, 6, 7, 80, 90]
# Average of all numbers in the list: 33.333333333333336

# print only even numbers

Numbers = [10, 22, 33, 44, 55, 66, 77, 88]

for i in Numbers:
    if i % 2 == 0:
        print("Its a given list:", Numbers)
        print("Even number in the list:", i)

#output:
# Its a given list: [10, 22, 33, 44, 55, 66, 77, 88]
# Even number in the list: 10


# print only odd numbers

Numbers = [10, 22, 33, 44, 55, 66, 77, 88]

for i in Numbers:
    if i % 2 != 0:
        print("Its a given list:", Numbers)
        print("Odd number in the list:", i)