# day2_control_flow.py

# If-Else conditions
age = int(input("Enter you age: "))

if age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# For loop example
print("Counting from 1 to 5: ")

for i in range(1, 6):
    print(f"i value is {i}")

# While loop example
count = 5
while count > 0:
    print(f"countdown: {count}")
    count -= 1

# Function declaration
def greet(name):
    return f"Hi {name}"

# Function call
user_name = input("What is your name? ")
print(greet(user_name))