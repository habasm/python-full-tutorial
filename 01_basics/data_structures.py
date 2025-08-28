# ===============================
# 🔰 Data Structures in Python
# ===============================

print("_" * 60)
print("📌 LISTS")
print("_" * 60)

# List (ordered, mutable, allows duplicates)
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Iterating through list
for fruit in fruits:
    print("Fruit:", fruit)

# List operations
fruits.append("orange")         # add element
fruits.remove("banana")         # remove element
print("Updated Fruits:", fruits)

# Slicing
print("First two fruits:", fruits[:2])

# List comprehension
squares = [x**2 for x in range(5)]
print("Squares:", squares)

print("_" * 60)
print("📌 TUPLES")
print("_" * 60)

# Tuple (ordered, immutable)
coordinates = (10, 20)
print("Coordinates:", coordinates)

# Iterating
for value in coordinates:
    print("Coordinate:", value)

# Tuple unpacking
x, y = coordinates
print("Unpacked:", x, y)

# Tuples are immutable (the following would cause error if uncommented)
# coordinates[0] = 99

print("_" * 60)
print("📌 SETS")
print("_" * 60)

# Set (unordered, no duplicates)
unique_numbers = {1, 2, 3, 3, 2}
print("Unique Numbers:", unique_numbers)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference (a-b):", a - b)
print("Difference (b-a):", b - a)

# Add/remove
a.add(6)
a.discard(2)
print("Modified set a:", a)

print("_" * 60)
print("📌 DICTIONARIES")
print("_" * 60)

# Dictionary (key-value pairs)
student = {"name": "Alice", "age": 21, "grade": "A"}
print("Student Info:", student)

# Accessing values
print("Name:", student["name"])
print("Age:", student.get("age"))   # safer than student["age"]

# Iterating over dict
for key, value in student.items():
    print(f"{key}: {value}")

# Adding/updating
student["age"] = 22
student["city"] = "New York"
print("Updated Student:", student)

# Dictionary methods
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items:", list(student.items()))

print("_" * 60)
print("📌 NESTED STRUCTURES")
print("_" * 60)

# List of dictionaries
students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "C"}
]

for s in students:
    print(f"{s['name']} got grade {s['grade']}")

# Dictionary of lists
classroom = {
    "Math": ["Alice", "Bob"],
    "Science": ["Charlie", "David"]
}
print("Classroom:", classroom)

for subject, names in classroom.items():
    print(f"{subject}: {', '.join(names)}")

print("_" * 60)
print("✅ End of Data Structures Demo")
print("_" * 60)
