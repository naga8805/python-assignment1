# 1. Function to sum all even numbers in a list
def sum_even_numbers(lst):
    return sum(x for x in lst if x % 2 == 0)

# 2. Function to reverse a string
def reverse_string(s):
    return s[::-1]

# 3. Function to return squares of a list
def square_list(lst):
    return [x**2 for x in lst]

# 4. Function to check for prime numbers from 1 to 200
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

prime_numbers = [n for n in range(1, 201) if is_prime(n)]

# 5. Iterator class for Fibonacci sequence
class FibonacciIterator:
    def __init__(self, limit):
        self.limit = limit
        self.a, self.b = 0, 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return value

# 6. Generator for powers of 2
def powers_of_two(n):
    for i in range(n + 1):
        yield 2 ** i

# 7. Generator to read a file line by line
def read_file_lines(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

# 8. Sort list of tuples by second element using lambda
data = [(1, 3), (2, 1), (3, 2)]
sorted_data = sorted(data, key=lambda x: x[1])

# 9. Convert Celsius to Fahrenheit using map
celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

# 10. Remove vowels from a string using filter
def remove_vowels(s):
    return ''.join(filter(lambda x: x.lower() not in 'aeiou', s))

# 11. Bookstore accounting routine with lambda and map
orders = [
    ["34587", "Learning Python", 4, 40.95],
    ["98762", "Programming Python", 5, 56.80],
    ["77226", "Head First Python", 3, 32.95],
    ["88112", "Einführung in Python3", 3, 24.99]
]

order_totals = list(map(lambda order: (order[0], round(order[2] * order[3] + (10 if order[2]*order[3] < 100 else 0), 2)), orders))