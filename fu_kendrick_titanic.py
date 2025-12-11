

#titanic column indices (this improves code readability to help identify columns by name)
PASSENGERID = 0
SURVIVED = 1
PCLASS = 2
NAME = 3
SEX = 4
AGE = 5
SIBSP = 6
PARCH = 7
TICKET = 8
FARE = 9
CABIN = 10
EMBARKED = 11

def load_display_data(infile, rows):
    with open('first_ten.csv', 'w') as outfile:


    #Load and display data from the Titanic CSV file.
        passengers = []
        headers = []

        for line in infile:                         #input file
            fields = line.strip().split(',')

        #this removes the trailing whitespace

        for row in rows[1:11]:  # Read first 10 data rows
            passengers.append("".join(row))
        del passengers[0]
        print(passengers)

def getGender(infile):
    with open('genders.csv', 'w') as outfile:
       
       
        male_count = 0
        female_count = 0
       
        for line in infile:                         #input file
            fields = line.strip().split(',')
       
            sex = fields[5]                         #gender column in input file
           
            if sex == "male":
                male_count += 1
            elif sex == "female":
                female_count += 1
           
        outfile.write("Male" + "," + "Female")
        outfile.write("\n")
        outfile.write(str(male_count) + "," + str(female_count))
    
    print("Male survivors:", male_count, "Female Survivors:", female_count)

def calculate_basic_stats(headers, passengers):
    """
    Calculates and displays basic statistics about the passengers.
    
    Args:
        headers (list): List of column names
        passengers (list): List of passenger records (each record is a list)
    """
    survival_index = headers.index('Survived')
    # TODO: Calculate total passengers, survivors, and survival rate
    # Hint: Find the index of 'Survived' column in headers
    total = len(passengers)
    for p in passengers:
        if p[survival_index] == "1":
            survivors += 1
    #caculate the survival rate
    if total > 0:
        survivalrate = (survivors / total * 100)
    else:
        survivalrate = 0
    #total = 0
    #survivors = 0
    
    print("=== BASIC STATISTICS ===")
    print(f"Total Passengers: {total}")
    print(f"Survivors: {survivors}")
    print(f"Survival Rate: {survivalrate:.1f}%")
    print()


def write_surv(input):
    with open('genders.csv', 'w') as outfile:
       
        total_pass = 0
        survivors = 0
       
        for line in input:                         #input file
            fields = line.strip().split(',')
       
            lived = fields[1]                         #gender column in input file
            name = fields[3]
           
            if lived == "1":
                survivors += 1
                total_pass  +=1
            else:
                survivors
           
        outfile.write("Male" + "," + "Female")
        outfile.write("\n")
        outfile.write(str(male_count) + "," + str(female_count))





def write_survivors(headers, passengers, output_file):
    """
    Writes information about all survivors to a file.
    
    Args:
        headers (list): List of column names
        passengers (list): List of passenger records
        output_file (str): Name of output file
    """
    # TODO: Write survivor information to file
    # Format: PassengerId,Name,Age,Class
    # Use headers to find the correct indices
    pid_data = PASSENGERID
    name_data = NAME
    age_data = AGE
    survivalamount = SURVIVED

    with open(output_file, 'w') as outfile: 
        #Writing the Header
        outfile.write("PassengerId, Name, Age, Class")

        survivalcount = 0
        for p in passengers:
            #checking for suvivor
            if len(p) > survivalamount and p[survivalamount] == "1":
                #take the data and format it
                pid = p[pid_data]
                name = p[name_data]
                age = p[age_data]
                pclass = p[survivalamount]

                outfile.write(pid, name, age, pclass)
                survivorcount +=1
    print(f"Survivor Information Written to {output_file} ({survivorcount} records"),

    


def write_first_class(headers, passengers, output_file):
    """
    Writes information about first-class passengers to a file.
    
    Args:
        headers (list): List of column names
        passengers (list): List of passenger records
        output_file (str): Name of output file
    """
    # TODO: Filter first-class passengers and write to file
    # Include survival rate at the top
    with open('genders.csv', 'w') as outfile:
       
       
        male_count = 0
        female_count = 0
       
        for line in infile:                         #input file
            fields = line.strip().split(',')
       
            sex = fields[5]                         #gender column in input file
           
            if sex == "male":
                male_count += 1
            elif sex == "female":
                female_count += 1
           
        outfile.write("Male" + "," + "Female")
        outfile.write("\n")
        outfile.write(str(male_count) + "," + str(female_count))
    
    print("Male survivors:", male_count, "Female Survivors:", female_count)
    pass


def write_children(headers, passengers, output_file):
    """
    Writes information about passengers under 18 to a file.
    
    Args:
        headers (list): List of column names
        passengers (list): List of passenger records
        output_file (str): Name of output file
    """
    # TODO: Filter passengers under 18 and write to file
    # Remember: some ages might be missing!
    pass


def generate_analysis_report(headers, passengers, output_file):
    """
    Generates a comprehensive analysis report.
    
    Args:
        headers (list): List of column names
        passengers (list): List of passenger records
        output_file (str): Name of output file
    """
    # TODO: Calculate survival rates by class and gender
    # TODO: Calculate average ages
    # TODO: Write formatted report to file
    pass

def main():
    input_file = open('titanic.csv')
    rows = []
    input_file.seek(1)                  #move pointer of input file to top of file
    for line in input_file:
        rows.append(line.strip().split(','))

    #getGender(input_file)
    #load_display_data(input_file, rows)






main()