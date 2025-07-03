#🔹 Beginner Level
#Create an array and print all elements.

#Find the length of an array.

#Access the first and last element of an array.

#Update the value at a specific index.

#Insert an element at the end of an array.

#Insert an element at the beginning of an array.

#Remove the last element from an array.

#Remove the first element from an array.

#Find the sum of all elements in an array.

#Find the average of array elements.

# 1Create an array and print all elements.

fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(fruit)

# 2Find the length of an array.

amimals = ["cat", "dog", "elephant", "giraffe"]
print("Length of the array:", len(amimals))


# 3Access the first and last element of an array.


Numbers = [10, 20 , 30 , 40 ,50]
print("sline the index", Numbers[0:5])  # Numbers[start:end] → includes start, excludes end.

                                        #Numbers[:] → gets the whole list (shortcut).

                                        #Numbers[0:5] → elements at index 1, 2, 3.

# method 2
# Access specific
Numbers = [100, 200, 300, 400, 500]
print("First element:", Numbers[0])
print("Last element:", Numbers[-1])  # Negative index for last element



# Method 3
# using loop

Numbers = [100, 200, 300, 400, 500]
for i in [1, -1]:
    print(Numbers[i])

# 4Update the value at a specific index.

Vegetables = ["carrot", "banana", "cabbage", "potato"]

Vegetables[1] = "bottle gourd"

print("Before :", Vegetables)


#method2

Vegetables = ["carrot", "banana", "cabbage", "potato"]

Vegetables.append("onion")

print("before", Vegetables)


# method3

Vegetables = ["carrot", "banana", "cabbage", "potato"]

Vegetables.insert(3, "onion")

print("i will insert onion at index 3", Vegetables)


# method4  its for  i will reverse the string

Vegetables = ["carrot", "banana", "cabbage", "potato"]

Vegetables.reverse()

print("reversed list", Vegetables)