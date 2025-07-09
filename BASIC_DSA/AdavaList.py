#✅ Intermediate Array Practice
#2️⃣1️⃣ Find the second largest number in a list.

#2️⃣2️⃣ Remove duplicate elements from a list.

#2️⃣3️⃣ Merge two lists into one.

#2️⃣4️⃣ Create a list from 1 to 10 using range().

#2️⃣5️⃣ Square each number in a list and store it in a new list.

#2️⃣6️⃣ Find the index of an element in a list.

#2️⃣7️⃣ Check if two lists are equal.

#2️⃣8️⃣ Multiply all numbers in a list.

#2️⃣9️⃣ Split a list into two halves.

#3️⃣0️⃣ Swap first and last elements in a list.


# find the largest number in a list

List = [100, 20, 2000, 110, 50, 60, 100, 3, 4, 8]
number = max(List)
print("The largest number in the list is:", number)


#method 2
# loop methods

List = [100, 20, 2000, 110, 50, 60, 100, 3, 4, 8]

largest = List[0]

for i in List:
    if i > largest:
        largest = i
print("The largest number in the list is:", largest)


# method 3
