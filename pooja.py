# Python syntax basics:
# Python uses indentation to define blocks:
if True:
    print("Hello, Pooja!")


# Variables and data types:
name = "Pooja"
age = 21        

# operators:
sum = age + 5
print("Sum:", sum)

# string, lists, tuples, Dictionaries, and sets:
#strings
name = "Pooja"
print(name.upper())

# lists
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

# tuples
coordinates = (10, 20)
print(coordinates[1])

# Dictionaries
person = {"name": "Pooja", "age": 21}
print(person["name"])

# sets
unique_numbers = {1, 2, 3, 4, 5}
print(unique_numbers)



# List comprehensions, Generator expressions, and Dictionary comprehensions:
# List comprehensions
squares = [x**2 for x in range(10)]
print(squares)

# Generator expressions
gen=(x**2 for x in range(10))
print(list(gen))
print(list(gen))  # This will be empty since the generator is exhausted

# Dictionary comprehensions
squared_dict = {x: x**2 for x in range(10)}
print(squared_dict)



# Object-oriented programming (OOP):
# Classes and objects:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
person1 = Person("Pooja", 21)
print(person1.greet())

# Inheritance:
class Student(Person):  
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  
        self.student_id = student_id

    def get_student_info(self):
        return f"Student ID: {self.student_id}"


student1 = Student("Pooja", 21, "S001")
print(student1.greet())
print(student1.get_student_info())


#Encapsulation:
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance
account = BankAccount("Pooja")
account.deposit(1000)   
account.withdraw(200)    
print("Current balance:", account.get_balance())

# Polymorphism:
class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c
calc = Calculator()
print(calc.add(1, 2, 3))  # This will call the second add method, as it overwrites the first one.


#Method overriding:
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

class Cat(Animal):
    def speak(self):
        return "Cat meows"

# Creating instances of the classes
animal = Animal()
dog = Dog()
cat = Cat()

# Calling the speak method (polymorphism)
print(animal.speak())
print(dog.speak())
print(cat.speak())

# Exception handling:
try:
    #code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

#Muliple except blocks:
try:
    #code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


#Raising and catching exceptions:
#creating a custom exception class
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
#raising the custom exception
try:
    raise CustomError("This is a custom error.")
except CustomError as e:
    print(f"Custom error occurred: {e.message}")
#catching a custom exception
try:
    raise CustomError("This is another custom error.")
except CustomError as e:
    print(f"Custom error occurred: {e.message}")

#Example:
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def divide(a, b):
    # Custom condition: if a or b is negative, raise CustomError
    if a < 0 or b < 0:
        raise CustomError("Negative values are not allowed for division.")
    
    # Real error condition: Division by zero
    if b == 0:
        raise Exception("Division by zero is not allowed.")  # This uses the real exception for zero division.

    return a / b

try:
    result = divide(-10, 5)  # This will trigger the CustomError
except CustomError as e:
    print(f"Caught CustomError: {e}")
except Exception as e:
    # This will catch other general exceptions, including division by zero
    print(f"Caught a general exception: {e}")




# Modules and packages:
# Importing a module:
import math
print(math.sqrt(16))




# Loops types in Python:
# For loop:
for i in range(5):
    print(i)

# While loop:
i = 0
while i < 5:
    print(i)
    i += 1

#nested loops:
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# break and continue statements:
for i in range(10):
    if i == 5:
        break
    print(i)
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)


# Functional programming concepts:
# Pure functions:
def add(a, b):
    return a + b
print(add(2, 3))

# first-class functions:
def greet(name):
    return f"Hello, {name}!"
greeting = greet  # Assigning the function to a variable
print(greeting("Pooja"))
func = greeting("Pooja")
print(func)

# higher-order functions:
def apply_operation(a, b, operation):
    return operation(a, b)
def multiply(x, y):
    return x * y
result = apply_operation(5, 3, multiply)
print(result)
def square(x):
    return x * x
print(apply_operation(4, 0, lambda x, _: square(x)))  # Using a lambda function to apply the square operation



# higher-order functions, lambda functions, and map, filter, and reduce functions:
# higher-order functions:
def higher_order(func): 
    return func()
def say_hello():
    return "Hello, Pooja!"
print(higher_order(say_hello))

# lambda functions:
square = lambda x: x * x 
print(square(5))

# map function:
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)

# filter function:
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# reduce function:
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)



# Design patterns:
# closures:
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function
closure = outer_function("Hello, Pooja!")
closure()  # This will print "Hello, Pooja!" because the inner function has access to the msg variable from the outer function.

# decorators:
def decorator(func):
    def wrapper():
        print("Before the function call.")
        func()
        print("After the function call.")
    return wrapper



#Working with modules and packages:
# Creating and importing a module:
def greet(name):
    return f"Hello, {name}!"
# To use this module, you would save it as greet_module.py and then import it in another file:
# from greet_module import greet
print(greet("Pooja"))

# using built-in and third-party libraries:
# Using a built-in library:
import os
print(os.getcwd())  # This will print the current working directory.    
import os
#Get the current working directory
current_directory = os.getcwd()
print("Current Directory:", current_directory)
#List all files and directories in the current directory
files_and_directories = os.listdir(current_directory)
print("Files and Directories:", files_and_directories)
# creating a new directory
new_directory = os.path.join(current_directory, "new_folder")
os.makedirs(new_directory, exist_ok=True)
print("New Directory Created:", new_directory)
#Removing the created directory
os.rmdir(new_directory)

#Get the version of python
import sys
print("Python version:", sys.version)

#Get the list of command-line arguments
command_line_arguments = sys.argv
print("Command-line arguments:", sys.argv)

#Exit from python
print("Exiting Python...")
sys.exit()

#Math
#Calculating the square root of a number
import math
sqrt_value = math.sqrt(16)
print("Square root of 16:", sqrt_value)

#Calculate the factorial of a number
factorial_value = math.factorial(5)
print("Factorial of 5:", factorial_value)

#calculate the greatest common divisor (GCD) of two numbers
gcd_value = math.gcd(48, 18)
print("GCD of 48 and 18:", gcd_value)

#Third party libraries:
#Using the requests library to make an HTTP GET request
import requests
response = requests.get("https://api.github.com")
if response.status_code == 200:
    print("Request successful!")
    print("Response JSON:", response.json())


#File handling:
# opening a file using open() function
file_path = "example.txt"
file = open(file_path, "w")
file.write("Hello, Pooja!")
file.close()
#Writing to a file using with statement
with open(file_path, "w") as file:
    file.write("Hello, Pooja!")
#Appending to a file
with open(file_path, "a") as file:
    file.write("\nWelcome to Python programming.")

#Working with json, csv, and other file formats:
#Working with JSON files:
import json
#Reading JSON data from a file
with open("data.json", "r") as file:
    data = json.load(file)
#Writing JSON data to a file
with open("output.json", "w") as file:
    json.dump(data, file, indent=4)

#Working with CSV files:
import csv
#Writing to a CSV file
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Pooja", 21])
#Reading from a CSV file
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)



#BAsics of concurrency and multithreading:
#Using the threading module to create a simple thread
import threading
import time
def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1) #Sleep for 1 second between prints

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(letter)
        time.sleep(1) #Sleep for 1 second between prints

#Creating a thread
thread = threading.Thread(target=print_letters)
thread.start()
thread.join() #Wait for the thread to complete 

#Starting another thread
thread2 = threading.Thread(target=print_numbers)    
thread2.start()
thread2.join() #Wait for the thread to complete

#waiting for both threads to complete
print("Both threads have completed.")
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)
thread1.start()
thread2.start()
thread1.join()
thread2.join()

#execution of join() method ensures that the main program waits for both threads to finish before proceeding. This is important to ensure that all output is printed before the program exits.
thread1.join()
thread2.join()


#Basics of concurrency and parallelism:
#Using the multiprocessing module to create a simple process
import asyncio
import multiprocessing
async def print_numbers():
    for i in range(5):
        print(i)
        await asyncio.sleep(1)  # Sleep for 1 second between prints
async def main():
    # Create a process for the print_numbers function
    process = multiprocessing.Process(target=asyncio.run, args=(print_numbers(),))
    process.start()
    process.join()  # Wait for the process to complete


#Working with threading and multiprocessing modules:
#Using the threading module to create a simple thread
import threading
import time
def worker():
    print("Worker thread is starting.")
    time.sleep(2)  # Simulate some work
    print("Worker thread has finished.")
#creating a thread
thread = threading.Thread(target=worker)
thread.start()
thread.join()  # Wait for the thread to complete

#using multiprocessing module to create a simple process
import multiprocessing

def worker():
    print("Worker process is starting.")
    time.sleep(2)  # Simulate some work
    print("Worker process has finished.")

if __name__ == "__main__":
    #creating a process
    process = multiprocessing.Process(target=worker)
    process.start()
    process.join()  # Wait for the process to complete
    
