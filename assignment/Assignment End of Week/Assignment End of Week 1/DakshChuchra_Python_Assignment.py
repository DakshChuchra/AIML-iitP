# This file is part of the Python assignment for Daksh Chuchra.



#                                       Part A Theory (18 Questions)
#                           Section 1: Installation & Environment (5 Qs)



# Ans 1 =>  

# Windows: Python installation typically requires downloading an installer from the official website and running an executable file (.exe). It's common to check a box to add Python to the system's PATH during installation.
# Mac: Python often comes pre-installed, but it's an older version. It's recommended to install a newer version using a package manager like Homebrew.
# Linux: Python is usually pre-installed on most distributions. Newer versions can be installed from the distribution's package manager (e.g., apt on Ubuntu).


# Ans 2 =>

# The purpose of a virtual environment is to create an isolated, self-contained environment for a Python project. This prevents dependencies for one project from interfering with those of other projects or the global Python installation. Each virtual environment can have its own specific versions of libraries and packages.


# Ans 3 => 

# The purpose of a virtual environment is to create an isolated, self-contained environment for a Python project. This prevents dependencies for one project from interfering with those of other projects or the global Python installation. Each virtual environment can have its own specific versions of libraries and packages.


# Ans 4 => 

# Windows:-
# Create:- python -m venv myenv
# Activate:- myenv\Scripts\activate

# Linux/Mac:-
# Create:- python3 -m venv myenv
# Activate:- source myenv/bin/activate


# Ans 5=> 

# Isolating dependencies is crucial because different projects may require different versions of the same package. Without isolation, installing a new version of a package for one project could break another project that relies on the older version. Virtual environments ensure that each project has its own dedicated set of dependencies, maintaining stability and preventing conflicts.



#                               Section 2: IDE, Jupyter & CLI Basics (5 Qs)



# Ans 1=>

# It allows for code to be written, executed, and documented in a single document (notebook).
# It provides an interactive environment for data exploration, visualization, and step-by-step code execution.


# Ans 2=>

# VS Code:- is a full-featured code editor (an IDE) that is used for writing, debugging, and managing large-scale software projects. It offers advanced features like syntax highlighting, auto-completion, and integrated terminals.
# Jupyter Notebook:- is an interactive web-based environment primarily used for data science and research. It focuses on creating and sharing documents that contain live code, equations, visualizations, and narrative text. The code is executed in cells, allowing for a more modular and exploratory workflow.


# Ans 3=>

# Check Python version:-
# python --version in windows 
# python3 --version in mac or linux

# Install a package using pip:-
# pip install package_name 


# Ans 4=>

# This command is used to save a list of all the Python packages and their exact versions that are installed in the current environment into a file named requirements.txt. This is crucial for managing project dependencies, as it allows other developers to easily recreate the same environment by running pip install -r requirements.txt.


# Ans 5=>

# This command is used to save a list of all the Python packages and their exact versions that are installed in the current environment into a file named requirements.txt. This is crucial for managing project dependencies, as it allows other developers to easily recreate the same environment by running pip install -r requirements.txt.




#                               Section 3: Debugging & Workflow (4 Qs)



# Ans 1=>

# Print statements: Adding print() statements throughout the code to display the value of variables and track the program's flow.
# Using a debugger: Employing a dedicated debugging tool (like the one built into VS Code) to set breakpoints, step through the code line by line, and inspect the state of variables at each step.


# Ans 2=>

# Dot-files are configuration files on Unix-like operating systems (including Linux and macOS) that are hidden by default. They are used to store user-specific settings for various applications and the shell.
# .bashrc
# .gitconfig


# Ans 3=>

# Hard coding:- is the practice of embedding data directly into the source code. This makes the code inflexible, difficult to modify, and prone to errors. For example, writing if status == "success": instead of using a constant or variable.
# Using variables:- involves storing data in named memory locations that can be referenced and changed. This makes the code more flexible, readable, and easier to maintain. For example, SUCCESS_STATUS = "success" and then writing if status == SUCCESS_STATUS:.


# Ans 4=>

# Keyboard shortcuts are important because they allow developers to perform common actions much faster than using a mouse. This reduces context switching, keeps their hands on the keyboard, and streamlines their workflow, leading to increased efficiency.

# Example 1: Ctrl + C (or Cmd + C on Mac)
# Purpose: Copies selected text. This is a fundamental shortcut used for quick duplication of code.

# Example 2: Ctrl + Z (or Cmd + Z on Mac)
# Purpose: Undoes the last action. This is invaluable for quickly correcting mistakes without having to manually delete or retype code.




#                               Section 4: Coding Workflow & Best Practices (4 Qs)



# Ans 1=>

# Refactoring is the process of restructuring existing computer code—changing the factoring—without changing its external behavior. Its purpose is to improve the design of the code, making it more readable, maintainable, and easier to understand.
# Example Scenario: A developer has a function that is very long and performs multiple, unrelated tasks (e.g., fetching data, processing it, and saving it to a database). Refactoring would involve breaking this large function into three smaller, more focused functions: one for fetching data, one for processing, and one for saving. This makes the code easier to test and maintain


# Ans 2=>

# Ctrl + P: Quickly opens the file switcher to navigate between files without using the mouse.
# Ctrl + F: Quickly finds the word or any character like marks or ma in whole file.


# Ans 3=>

# Developers should maintain code snippets or templates to save time and reduce repetitive typing. Snippets are reusable blocks of code for common patterns (e.g., function definitions, loops, class structures). By using them, developers can write consistent code and avoid manually re-typing boilerplate, which improves efficiency and reduces the chance of typos.


# Ans 4=>

# Dot-file: .env
# Function: It is used to store environment variables (such as API keys, database credentials, or configuration settings) for a project. Instead of hard-coding these sensitive values directly in the source code, they are placed in a .env file, which can be easily ignored by version control systems like Git, improving security and portability.



#                                   PART B: Coding Questions (22 Questions)
#                                        Section 5: Easy Level (10 Qs)



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
