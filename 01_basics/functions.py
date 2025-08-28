# ===============================
# 🔰 Functions in Python
# ===============================

print("_" * 50)
print("📌 Basic Functions")
print("_" * 50)

# Simple function
def greet(name: str) -> str:
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet("Bob"))

# Function with default argument
def add(a: int, b: int = 5) -> int:
    """Add two numbers, with default b=5."""
    return a + b

print("Sum (default b=5):", add(10))
print("Sum (override b):", add(10, 20))

print("_" * 50)
print("📌 Positional & Keyword Arguments")
print("_" * 50)

def describe_person(name: str, age: int, city: str = "Unknown") -> str:
    """Return formatted string describing a person."""
    return f"{name} is {age} years old and lives in {city}."

print(describe_person("Alice", 25))
print(describe_person(name="Bob", age=30, city="London"))

print("_" * 50)
print("📌 Arbitrary Arguments (*args, **kwargs)")
print("_" * 50)

def multiply(*args: int) -> int:
    """Multiply any number of arguments."""
    result = 1
    for num in args:
        result *= num
    return result

print("Multiply 2, 3, 4:", multiply(2, 3, 4))

def show_info(**kwargs) -> None:
    """Display key-value pairs passed as arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="Alice", age=25, country="Ethiopia")

print("_" * 50)
print("📌 Multiple Return Values")
print("_" * 50)

def min_max(numbers: list[int]) -> tuple[int, int]:
    """Return min and max from a list of numbers."""
    return min(numbers), max(numbers)

nums = [3, 7, 1, 9, 5]
low, high = min_max(nums)
print(f"Numbers: {nums}")
print(f"Min: {low}, Max: {high}")

print("_" * 50)
print("📌 Lambda Functions (Anonymous)")
print("_" * 50)

square = lambda x: x ** 2
print("Square of 5:", square(5))

# Lambda with sorted
words = ["banana", "apple", "cherry"]
sorted_words = sorted(words, key=lambda w: len(w))
print("Words sorted by length:", sorted_words)

print("_" * 50)
print("📌 Nested Functions & Closures")
print("_" * 50)

def outer_function(msg: str):
    """Example of closure."""
    def inner_function():
        print("Message from inner:", msg)
    return inner_function

my_func = outer_function("Hello from closure!")
my_func()  # calling inner function

print("_" * 50)
print("📌 Functions as First-Class Citizens")
print("_" * 50)

def apply_operation(func, x, y):
    """Apply a function to two numbers."""
    return func(x, y)

def add_op(a, b): return a + b
def mul_op(a, b): return a * b

print("Add via apply_operation:", apply_operation(add_op, 5, 3))
print("Multiply via apply_operation:", apply_operation(mul_op, 5, 3))

print("_" * 50)
print("✅ End of Functions Demo")
print("_" * 50)
