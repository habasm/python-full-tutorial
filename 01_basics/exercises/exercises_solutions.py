# 🧑‍💻 Python Basics – Exercise Solutions

import random

# ----------------------------------------------------
# Exercise 1 – User Input
# ----------------------------------------------------
def exercise1():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print(f"Hello {name}, you are {age} years old!")
    print(f"In 5 years, you will be {age + 5}.")

# ----------------------------------------------------
# Exercise 2 – Even Numbers
# ----------------------------------------------------
def exercise2():
    evens = [i for i in range(1, 21) if i % 2 == 0]
    print("Even numbers:", ", ".join(map(str, evens)))
    print("Total count:", len(evens))

# ----------------------------------------------------
# Exercise 3 – List Operations
# ----------------------------------------------------
def exercise3():
    numbers = [int(x) for x in input("Enter 5 numbers separated by space: ").split()]
    print("Numbers:", numbers)
    print("Sum:", sum(numbers))
    print("Max:", max(numbers))
    print("Min:", min(numbers))
    print("Average:", sum(numbers) / len(numbers))

# ----------------------------------------------------
# Exercise 4 – Palindrome Checker
# ----------------------------------------------------
def is_palindrome(word):
    cleaned = word.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def exercise4():
    word = input("Enter a word: ")
    print("Is palindrome?", is_palindrome(word))

# ----------------------------------------------------
# Exercise 5 – Multiplication Table
# ----------------------------------------------------
def exercise5():
    n = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

# ----------------------------------------------------
# Exercise 6 – Guess the Number
# ----------------------------------------------------
def exercise6():
    secret = random.randint(1, 10)
    chances = 3
    print("Guess a number between 1 and 10")
    for _ in range(chances):
        guess = int(input("Your guess: "))
        if guess == secret:
            print("🎉 Correct! You win!")
            return
        elif guess < secret:
            print("Too low!")
        else:
            print("Too high!")
    print(f"Sorry, you lost. The number was {secret}.")

# ----------------------------------------------------
# Exercise 7 – Word Counter
# ----------------------------------------------------
def exercise7():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    chars = len("".join(words))
    print("Words:", len(words))
    print("Characters (no spaces):", chars)

# ----------------------------------------------------
# Exercise 8 – FizzBuzz
# ----------------------------------------------------
def exercise8():
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=", ")
        elif i % 3 == 0:
            print("Fizz", end=", ")
        elif i % 5 == 0:
            print("Buzz", end=", ")
        else:
            print(i, end=", ")
    print()

# ----------------------------------------------------
# Exercise 9 – Reverse a String
# ----------------------------------------------------
def exercise9():
    text = input("Enter a string: ")
    reversed_text = text[::-1]
    print("Reversed:", reversed_text)
    print("Is palindrome?", text.lower() == reversed_text.lower())

# ----------------------------------------------------
# Exercise 10 – Basic Calculator
# ----------------------------------------------------
def exercise10():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /): ")

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        result = a / b if b != 0 else "Error (division by zero)"
    else:
        result = "Invalid operator"

    print("Result:", result)


# ----------------------------------------------------
# Runner – to test all exercises individually
# ----------------------------------------------------
if __name__ == "__main__":
    exercises = {
        "1": exercise1,
        "2": exercise2,
        "3": exercise3,
        "4": exercise4,
        "5": exercise5,
        "6": exercise6,
        "7": exercise7,
        "8": exercise8,
        "9": exercise9,
        "10": exercise10,
    }

    print("Python Basics – Exercise Solutions")
    choice = input("Choose exercise (1-10) or 'all': ")

    if choice == "all":
        for key, func in exercises.items():
            print(f"\n--- Running Exercise {key} ---")
            func()
    elif choice in exercises:
        exercises[choice]()
    else:
        print("Invalid choice.")
