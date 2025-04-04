# iterators

my_list = [1, 2, 3]
my_iter = iter(my_list)  # Create an iterator from the list

print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2
print(next(my_iter))  # Output: 3
#print(next(my_iter))  # Raises StopIteration exception, no more items

# generators

# using yield

#from typing import Generator
from collections.abc import Generator

def count_up_to(n: int) -> Generator[int, None, None]:
    """A generator function that counts up to n."""
    count = 1
    while count <= n:
        yield count  # Yield the current count
        count += 1   # Increment the count

print("Using yield:")
counter = count_up_to(3)
print(next(counter)) # Output: 1
print(next(counter)) # Output: 2
print(next(counter)) # Output: 3
#print(next(counter)) # Raises StopIteration exception, no more items

def fibonacci_gen() -> Generator[int, None, None]:
    """A generator function that yields Fibonacci numbers."""
    a, b = 0, 1
    while True:
        yield a  # Yield the current Fibonacci number
        a, b = b, a + b  # Update to the next Fibonacci number

fib = fibonacci_gen()  # Create a generator object
print("Using Fibonacci generator:")
print(next(fib)) # Output: 0
print(next(fib)) # Output: 1
print(next(fib)) # Output: 1
print(next(fib)) # Output: 2
print(next(fib)) # Output: 3
print(next(fib)) # Output: 5

# using expressions

#expression = (x + 1 for x in range(3))
expression = ( (x+1) ** 2 for x in range(4))
print("Using expression:")
print(next(expression)) # Output: 0
print(next(expression)) # Output: 1
print(next(expression)) # Output: 2
print(next(expression)) # Raises StopIteration exception, no more items
