
arr = [1, 2, 3, 4, 5]        # Example array with numbers

def simpleArraySum(arr):
    total = 0                # 1️⃣ Initialize total sum as 0

    for num in arr:          # 2️⃣ Loop through each number in the array
        total += num         # 3️⃣ Add the current number to the total sum

    return total             # 4️⃣ Return the total sum

result = simpleArraySum(arr) # 6️⃣ Call the function and store the result
print(result)                # 7️⃣ Print the result (should be 15)

# Output: 15
# This code calculates the sum of all elements in the array.