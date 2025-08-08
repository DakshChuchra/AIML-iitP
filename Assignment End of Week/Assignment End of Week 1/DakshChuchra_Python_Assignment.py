# This file is part of the Python assignment for Daksh Chuchra.


# PART B: Coding Questions (22 Questions)
# Section 5: Easy Level (10 Qs)



# 1. Print “Hello, Python World!”.

print("Hello, Python World!")

# 2. Store your name, age, and city in variables and print them in a single line.

Ques1Name = "Daksh Chuchra"
Ques1Age = 25 
Ques1City = "Abohar" 
print(f"Name: {Ques1Name}, Age: {Ques1Age}, City: {Ques1City}")

# 3. Write a program to take user input for name and greet them.

Ques2Name = input("Please enter your name: ")
print(f"Hello, {Ques2Name}! Welcome.")

# 4. Convert temperature from Celsius to Fahrenheit.

temperatureCelsius = float(input("Enter temperature in Celsius: "))
temperatureFahrenheit = (temperatureCelsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {temperatureFahrenheit}°F")

# 5. Write a program to swap two numbers without using a third variable.

SwapNum1 = 5
SwapNum2 = 10
SwapNum1, SwapNum2 = SwapNum2, SwapNum1
print(f"After swapping: Num1 = {SwapNum1}, Num2 = {SwapNum2}")

# 6. Create a program that calculates the square and cube of a number.

num = float(input("Enter a number you want to Square or Cube: "))
square = num ** 2
cube = num ** 3
print(f"The number is: {num}")
print(f"The square is: {square}")
print(f"The cube is: {cube}")

# 7. Take three numbers as input and print the largest.

print("Enter three numbers to find the largest among them.")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    largest = num1
    print(f"The largest number is: {largest}")
elif num2 > num3:
    largest = num2
    print(f"The largest number is: {largest}")
else:
    largest = num3
    print(f"The largest number is: {largest}")

# 8. Write a program to calculate the sum of all elements in a list.

numbers = [10, 20, 30, 40, 50, '60']
total = 0
for i in numbers:
    total += int(i)
print(f"The sum of the numbers in the list is: {total}")

# 9. Write a script that checks Python version using sys module.

import sys
print(f"Python version: {sys.version}")

# 10. Write a script that takes user input and saves it to a file named output.txt.

user_input = input("Please enter some text to save in output.txt: ")
with open("output.txt", "w") as file:
    file.write(user_input)
print("Your input has been saved to output.txt.")



# Section 6: Medium Level (8 Qs)



# 1 & 2. Count words and characters in a sentence
# 1. Script to count the number of words in a given string.
# 2. Take a sentence from the user and print:
#    - Total words
#    - Total characters (excluding spaces)

sentence = input("Enter a sentence: ")
words = sentence.split()
total_words = len(words)
total_chars = len(sentence.replace(" ", ""))
print(f"Total words: {total_words}")
print(f"Total characters (excluding spaces): {total_chars}")

# 3. Write a program to simulate a simple calculator (add, subtract, multiply, divide).

print("Simple Calculator")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero"
else:
    result = "Invalid operation"
print(f"Result: {result}")

# 4. Take a comma-separated list of integers from input, then print:
#    - Sorted list
#    - Sum of numbers

input_str = input("Enter comma-separated integers: ")
int_list = [int(x.strip()) for x in input_str.split(",")]
sorted_list = sorted(int_list)
sum_of_numbers = sum(int_list)

print(f"Sorted list: {sorted_list}")
print(f"Sum of numbers: {sum_of_numbers}")

# 5. Write a script that reads a text file and counts how many times the word “Python” appears.
# First, create a sample file for the script to read

with open("sample.txt", "w") as f:
    f.write("Python is a great language. I love Python. Python is versatile.")

word_to_find = "Python"
count = 0

try:
    with open("sample.txt", "r") as file:
        content = file.read()
        # Split the content by words and count occurrences, case-insensitive
        words = content.lower().split()
        count = words.count(word_to_find.lower())
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

print(f"The word '{word_to_find}' appears {count} times.")

# 6. Write a program to generate a multiplication table for a given number up to 10.

num = int(input("Enter a number for multiplication table: "))
print(f"Multiplication table for {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")

# 7. Create a script that prints the current working directory using os module.

import os
print("Current working directory:", os.getcwd())

# 8. Write a program to create and activate a virtual environment using Python code

import venv
venv_dir = "myenv"
venv.create(venv_dir, with_pip=True)
print(f"Virtual environment created in ./{venv_dir}")
print("To activate it, run:")
print(f"  .\\{venv_dir}\\Scripts\\activate")
