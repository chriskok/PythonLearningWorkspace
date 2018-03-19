# ---------- PROBLEM ----------
# Create a random list filled with the characters H and T
# for heads and tails. Output the number of Hs and Ts
# Example Output
# Heads :  46
# Tails :  54

# Create the list
flipList = []

# Populate the list with 100 Hs and Ts
# Trick : random.choice() returns a random value from the list
for i in range(1, 101):
    flipList += random.choice(['H', 'T'])

# Output results
print("Heads : ", flipList.count('H'))
print("Tails : ", flipList.count('T'))