# ===============================
# 🔰 Control Flow in Python
# ===============================

print("_" * 50)
print("📌 IF-ELSE Examples")
print("_" * 50)

x = 10

# If-elif-else
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# Nested conditions
if x > 0:
    if x % 2 == 0:
        print("x is a positive even number")
    else:
        print("x is a positive odd number")

# Ternary operator
status = "Even" if x % 2 == 0 else "Odd"
print(f"x is {status}")

print("_" * 50)
print("📌 FOR Loop Examples")
print("_" * 50)

# Looping over a range
for i in range(5):
    print("Iteration:", i)

# Loop with step
for i in range(0, 10, 2):
    print("Even number:", i)

# Looping over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# Looping with index
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Looping over dictionary
student = {"name": "Alice", "age": 21, "grade": "A"}
for key, value in student.items():
    print(f"{key}: {value}")

print("_" * 50)
print("📌 Loop Control (break, continue, else)")
print("_" * 50)

# Break example
for i in range(10):
    if i == 5:
        print("Breaking at 5")
        break
    print(i)

# Continue example
for i in range(5):
    if i == 2:
        print("Skipping 2")
        continue
    print(i)

# For loop with else (runs if no break occurs)
for i in range(3):
    print(i)
else:
    print("Loop finished without break")

print("_" * 50)
print("📌 WHILE Loop Examples")
print("_" * 50)

count = 0
while count < 3:
    print("Count:", count)
    count += 1
else:
    print("While loop finished")

# Safe while loop with break condition
n = 1
while True:
    if n > 5:
        break
    print("n:", n)
    n += 1

print("_" * 50)
print("📌 MATCH-CASE (Python 3.10+)")
print("_" * 50)

day = "Monday"

match day:
    case "Monday":
        print("Start of the work week")
    case "Friday":
        print("Almost weekend")
    case "Saturday" | "Sunday":
        print("Weekend!")
    case _:
        print("Midweek day")

print("_" * 50)
print("✅ End of Control Flow Demo")
print("_" * 50)
