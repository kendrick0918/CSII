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
        print("8. Get Initals")
        print("9. Hyphen")
        print("10. Lowercase")
        print("11. Uppercase")
        print("12. Exit")
        

        functionchoice = input("Select an option (1-12), Choose 12 to break the code") 

        if functionchoice == "1":
            print("name:", printname(fullname))
        elif functionchoice == "2":
            print("reversed name", reversename(fullname))
        elif functionchoice == "3":
            print("number of vowels in name", numberofvowels(fullname))
        elif functionchoice == "4":
            print("consonant frequency:",consonant_frequency(fullname))
        elif functionchoice == "5":
            print("first name:", firstname(fullname)) #remember to print the function, because its stored not printed. 
        elif functionchoice == "6":
            print("last name:", lastname(fullname))
        elif functionchoice == "7":
            print("middle name:", middlename(fullname))
        elif functionchoice == "8":
            print("Initals:", getinitals(fullname))
        elif functionchoice == "9":
            print("Hyphen:", if_hyphen(fullname))
        elif functionchoice == "10":
            print("Lowercase:", lowercase(fullname))
        elif functionchoice == "11":
            print("uppercase:", uppercase(fullname))
        elif functionchoice == "12":
            break
        else:
            print("Invalid Choice, Please try again") #invalid choice

def printname(fullname): # prints fullname
    print(fullname)

def reversename(fullname):
    reversed_name = " "
    for i in range(len(fullname)-1,-1,-1):
        reversed_name += fullname[i]
    return reversed_name

def numberofvowels(fullname): #takes a string and returns the number of vowels in it.
    #bug here, doesnt print output for some reason
    vowels = 0
    vowels = ['a','e','i','o','u']

    for letter in fullname:
        output = ""
        if letter in ['a','e','i','o','u']:
            vowels += 1
    return output

def consonant_frequency(fullname): #takes a string and counts the number of consonants in it. 
    #slight bug here, if you put a number it just prints the whole list
    totalconsonants = 0
    totalconsonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    
    for letter in fullname:
        if letter in ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']:
            totalconsonants += 1
    return totalconsonants

def get_names(fullname):
    names = []
    name = ''

    for letter in fullname:
        if letter == ' ':
            names.append(name)
            name = ''
        else:
            name += letter
    names.append(name)
    return names

def join_names(names, char):
    name = ''

    for n in names:
        name += n + char
    
    return name[:-1]

def firstname(fullname): #takes a string(users fullname input) and isolates the first name and returns it.
    names = get_names(fullname)
    return names[0]

def lastname(fullname): #takes a string(user fullname input) isolates the last name and returns it. 
    names = get_names(fullname)
    return names[-1]

def middlename(fullname):
    names = get_names(fullname)
    return join_names(names[1:-1], ' ')
             
def getinitals(fullname):
    initials = ''
    names = get_names(fullname)

    for name in names:
        initials += uppercase(name[0])
    return initials

def if_hyphen(fullname):
    return '-' in lastname(fullname)
def lowercase(fullname):
    new_name = ''
    for letter in fullname:
        if ord(letter) > 64 and ord(letter) < 91:
            num = ord(letter)
            num += 32
            letter = chr(num)
        new_name += letter
    return new_name
def uppercase(fullname):
    ''''''
    newname = ''
    for letter in fullname:
        if ord(letter) > 96 and ord(letter) < 123:
            num = ord(letter)
            num -=32
            letter = chr(num)
        newname += letter
    return newname
    #use lowercase function as reference with numbers 96 to 123 and subtract 32
def create_random_name(fullname):
    fn = firstname(fullname)
    fn_list = list(fn)
    #use random.shuffle to scramble list
    #return the list joined as a string
def if_palindrome(string):
    return reversename(string) == string
def arrayofcharacters():
    pass
def menu():
    pass
def contains_title(fullname):
    ''''''
    titles = ['Dr.', 'Sir', 'Esq', 'Ph.d', ' ']
    for title in titles:
        if title in get_names(fullname):
            return True
    return False
    #titles = ['Dr.', 'Ph.D', 'Ms.'....]
    #for title in titles:
        #if title in get_names(fullname):
            #return True
    #return False
def remove_title(fullname):
    ''''''

    #titles = ['Dr.', 'Ph.D', 'Ms.'....]
    #names = get_names(fullname)
    #for title in titles:
        #if title in names:
            #names.remove(title)
    #return names

main()
    