# 1. Write a script to count the number of words in a given string.

def count_words():
    input_string = input("Enter a sentence: ")
    print("Total words:", len(input_string.split()))
# count_words()
    
# 2. Take a sentence from the user and print:
# Total words
# Total characters (excluding spaces)

def count_words_and_char():
    input_string = input("Enter a sentence: ")
    print("Total words:", len(input_string.split()))
    print("Total char:", len(input_string.replace(" ", "")))
# count_words_and_char()

# 3. Write a program to simulate a simple calculator (add, subtract, multiply, divide).

def simple_calculator():
    print ("Simple Calculator")
    print ("1. To Add  (+) ")
    print ("2. To Subtract (-)")
    print ("3. To Multiply (*)")
    print ("4. To Divide   (/) ")
    choice = input("Enter your choice (1/2/3/4): ")
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    if choice == '1':
        print("Result:", num1 + num2)
    elif choice == '2':
        print("Result:", num1 - num2)
    elif choice == '3':
        print("Result:", num1 * num2)
    elif choice == '4':
        if num2 == 0:
            print("Division by zero is not allowed.")
        else:
            print("Result:", num1 / num2)
    else:
        print("Invalid choice")
simple_calculator()
# 4. Take a comma-separated list of integers from input, then print:
# Sorted list
# Sum of numbers
# 5. Write a script that reads a text file and counts how many times the word “Python” appears.
# 6. Write a program to generate a multiplication table for a given number up to 10.
# 7. Create a script that prints the current working directory using os module.
# 8. Write a program to create and activate a virtual environment using Python code