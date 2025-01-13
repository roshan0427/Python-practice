# 1. Print "Hello, World!"
print("Hello, World!")

# 2. Variables and Data Types
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Your name is", name, "and your age is", age)

# 3. Arithmetic Operations
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

# 4. Convert Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

# 5. Swap Two Variables
x = input("Enter first variable: ")
y = input("Enter second variable: ")
print("Before swapping: x =", x, ", y =", y)
x, y = y, x
print("After swapping: x =", x, ", y =", y)

# 6. Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 7. Check Vowel or Consonant
letter = input("Enter a letter: ").lower()
if letter in "aeiou":
    print("Vowel")
else:
    print("Consonant")

# 8. Square, Cube, and Square Root
num = float(input("Enter a number: "))
print("Square:", num ** 2)
print("Cube:", num ** 3)
print("Square root:", num ** 0.5)

# 9. Area of Circle
radius = float(input("Enter the radius of the circle: "))
area = 3.14159 * radius ** 2
print("Area of the circle:", area)

# 10. Simple Interest Calculation
principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))
si = (principal * rate * time) / 100
print("Simple Interest:", si)

# 11. Largest of Three Numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
print("Largest:", max(a, b, c))

# 12. Leap Year Checker
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# 13. Multiplication Table
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# 14. Sum of N Natural Numbers
n = int(input("Enter a number: "))
print("Sum:", n * (n + 1) // 2)

# 15. Factorial of a Number
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial:", fact)

# 16. Number Guessing (While Loop)
import random
random_number = random.randint(1, 100)
guess = int(input("Guess the number between 1 and 100: "))
while guess != random_number:
    if guess < random_number:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Try again: "))
print("Correct! The number was", random_number)

# 17. Count Digits of a Number
num = int(input("Enter a number: "))
print("Number of digits:", len(str(num)))

# 18. Reverse a Number (While Loop)
num = int(input("Enter a number: "))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print("Reversed number:", reversed_num)

# 19. Sum of Even and Odd Numbers Separately
n = int(input("Enter a number: "))
even_sum, odd_sum = 0, 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)

# 20. Palindrome Checker (Integer)
num = int(input("Enter a number: "))
original_num = num
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
if original_num == reversed_num:
    print("Palindrome")
else:
    print("Not a Palindrome")

# 21. Create a Simple Calculator (Functions)
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == '+':
    print(add(a, b))
elif operation == '-':
    print(subtract(a, b))
elif operation == '*':
    print(multiply(a, b))
elif operation == '/':
    print(divide(a, b))
else:
    print("Invalid operation")

# 22. Power Function
def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

base = float(input("Enter base: "))
exponent = int(input("Enter exponent: "))
print(power(base, exponent))

# 23. Count Characters in a String (Function)
def count_characters(s):
    return len(s)

string = input("Enter a string: ")
print(count_characters(string))

# 24. Check Prime (Function)
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
print(is_prime(num))

# 25. Fibonacci Series (Function)
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

n = int(input("Enter number of terms: "))
print(fibonacci(n))

# 26. GCD of Two Numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(gcd(a, b))

# 27. LCM of Two Numbers
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(lcm(a, b))

# 28. Factorial (Recursive)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a number: "))
print(factorial(num))

# 29. Tower of Hanoi
def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)

n = int(input("Enter number of disks: "))
tower_of_hanoi(n, 'A', 'C', 'B')

# 30. Count Occurrences of an Element
def count_occurrences(lst, x):
    return lst.count(x)

lst = list(map(int, input("Enter list of numbers: ").split()))
x = int(input("Enter element to count: "))
print(count_occurrences(lst, x))



# 31. List Operations
lst = [1, 2, 3]
lst.append(4)
print("After append:", lst)
lst.insert(2, 5)
print("After insert:", lst)
lst.remove(2)
print("After remove:", lst)
lst.pop()
print("After pop:", lst)

# 32. Maximum and Minimum in a List
nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("Max:", max(nums))
print("Min:", min(nums))

# 33. Second Largest Element
nums = list(map(int, input("Enter unique numbers separated by space: ").split()))
nums.sort()
print("Second largest:", nums[-2])

# 34. Sum and Average of a List
nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("Sum:", sum(nums))
print("Average:", sum(nums) / len(nums))

# 35. Count Positive, Negative, Zero
nums = list(map(int, input("Enter numbers separated by space: ").split()))
pos = neg = zero = 0
for num in nums:
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        zero += 1
print("Positive:", pos, "Negative:", neg, "Zero:", zero)

# 36. Remove Duplicates from a List
nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("Without duplicates:", list(set(nums)))

# 37. Concatenate Two Lists
list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))
print("Concatenated list:", list1 + list2)

# 38. List Reversal
def reverse_list(lst):
    lst.reverse()
nums = list(map(int, input("Enter numbers: ").split()))
reverse_list(nums)
print("Reversed list:", nums)

# 39. Find Common Elements of Two Lists
list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))
print("Common elements:", list(set(list1) & set(list2)))

# 40. Element-wise Sum of Two Lists
list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))
result = [a + b for a, b in zip(list1, list2)]
print("Element-wise sum:", result)

# 41. Tuple Creation and Access
tpl = ("apple", "banana", "cherry")
index = int(input("Enter index: "))
print("Element at index:", tpl[index])

# 42. Tuple to List
tpl = tuple(map(int, input("Enter tuple elements: ").split()))
lst = list(tpl)
lst[0] = lst[0] * 2
tpl = tuple(lst)
print("Modified tuple:", tpl)

# 43. Check if Element Exists in Tuple
tpl = tuple(map(int, input("Enter tuple elements: ").split()))
elem = int(input("Enter element to check: "))
print("Exists in tuple:", elem in tpl)

# 44. Dictionary: Word Count
text = input("Enter a string: ")
words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print("Word count:", word_count)

# 45. Dictionary: Student Grades
grades = {"Alice": 90, "Bob": 85, "Charlie": 95}
name = input("Enter student name: ")
print("Grade:", grades.get(name, "Not found"))

# 46. Dictionary: Keys and Values
d = {"a": 1, "b": 2, "c": 3}
print("Keys:", list(d.keys()))
print("Values:", list(d.values()))

# 47. Merge Two Dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
merged_dict = {**d1, **d2}
print("Merged dictionary:", merged_dict)

# 48. Invert Dictionary
d = {"a": 1, "b": 2, "c": 3}
inverted_dict = {v: k for k, v in d.items()}
print("Inverted dictionary:", inverted_dict)

# 49. Set Operations
set1 = set(map(int, input("Enter first list: ").split()))
set2 = set(map(int, input("Enter second list: ").split()))
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)

# 50. Set Membership Testing
names = {"Alice", "Bob", "Charlie"}
name = input("Enter name: ")
print("Exists in set:", name in names)

# 51. Reverse a String
string = input("Enter a string: ")
print(string[::-1])

# 52. Palindrome String Checker
string = input("Enter a string: ")
print(string == string[::-1])

# 53. Count Vowels in a String
string = input("Enter a string: ").lower()
vowels = "aeiou"
count = sum(1 for char in string if char in vowels)
print(count)

# 54. Check Anagram
str1 = input("Enter first string: ").lower()
str2 = input("Enter second string: ").lower()
print(sorted(str1) == sorted(str2))

# 55. Remove Spaces
string = input("Enter a string: ")
print(string.replace(" ", ""))

# 56. Longest Word in a Sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word = max(words, key=len)
print(longest_word)

# 57. String Case Conversion
string = input("Enter a string: ")
print(string.upper())
print(string.lower())
print(string.title())

# 58. Capitalize Every Word
string = input("Enter a string: ")
print(" ".join(word.capitalize() for word in string.split()))

# 59. Count Special Characters
import string as s
text = input("Enter a string: ")
special_chars = sum(1 for char in text if char in s.punctuation)
print(special_chars)

# 60. Character Frequency in String
text = input("Enter a string: ")
frequency = {}
for char in text:
    frequency[char] = frequency.get(char, 0) + 1
print(frequency)

# 61. Armstrong Number
num = int(input("Enter a number: "))
digits = [int(d) for d in str(num)]
print(sum(d**len(digits) for d in digits) == num)

# 62. Strong Number
from math import factorial
num = int(input("Enter a number: "))
digits = [int(d) for d in str(num)]
print(sum(factorial(d) for d in digits) == num)

# 63. Perfect Number
num = int(input("Enter a number: "))
divisors = [i for i in range(1, num) if num % i == 0]
print(sum(divisors) == num)

# 64. Sum of Digits
num = int(input("Enter a number: "))
print(sum(int(d) for d in str(num)))

# 65. Binary to Decimal Conversion
binary = input("Enter a binary number: ")
print(int(binary, 2))

# 66. Decimal to Binary Conversion
decimal = int(input("Enter a decimal number: "))
print(bin(decimal)[2:])

# 67. Prime Factors of a Number
def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

num = int(input("Enter a number: "))
print(prime_factors(num))

# 68. Number to Words
def num_to_words(n):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    return " ".join(words[int(d)] for d in str(n))

num = int(input("Enter a number: "))
print(num_to_words(num))

# 69. LCM of a Range
from math import gcd
def lcm_range(n):
    lcm = 1
    for i in range(1, n + 1):
        lcm = lcm * i // gcd(lcm, i)
    return lcm

n = int(input("Enter a number: "))
print(lcm_range(n))

# 70. Sieve of Eratosthenes
def sieve(n):
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [x for x in range(2, n + 1) if primes[x]]

n = int(input("Enter a number: "))
print(sieve(n))



# 71. Write to File
text = input("Enter text: ")
with open("output.txt", "w") as f:
    f.write(text)

# 72. Read from File
with open("output.txt", "r") as f:
    print(f.read())

# 73. Copy File
try:
    with open("output.txt", "r") as src, open("copy.txt", "w") as dest:
        dest.write(src.read())
except FileNotFoundError:
    print("Source file not found.")

# 74. Count Lines in a File
with open("output.txt", "r") as f:
    print(len(f.readlines()))

# 75. Count Words in a File
with open("output.txt", "r") as f:
    print(sum(len(line.split()) for line in f))

# 76. Find Longest Line in a File
with open("output.txt", "r") as f:
    print(max(f, key=len))

# 77. Search for a Word in a File
word = input("Enter word to search: ")
with open("output.txt", "r") as f:
    for i, line in enumerate(f, 1):
        if word in line:
            print(f"Found in line {i}")

# 78. Append to a File
text = input("Enter text to append: ")
with open("output.txt", "a") as f:
    f.write("\n" + text)

# 79. Remove Blank Lines
with open("output.txt", "r") as f, open("cleaned.txt", "w") as new_f:
    new_f.writelines(line for line in f if line.strip())

# 80. File Statistics
with open("output.txt", "r") as f:
    content = f.read()
    print("Characters:", len(content))
    print("Lines:", content.count("\n") + 1)
    print("Words:", len(content.split()))

# 81. Class Rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# 82. Class Circle
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14159 * self.radius

# 83. Class BankAccount
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance

# 84. Class Student
class Student:
    def __init__(self, name, student_id, grades):
        self.name = name
        self.student_id = student_id
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

# 85. Class Car and ElectricCar
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

# 86. Class ComplexNumber
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

# 87. Class Point
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

# 88. Classmethod and Staticmethod
class MyClass:
    def instance_method(self):
        return "Instance method"

    @classmethod
    def class_method(cls):
        return "Class method"

    @staticmethod
    def static_method():
        return "Static method"

# 89. Property Decorators
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

# 90. Class Employee with Inheritance
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        return f"Name: {self.name}, ID: {self.emp_id}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department

    def display(self):
        return f"{super().display()}, Department: {self.department}"




