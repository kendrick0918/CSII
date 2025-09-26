import random

def main():
    fullname = input("what is your name? (first, middle, last)") #user input

    while True: #gives users menu of how to modify their input, and has them choose their functions
        print("1. Print full name")
        print("2. Reverse name")
        print("3. Count number of vowels")
        print("4. Count number of consonants")
        print("5. Show first name")
        print("6. Show last name")
        print("7. Show middle name")
        print("11. Exit")

        functionchoice = input("Select an option (1-10), Choose 11 to break the code") 

        if functionchoice == "1":
            print("name:", printname(fullname))
        elif functionchoice == "2":
            print("reversed name", reversename(fullname))
        elif functionchoice == "3":
            print("number of vowels in name", numberofvowels(fullname))
        elif functionchoice == "4":
            print("consonant frequency:",consonant_frequency(fullname))
        elif functionchoice == "5":
            print("first name:", print(firstname(fullname))) #remember to print the function, because its stored not printed. 
        elif functionchoice == "6":
            print("last name:", print(lastname(fullname)))
        elif functionchoice == "7":
            print("middle name:",print(middlename(fullname)))
        elif functionchoice == "11":
            break
        else:
            print("Invalid Choice, Please try again") #invalid choice

def printname(fullname): # prints fullname
        print(fullname)
'''
    prints the fullname

    Args:
        fullname(string): user input name
    
    Returns:
        fullname(string): user input name

    Raises:
        Error: Description of the error 
    '''

def reversename(fullname):
    return fullname[::-1] #reverses name by taking a string and reversing it
'''
    reverses name by taking a string and reversing it

    Args:
        vairable(type): Description of variable.
    
    Returns:
        variable(type): Description of variable.  

    Raises:
        Error: Description of the error 
    '''

def numberofvowels(fullname): #takes a string and returns the number of vowels in it.
    vowels = 0
    vowels = ['a','e','i','o','u']
    for letter in fullname:
        if letter in ['a','e','i','o','u']:
            vowels += 1
    return vowels
'''
    takes a string and returns the number of vowels in it

    Args:
        vairable(type): Description of variable.
    
    Returns:
        variable(type): Description of variable.  

    Raises:
        Error: Description of the error 
    '''
def consonant_frequency(fullname): #takes a string and counts the number of consonants in it. 
    totalconsonants = 0
    totalconsonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    for letter in fullname:
        if letter in ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']:
            totalconsonants += 1
    return totalconsonants
'''
    takes a string and counts the number of consonants in it

    Args:
        vairable(type): Description of variable.
    
    Returns:
        variable(type): Description of variable.  

    Raises:
        Error: Description of the error 
    '''
def firstname(fullname): #takes a string(users fullname input) and isolates the first name and returns it.
    first_name = ""
    for char in fullname:
       if char == " ":
          break
       first_name += char
    return first_name

    '''
    takes a string(users fullname input) and isloates the first name and returns it. 

    Args:
        vairable(type): Description of variable.
    
    Returns:
        variable(type): Description of variable.  
    '''


def lastname(fullname): #takes a string(user fullname input) isolates the last name and returns it. 
    
    lastspace = -1
    for i in range(len(fullname)-1, -1 ,-1):
       if fullname[i] == " ":
          lastspace = i
          break
       if lastspace == -1:
          print("last name not found")
       lastname = ""
       for i in range(i+1, len(fullname)):
          lastname += fullname[i]
    return lastname
'''
    takes a string(user fullname input) and isloates the last name and returns it. 

    Args:
        fullname(string): user input name
    
    Returns:
        variable(type): Description of variable.  
    '''

def middlename(fullname):
    space = 0
    for char in fullname:
       if char == " ":
        space +=1
    
       if space < 2:
          return "Middle Name not Found"
       else:
          beg = 0
          end = 0

          for i in range(len(fullname)):
             if fullname[i] == ' ':
                beg = i+1
                break
             else:
                beg+=1
             for i in range(len(fullname),0, -1):
                if fullname [i-1] == " ":
                   end = i
                   break
             

    


  

def getinitals(fullname):
    intials = ""
    for word in name.split():
        if word: #makes sure that it's not an empty string
            initals += word[0].upper()
    return intials
def if_hyphen():
    pass
def convert_lowercase(fullname):
    pass
def convert_uppercase():
    pass
def create_random_name():
    pass
def if_palindrome(fullname):
    pass
def arrayofcharacters():
    pass
def menu():
    pass
def titledistinction():
    pass

main()
    