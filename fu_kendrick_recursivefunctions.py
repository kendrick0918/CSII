
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

Tester: Jackson Lieberman
Bugs:
1. error in sum of digits -- ex: input = 67 and output = 13.7
2. error in product of digits -- ex: input = 67 and output = 46.9
3. code crashes when an input that isn't acepted is given
'''

def get_int(userinput):
    '''
    Description: Gets an integer from the user and keeps asking until a valid
    integer is entered.

    Args:
        prompt(str): The message shown to the user

    Returns:
        int: A valid integer entered by the user
    '''
    while True:
        try:
            return int(input(userinput))
        except ValueError:
            print('Invalid input. Please enter an integer.')

def factorial(n):
    '''
    Description: Finds the factorial of a number.

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
    Descrpition: Finds the sum of all integers from 1 to n.

    Args:
        n(int): The ending number.

    Returns:
        The sum from 1 to n.
    '''
    if n == 0:
        return 0
    return n + summation(n - 1)



def power(base, exponent):
    '''
    Descrpition: Finds base number raised to a power.

    Args:
        base(int): The base number.
        exponent(int): The exponent.

    Returns:
        base number raised to exponent.
    '''

    if exponent == 0:
        return 1
    return base * power(base, exponent= - 1)



def fibonacci(n):
    '''
    Descrpition: Finds the nth Fibonacci number.

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


def sum_digits(n):
    '''
    Description: Finds the sum of all digits in a number.

    Args:
        n(int): The number whose digits will be added.

    Returns:
        int: The sum of the digits.
    '''
    
    if n < 10:
        return n
    return (n % 10) + sum_digits(n // 10) #bug only fixed if I used // instead of /



def product_digits(n):
    '''
    Description: Finds the product of all digits in a number

    Args:
        n(int): The number whose digits will be multiplied.

    Returns:
        The product of the digits
    '''
    if n < 10:
        return n
    return (n % 10) * product_digits(n // 10) #bug only fixed if I used // instead of /



def multiply(a, b):
    '''
    Description: Multiplies two whole numbers

    Args:
        a(int): The first number
        b(int): The second number

    Returns:
        The product of a and b
    '''
    if b == 0:
        return 0
    return a + multiply(a, b - 1)



def range_sum(start, end):
    '''
    Description: Finds the sum of all numbers in the range 

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






# Menu
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
        
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            n = get_int("Enter a number: ")
            print("Factorial =", factorial(n))

        elif choice == "2":
            n = get_int("Enter a number: ")
            print("Summation =", summation(n))

        elif choice == "3":
            base = get_int("Enter the base: ")
            exponent = get_int("Enter the exponent: ")
            print("Power =", power(base, exponent))

        elif choice == "4":
            n = get_int("Enter n: ")
            print("Fibonacci =", fibonacci(n))

        elif choice == "5":
            n = get_int("Enter a number: ")
            print("Sum of Digits =", sum_digits(n))

        elif choice == "6":
            n = get_int("Enter a number: ")
            print("Product of Digits =", product_digits(n))

        elif choice == "7":
            a = get_int("Enter first number: ")
            b = get_int("Enter second number: ")
            print("Product =", multiply(a, b))

        elif choice == "8":
            start = get_int("Enter start of range: ")
            end = get_int("Enter end of range: ")
            print("Range Sum =", range_sum(start, end))

        elif choice == "0":
            print("thank you for playing")
            break

        else:
            print("Invalid choice. Try again.")


main()