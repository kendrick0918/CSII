import random

'''

pulls userinput from lenght, width, height for package. 

if-elifs are just specifications for making different categories of shipping

1+2(w+h)works for large envoelope - look at the instructions




'''

def getsize(l,w,h):
    
    if 3.5 <= l <= 4.25 and 3.5 <= w <= 6 and 0.007 <= h <= 0.016:
        return "Post_card"
    elif 4.25 < l <= 6 and 6 < w <= 11.5 and 0.007 <= h <= 0.015:
        return "Large post card"
    elif 3.5 <= l <= 6.125 and 5 <= w <= 11.5 and 0.016 < h <= 0.25:
        return "Envelope"
    elif 6.125 < l <= 24 and 11 <= w <= 18 and 0.25 < h <= 0.5:
        return "Large envelope"
    elif l + 2 * (w+h) <= 84:
        return "Package"
    elif l + 2 * (w+h) <= 130:
        return "Large package"
    else:
        return "unmailable"
    
'''
function for determining zipcode codes

first zipcode has to be an integer always (not a float because no decimals)

Then define specifications for different zones to ship to
'''
def get_zip (zipcode):
   
    zipcode = int(zipcode)

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
'''
this function calculates cost

takes the mailtype (if its a certain type decides how much it costs to ship)
then takes the distance from zipcode (first zone and last zone) (defined below in main)
Mathmathical calculations for how muc it costs

'''
    
def calculatecost(mailtype, distance):
    if mailtype == "Post card":
        return 0.40 + (0.05 * distance)
    elif mailtype == "Large post card":
        return 0.55 + (0.07 * distance)
    elif mailtype == "Envelope":
        return 0.70 + (0.10 * distance)
    elif mailtype == "Large envelope":
        return 1.00 + (0.15 * distance)
    elif mailtype == "Package":
        return 3.00 + (0.50 * distance)
    elif mailtype == "Large package":
        return 5.00 + (0.75 * distance)
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

    data = input("enter data")
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
    print("Mail Type:", mailtype)
    print("Zone Distance:", distance)
    print("Cost of Delivery: $", cost)

if __name__ == "__main__":
    main()