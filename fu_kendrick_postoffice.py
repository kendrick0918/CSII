import random

'''
Author: Kendrick Fu
Sources: Mr. Campbell, Julian Toub
Bugs: No bugs currently, but had issues with if input wasn't an interger or float, fixed
Description: Calculates and returns cost of shipping a certain type of package
Date: 10/23/25




pulls userinput from length, width, height for package. 

if-elifs are just specifications for making different categories of shipping

1+2(w+h)works for large envoelope - look at the instructions




'''

def getsize(l,w,h):
    """
    Determines the classifcation of mail based on its dimensions
    
    l (float) length
    w (float) width
    h (float) height

    returns: 
    str: the category of the mail
        then returns unmailable if dimensions exceed limits
    """
    if 3.5 <= l <= 4.25 and 3.5 <= w <= 6 and 0.007 <= h <= 0.016:
        return "Post Card"
    elif 4.25 < l <= 6 and 6 < w <= 11.5 and 0.007 <= h <= 0.015:
        return "Large Post Card"
    elif 3.5 <= l <= 6.125 and 5 <= w <= 11.5 and 0.016 < h <= 0.25:
        return "Envolepe"
    elif 6.125 < l <= 24 and 11 <= w <= 18 and 0.25 < h <= 0.5:
        return "Large Envelope"
    elif l + 2 * (w+h) <= 84:
        return "Package"
    elif l + 2 * (w+h) <= 130:
        return "Large Package"
    else:
        return "Unmailable"
    
'''
function for determining zipcode codes

Parameters:
zipcode (int or str): the zip code 

returns:
int: the zone number (1-6). returns 0 if the zip code is invalid
'''
def get_zip (zipcode):
   
    try:
        zipcode = int(zipcode)
    except ValueError:
        return 0

    if 0 <= zipcode <= 6999:
        return 1
    elif 7000 <= zipcode <= 19999:
        return 2
    elif 20000 <= zipcode <= 35999:
        return 3
    elif 36000 <= zipcode <= 62999:
        return 4
    elif 63000 <= zipcode <= 84999:
        return 5
    elif 85000 <= zipcode <= 99999:
        return 6
    else:
        return 0  # Invalid zip
    
def calculatecost(mailtype, distance):

    """
    Calculates shipping cost based on mail type and zone distance
    
    Parameters:
    mailtype (string) category of the mail
    distance (int) The positive/absolute difference between the starting and ending zones.
    """

    if mailtype == "Post Card":
        return 0.20 + (0.03 * distance)
    elif mailtype == "Large Post Card":
        return 0.37 + (0.03 * distance)
    elif mailtype == "Envelope":
        return 0.37 + (0.04 * distance)
    elif mailtype == "Large Envelope":
        return 0.60 + (0.05 * distance)
    elif mailtype == "Package":
        return 2.95 + (0.25 * distance)
    elif mailtype == "Large package":
        return 3.95 + (0.35 * distance)
    else:
        return 0.00

'''
Main function that pulls all functions and takes user input and spits output
data splits the different inputs when a comma is placed
If the data is not equal to 5 inputs (only asks for 5 inputs)
Then try if input is a float for all the first 3 data points, (float because lenght, width, and height can have decimal points)
Then try if input is an int for the zipcode inputs, (int becuase zipcode can't be decimal points)
If its not, then ValueError tells the user their inpug is invalid
defines zoneto, zonefrom, and distance that would be pluged into the calculate cost function
Then pull the calculate cost and print
'''

def main():
  
    #trying to loop the program 5 times 
    for i in range(5): 
        print(f"Run{i+1} of 5")
        data = input("Enter data (Length, Width, Height, ZipTo, ZipFrom)") 
        data = data.split (",")
        
        if len(data) != 5:
            print("invalid input, input 5 values")
            return
        try:
            l = float(data[0])
            w = float(data[1])
            h = float(data[2])
            zipto = int(data[3])
            zipfrom = int(data[4])
        except ValueError:
            print("Invalid Input, Input must be a number")
            return
        zone_to = get_zip(zipto)
        zone_from = get_zip(zipfrom)
        distance = abs(zone_to - zone_from)
        

        mailtype = getsize(l,w,h)
        distance = abs(get_zip(zipto)- get_zip(zipfrom))
        cost = calculatecost(mailtype, distance)
       

        
        cost = str(cost).lstrip('0')

        if len(cost) == 2:
            cost = cost + "0"


        print(cost)
     
if __name__ == "__main__":
    main()