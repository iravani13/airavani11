# Lab 3 - Investigating loops

# Function from step 2
def check_number(num):
    return num % 5 == 0

# Step 3
user_num = int(input("Enter a number: "))  # Lab 1 - Introduction to Python

# Step 4
count = 0
while not check_number(user_num):  # Lab 3 - Investigating loops
    print(user_num)  # Print the current value before adding 5
    user_num += 5
    count += 1

# Step 6
print(user_num)
print(user_num+5)
print(user_num+10)
print(user_num+15)
print("Number of times loop repeated:", count)

