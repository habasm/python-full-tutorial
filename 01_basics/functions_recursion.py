# ===============================
# 🔰 Recursion in Python
# ===============================

print("_" * 50)
print("📌 Recursion Examples with Explanations")
print("_" * 50)

# ------------------------------------------------
# 1. Factorial (classic recursion)
# ------------------------------------------------
def factorial(n: int) -> int:
    """
    Compute factorial of a number using recursion.
    factorial(n) = n * factorial(n-1), with factorial(0) = 1

    Example:
    factorial(4)
    = 4 * factorial(3)
    = 4 * (3 * factorial(2))
    = 4 * (3 * (2 * factorial(1)))
    = 4 * (3 * (2 * 1))
    = 24
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))


# ------------------------------------------------
# 2. Fibonacci Sequence
# ------------------------------------------------
def fibonacci(n: int) -> int:
    """
    Compute the nth Fibonacci number using recursion.
    fibonacci(0) = 0, fibonacci(1) = 1

    Example for fibonacci(5):
    fib(5)
     ├─ fib(4)
     │   ├─ fib(3)
     │   │   ├─ fib(2)
     │   │   │   ├─ fib(1) = 1
     │   │   │   └─ fib(0) = 0
     │   │   └─ fib(1) = 1
     │   └─ fib(2)
     │       ├─ fib(1) = 1
     │       └─ fib(0) = 0
     └─ fib(3) ...
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci(6):", fibonacci(6))


# Optimized Fibonacci with memoization (caching results)
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_memo(n: int) -> int:
    """Efficient Fibonacci with memoization (no repeated calls)."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)

print("Fibonacci with memoization (20):", fibonacci_memo(20))


# ------------------------------------------------
# 3. Recursive Sum of a List
# ------------------------------------------------
def recursive_sum(lst: list[int]) -> int:
    """
    Compute sum of list using recursion.

    Example with [1, 2, 3]:
    recursive_sum([1, 2, 3])
    = 1 + recursive_sum([2, 3])
    = 1 + (2 + recursive_sum([3]))
    = 1 + (2 + (3 + recursive_sum([])))
    = 1 + (2 + (3 + 0))
    = 6
    """
    if not lst:  # base case: empty list
        return 0
    return lst[0] + recursive_sum(lst[1:])

numbers = [1, 2, 3, 4, 5]
print(f"Recursive sum of {numbers}:", recursive_sum(numbers))


# ------------------------------------------------
# 4. Reverse a String Recursively
# ------------------------------------------------
def reverse_string(s: str) -> str:
    """
    Reverse a string using recursion.

    Example:
    reverse_string("abc")
    = reverse_string("bc") + "a"
    = (reverse_string("c") + "b") + "a"
    = ("c" + "b") + "a"
    = "cba"
    """
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

text = "recursion"
print(f"Reverse of '{text}':", reverse_string(text))


# ------------------------------------------------
# 5. Countdown Example
# ------------------------------------------------
def countdown(n: int) -> None:
    """
    Print a countdown using recursion.

    Example for countdown(3):
    countdown(3) → prints 3
      countdown(2) → prints 2
        countdown(1) → prints 1
          countdown(0) → prints "Blast off!"
    """
    if n <= 0:
        print("Blast off! 🚀")
    else:
        print(n)
        countdown(n - 1)

countdown(5)


print("_" * 50)
print("✅ End of Recursion Demo")
print("_" * 50)
