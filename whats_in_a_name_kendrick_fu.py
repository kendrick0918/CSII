

def main():
  fullname = input("what is your name? (first, middle, last)") 

  while True:

    print("Choose an option:")
    functionchoice = input("Select an option (1-10), Choose 11 to break the code")
    if functionchoice == "1":
      printname()
    elif functionchoice == "2":
      reversename()
    elif functionchoice == "3":
      numberofvowels()
    elif functionchoice == "4":
      consonant_frequency()
    elif functionchoice == "5":
      print(firstname(fullname))
    elif functionchoice == "6":
       print(lastname(fullname))
    elif functionchoice == "11":
      break
    else:
      print("Invalid Choice, Please try again")





def printname(fullname):
        print(fullname)

def reversename():
    return text[::-1]

def numberofvowels(fullname):
    vowels = 0
    vowels = ['a','e','i','o','u']
    for letter in fullname:
        if letter in ['a','e','i','o','u']:
            vowels += 1
    return vowels

def consonant_frequency(fullname):
    totalconsonants = 0
    totalconsonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    for letter in fullname:
        if letter in ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']:
            totalconsonants += 1
    return totalconsonants

def firstname(fullname):
    listofletters = []
    for i in fullname:
       if i == " ":
          break
       listofletters.append(i)
    return "".join(listofletters)
  


def lastname(fullname):
    list_of_letters = []
    for i in fullname:
       if i == " ":
          break
       list_of_letters.append(i)
    return "".join(list_of_letters)

def middlename(fullname):
    space = 0
    for char in fullname:
       if char == " ":
        space +=1
       if space <=1:
          middle = "Middle Name not Found"
       else:
          beg = 0
          end = len(fullname)-1
          for i in range(0, len(fullname)):
             if fullname[i] == '':
                beg +=1
                break
             else:
                beg = beg+1


           
          for i in range(len(fullname)-1,-1,-1):
             if fullname[i] == '':
                break
             else:
                end = end-1
             middle = fullname[beg:end]
             return middle

    


  

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
def if_palindrome():
    pass
def arrayofcharacters():
    pass
def menu():
    pass
def titledistinction():
    pass


main()
    