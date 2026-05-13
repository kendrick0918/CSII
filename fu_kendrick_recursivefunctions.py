
'''
fu_kendrick_recursive_functions.py

Description: Recursive functions program with choices that has a menu

Features: 
factorial, 
summation, 
power/exponent, 
fibonacci, 
sum of numbers digits
product of numbers digits
product of two numbers
sum of numbers in range
reverse digits in number

Log: 1.2

Bugs: no bugs after testing 
'''

def factorial(n):
     '''
    Finds the factorial of a number.

    Args:
        n(int): The number to find the factorial of.

    Returns:
        The factorial of n.
    '''
    if n == 0:
        return 1
    return n * factorial(n - 1)



def summation(n):
    '''
    Finds the sum of all integers from 1 to n.

    Args:
        n(int): The ending number.

    Returns:
        The sum from 1 to n.
    '''
    if n == 0:
        return 0
    return n + summation(n - 1)


# 3. Power and Exponential function (a^n)
def power(a, n):
    '''
    Finds base number raised to a power.

    Args:
        base(int): The base number.
        exponent(int): The exponent.

    Returns:
        base number raised to exponent.
    '''

    if n == 0:
        return 1
    return a * power(a, n - 1)


# 4. Fibonacci numbers
def fibonacci(n):
    '''
    Finds the nth Fibonacci number.

    Args:
        n(int): The position in the Fibonacci sequence.

    Returns:
        The nth Fibonacci number.
    '''
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# % mean 
# 5. Sum of a number's digits
def sum_digits(n):
    '''
    Finds the sum of all digits in a number.

    Args:
        n(int): The number whose digits will be added.

    Returns:
        int: The sum of the digits.
    '''

    #  % is modulus. It returns the remainder.
    # Example: 123 % 10 = 3
    
    if n < 10:
        return n
    return (n % 10) + sum_digits(n / 10)


# 6. Product of a number's digits
def product_digits(n):
    '''
    Finds the product of all digits in a number

    Args:
        n(int): The number whose digits will be multiplied.

    Returns:
        The product of the digits
    '''
    if n < 10:
        return n
    return (n % 10) * product_digits(n / 10)


# 7. Product of two whole numbers (using repeated addition)
def multiply(a, b):
    '''
    Multiplies two whole numbers

    Args:
        a(int): The first number
        b(int): The second number

    Returns:
        The product of a and b
    '''
    if b == 0:
        return 0
    return a + multiply(a, b - 1)


# 8. Sum of numbers in a range
def range_sum(start, end):
    '''
    Finds the sum of all numbers in the range 

    Args:
        start(int): The first number in the range.
        end(int): The last number in the range.

    Returns:
        The sum of all numbers from start to end
    '''
    if start > end:
        return 0
    if start == end:
        return start
    return start + range_sum(start + 1, end)


# 9. Reverse the digits in a number
def reverse_number(n, rev=0):
    '''
    Reverses the digits of a number using recursion

    Args:
        n(int): The original number.
        reversed_num(int): The reversed number being built.

    Returns:
        The digits of n in reverse order
    '''
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10) 


# Main menu
def main():
    #simple menu choice 
    while True:
        print("\nRecursive Algorithm Menu")
        print("1. Factorial")
        print("2. Summation")
        print("3. Power")
        print("4. Fibonacci")
        print("5. Sum of Digits")
        print("6. Product of Digits")
        print("7. Product of Two Numbers")
        print("8. Sum of Numbers in a Range")
        print("9. Reverse a Number")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            n = int(input("Enter a number: "))
            print("Factorial =", factorial(n))

        elif choice == "2":
            n = int(input("Enter a number: "))
            print("Summation =", summation(n))

        elif choice == "3":
            a = int(input("Enter the base: "))
            n = int(input("Enter the exponent: "))
            print("Power =", power(a, n))

        elif choice == "4":
            n = int(input("Enter n: "))
            print("Fibonacci =", fibonacci(n))

        elif choice == "5":
            n = int(input("Enter a number: "))
            print("Sum of Digits =", sum_digits(n))

        elif choice == "6":
            n = int(input("Enter a number: "))
            print("Product of Digits =", product_digits(n))

        elif choice == "7":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Product =", multiply(a, b))

        elif choice == "8":
            start = int(input("Enter start of range: "))
            end = int(input("Enter end of range: "))
            print("Range Sum =", range_sum(start, end))

        elif choice == "9":
            n = int(input("Enter a number: "))
            print("Reversed Number =", reverse_number(n))

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


# Run the program
main()