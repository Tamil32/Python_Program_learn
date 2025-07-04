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
                                                     