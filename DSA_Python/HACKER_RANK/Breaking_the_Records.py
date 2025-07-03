def breakingRecords(scores):
    # Step 1: Initialize the high and low scores with the first score
    high = scores[0]
    low = scores[0]

    # Step 2: Counters for how many times records are broken
    high_breaks = 0
    low_breaks = 0

    # Step 3: Loop through scores starting from the second score
    for score in scores[1:]:
        # Step 4: Check if the current score is higher than the current high score
        if score > high:
            high = score            # Update high score
            high_breaks += 1       # Increment high break counter

        # Step 5: Check if the current score is lower than the current low score
        elif score < low:
            low = score            # Update low score
            low_breaks += 1        # Increment low break counter

    # Step 6: Return the counts of record-breaking highs and lows
    return [high_breaks, low_breaks]

# Step 7: Example usage
scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
result = breakingRecords(scores)
print(result)  # Output: [2, 4]