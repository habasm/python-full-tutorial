# ===============================
# 🔰 Python Variables & Printing
# ===============================

# Basic variables
age = 25                           # Integer
name = "Abebe"                     # String
balance = 67.05                    # Float
pi = 3.141592653589                # Float (long precision)
is_student = True                  # Boolean

# Collections
fruits = ["apple", "banana", "cherry"]  # List
coordinates = (10, 20)                  # Tuple
unique_numbers = {1, 2, 3, 3, 2}        # Set (removes duplicates)
student = {"name": "Alice", "age": 21, "grade": "A"}  # Dictionary

# Table-like data
data = [
    ("Name", "Age", "City"),   # Header
    ("Alice", 25, "New York"),
    ("Bob", 30, "London"),
    ("Charlie", 22, "Paris"),
    ("Dawit", 28, "Addis Ababa"),
]

print("_" * 60)
print("📌 Data Types Demo")
print("_" * 60)

# Display variable types
print("The type of 'age' variable is:     ", type(age))
print("The type of 'name' variable is:    ", type(name))
print("The type of 'balance' variable is: ", type(balance))
print("The type of 'is_student':          ", type(is_student))
print("The type of 'fruits':              ", type(fruits))
print("The type of 'coordinates':         ", type(coordinates))
print("The type of 'unique_numbers':      ", type(unique_numbers))
print("The type of 'student':             ", type(student))

print("_" * 60)
print("📌 String & Number Formatting")
print("_" * 60)

# Display information in multiple ways
print("The age of Abebe is:", age)  # simple print
print(f"The age of {name} is {age} years old")  # f-string
print("The age of {} is {} years old".format(name, age))  # format method
print("The age {1} is associated with the {0}".format(name, age))  # reordering
print("My name is %s and I am %d years old." % (name, age))  # old-style formatting

# Working with floating numbers
print(f"Pi rounded to 2 decimal places: {pi:.2f}")
print("Pi rounded to 4 decimals (format method): {:.4f}".format(pi))

# Numeric operations
print(f"Balance + 10: {balance + 10}")
print(f"Absolute value of -5: {abs(-5)}")
print(f"Rounded balance (no decimals): {round(balance)}")

print("_" * 60)
print("📌 String Operations")
print("_" * 60)

sample_text = "   Hello Python World!   "
print("Original:", f"[{sample_text}]")
print("Uppercase:", sample_text.upper())
print("Lowercase:", sample_text.lower())
print("Stripped:", f"[{sample_text.strip()}]")  # remove spaces
print("Replace:", sample_text.replace("Python", "Programming"))
print("Split:", sample_text.split())
print("Join:", "-".join(["Python", "is", "fun"]))

print("_" * 60)
print("📌 Text Alignment Examples")
print("_" * 60)

text = "Hi"
print(f"[{text:<10}] <- Left aligned")
print(f"[{text:>10}] <- Right aligned")
print(f"[{text:^10}] <- Center aligned")

print("_" * 60)
print("📌 Table Formatting (Aligned)")
print("_" * 60)

# Method 1: simple loop
for row in data:
    print(f"{row[0]:<12}{row[1]:<6}{row[2]:<15}")

print("_" * 60)

# Method 2: header + separator
header = data[0]
print(f"{header[0]:<12}{header[1]:<6}{header[2]:<15}")
print("-" * 33)
for row in data[1:]:
    print(f"{row[0]:<12}{row[1]:<6}{row[2]:<15}")

print("_" * 60)
print("📌 Dictionary Access")
print("_" * 60)

print("Student Dictionary:", student)
print("Name:", student["name"])
print("Age:", student["age"])
print("Grade:", student["grade"])

print("_" * 60)
print("📌 Lists & Loops")
print("_" * 60)

for fruit in fruits:
    print("Fruit:", fruit)

print("_" * 60)
print("✅ End of Demo")
print("_" * 60)

# (Optional) Ask user input
# user_name = input("Enter your name: ")
# print(f"Hello {user_name}, nice to meet you!")
