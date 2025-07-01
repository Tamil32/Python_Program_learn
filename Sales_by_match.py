n = 7
ar = [1, 2, 1, 2, 1, 3, 2]

def sockMerchant(n, ar):
    color_count = {}  # 1️⃣ Create empty dictionary to store sock colors
    pairs = 0         # 2️⃣ Initialize pairs count to zero

    for sock in ar:   # 3️⃣ Loop through each sock in the array
        if sock in color_count:
            color_count[sock] += 1  # If sock color exists, increase count
        else:
            color_count[sock] = 1   # If sock color is new, start with 1

    for count in color_count.values():  # 4️⃣ Loop through all color counts
        pairs += count // 2             # Integer division: count // 2 gives pairs

    return pairs  # 5️⃣ Return total pairs

retun = sockMerchant(n, ar)  # Call the function with n and ar
print(retun)  # Print the result

# Output: 2
# This code counts the number of pairs of socks with the same color.
