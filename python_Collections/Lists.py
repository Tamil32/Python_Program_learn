# Creating a list

my_list = ["apple", "banana", "cherry", "apple"]
print("My List:", my_list)
print("Type:", type(my_list))
print("Length:", len(my_list))



# Accessing items (using index, starts from 0)
print("First item:", my_list[0])
print("Last item (negative index):", my_list[-1]) # Access from the end

# Slicing (getting a range of items)
print("Items from index 1 to 2:", my_list[1:3]) # cherry is at index 2, 3 is exclusive

# Changing an item
my_list[1] = "blackberry"
print("List after changing item:", my_list)

# Adding items
my_list.append("orange") # Adds to the end
print("List after append:", my_list)
my_list.insert(1, "grape") # Inserts at a specific index
print("List after insert:", my_list)

# Removing items
my_list.remove("cherry") # Removes the first occurrence of the value
print("List after remove:", my_list)
my_list.pop() # Removes and returns the last item
print("List after pop (last item):", my_list)
my_list.pop(0) # Removes and returns item at a specific index
print("List after pop (index 0):", my_list)

# Checking if an item exists
if "apple" in my_list:
    print("Yes, 'apple' is in the list.")

# Iterating through a list
print("\nIterating through the list:")
for item in my_list:
    print(item)



# A User's Shopping Cart on an E-commerce Website

#Why a List? Items are added in the order they are selected, you might want to change the quantity of an item or remove it, and a user can definitely add the same product multiple times.

user_cart = [] 
print("initial cart:", user_cart)

user_cart.append("Laptop")
user_cart.append("Laptop Case")
user_cart.append("Wireless Mouse")
user_cart.append("keyboard")
user_cart.append("Laptop")

print("Cart after adding items:", user_cart)



# User decides to remove 

user_cart.remove("Laptop Case")
print("Cart after removing  Laptop Case:", user_cart)


# Adimin can add a new item to the cart

user_cart[0] = "online order"
print("cart after upgrading item:", user_cart)