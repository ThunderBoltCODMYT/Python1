# Step 1: Get user input
num = int(input("Enter a number: "))

# Step 2: Initialize count variable
count = 0

# Step 3: Use a while loop to count digits
while num != 0:
    num = num // 10  # Remove the last digit
    count += 1  # Increase the count

# Step 4: Print the total number of digits
print("Total digits:", count)