

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

def load_display_data():

    """
    Extracts the first 10 passenger records from the Titanic dataset and writes them to a new file.
    Skips the header row and saves rows 2-11.

    Args:
        None

    Returns:
        None. Writes output to 'first_ten.csv'.


    """

    input = open("titanic.csv")

    with open('first_ten.csv', 'w') as outfile:

        counter = 0

        for line in input:
            counter = counter +1
            if counter > 1 and counter < 12:
                outfile.write(line)


def getGender():

    input = open("titanic.csv")

    with open('genders.csv', 'w') as outfile:
        '''
        Counts the number of male and female passengers in the dataset and writes the counts to a CSV file.
        Also prints the counts to the console.

        Args:
            infile: An open file object containing passenger data in CSV format.

        Returns:
            None. Writes output to 'genders.csv' and prints counts to console.

        '''
       
        male_count = 0
        female_count = 0
       
        for line in input:                         #input file
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

def calculate_basic_stats():

    
    '''
    Calculates total passenger count and number of survivors from the Titanic dataset.
    Writes statistics to a CSV file with instructions for calculating survival rate.

    Args:
        None

    Returns:
        None. Writes output to 'calculate_basic_stats.csv'.

    '''
    
    # TODO: Calculate total passengers, survivors, and survival rate
    # Hint: Find the index of 'Survived' column in headers
    
    input = open("titanic.csv")
    total_passengers = 0
    total_survived = 0
    with open("calculate_basic_stats.csv", "w") as outfile:

        for line in input:
            fields = line.strip().split(',')

            total_passengers = total_passengers + 1

            survived = fields[1]

            if survived == "1":
                total_survived += 1

        outfile.write("Total Passengers" + "," + "Survivors")
        outfile.write("\n")
        outfile.write(str(total_passengers) + "," + str(total_survived))
        outfile.write("\n")
        outfile.write("Make a pie graph to see the survival rate Calculation is: total_survived/total_passengers * 100")
    
    



def write_surv():

    '''
    Calculates and writes the number of survivors and total passengers to a CSV file.
    Counts all passengers and those who survived (Survived = 1).

    Args:
        None

    Returns:
        None. Writes output to 'write_surv.csv'.

    '''

    input = open("titanic.csv")
    

    with open('write_surv.csv', 'w') as outfile:
       
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
                total_pass+=1
           
        outfile.write("Survivors" + "," + " Total Passengers")
        outfile.write("\n")
        outfile.write(str(survivors) + "," + str(total_pass))

        input.close()
        outfile.close()
    
def write_first_class():
    
    '''
    Filters and writes all first-class passenger records (Pclass = 1) to a CSV file.
    Includes all columns from the original dataset for matching passengers.

    Args:
        None

    Returns:
        None. Writes output to 'write_first_class.csv'.
    '''

    # TODO: Filter first-class passengers and write to file
    # Include survival rate at the top
    with open('write_first_class.csv', 'w') as outfile:
       
        input = open("titanic.csv")
        for line in input:                         #input file
            fields = line.strip().split(',')
       
            pclass = fields[2]                         #Pclass column in input file
           
            if pclass == "1":
                outfile.write(line)



def write_children():
    '''
    Filters and writes all passenger records for children under 18 years old to a CSV file.
    Skips records with missing age data. Includes all columns from the original dataset.

    Args:
        None

    Returns:
        None. Writes output to 'write_children.csv'.

    '''

    with open('write_children.csv', 'w') as outfile:
       
        input = open("titanic.csv")
        input.readline()
        for line in input:                         #input file
            
            fields = line.strip().split(',')
       
            age = fields[6]                         #Age column in input file
           
            if age != "" and float(age) < 18:
                outfile.write(line)


def generate_analysis_report():
    '''
    Generates a comprehensive CSV report with survival statistics broken down by passenger class,
    gender, and average age. Calculates survival rates as percentages for each category.

    Args:
        None

    Returns:
        None. Writes formatted analysis report to 'Generate_analysis_report.csv'.

    '''

    # TODO: Calculate survival rates by class and gender
    # TODO: Calculate average ages
    # TODO: Write formatted report to file
    with open('Generate_analysis_report.csv','w') as outfile:

        
        
        total_passengers = 0
        total_survived = 0

        firstclasstotal = 0
        firstclasssurv = 0
        secondclasstotal = 0
        secondclasssurv = 0
        thirdclasstotal = 0
        thirdclasssurv = 0

        male_total = 0
        male_surv = 0
        female_total = 0
        female_surv = 0

        age_sum = 0
        age_count = 0


        input = open('titanic.csv')

        input.readline()

        for line in input:
            fields = line.strip().split(",")

            pclass = fields[2]
            gender = fields[4]
            age = fields[6]
            survived = fields[1]

            

            if survived == "1":
                total_survived += 1

            if pclass == "1":
                firstclasstotal += 1
                if survived == "1":
                    firstclasssurv += 1
            elif pclass == "2":
                secondclasstotal += 1
                if survived == "1":
                    secondclasssurv += 1
            elif pclass == "3":
                thirdclasstotal += 1
                if survived == "1":
                    thirdclasssurv += 1

            if gender == "male":
                male_total += 1
                if survived == "1":
                    male_surv += 1
            elif gender == "female":
                female_total += 1
                if survived == "1":
                    female_surv += 1

            if age != "":
                try:
                    age_sum += float(age)
                    age_count += 1
                except ValueError as e:
                    print(f"Error converting age '{age}' to float: {e}")
                    

        outfile.write("Category,Total,Survived,Survival Rate")
        outfile.write("\n")
        if total_passengers > 0:
            outfile.write("Overall," + str(total_passengers) + "," + str(total_survived) + "," + str(total_survived/total_passengers * 100))
        if firstclasstotal > 0:
            outfile.write("\n")
            outfile.write("Class 1," + str(firstclasstotal) + "," + str(firstclasssurv) + "," + str(firstclasssurv/firstclasstotal * 100))
        outfile.write("\n")
        if secondclasstotal > 0:
            outfile.write("Class 2," + str(secondclasstotal) + "," + str(secondclasssurv) + "," + str(secondclasssurv/secondclasstotal * 100))
        outfile.write("\n")
        if thirdclasstotal > 0:
            outfile.write("Class 3," + str(thirdclasstotal) + "," + str(thirdclasssurv) + "," + str(thirdclasssurv/thirdclasstotal * 100))
        outfile.write("\n")
        if male_total > 0:
            outfile.write("Male," + str(male_total) + "," + str(male_surv) + "," + str(male_surv/male_total * 100))
        outfile.write("\n")
        if female_total > 0:
            outfile.write("Female," + str(female_total) + "," + str(female_surv) + "," + str(female_surv/female_total * 100))
        outfile.write("\n")
        if age_count > 0:
            outfile.write("Average Age," + str(age_sum/age_count))

def main():
    '''
    Main program loop that presents a menu system for executing various Titanic dataset analysis functions.
    Continuously prompts user for function selection until they choose to exit.

    Args:
        None

    Returns:
        None

    '''

    while True:

        print("Function Choices:")
        print("1. load_display_data ")
        print("2. getGender ")
        print("3. calculate_basic_stats ")
        print("4. write_surv ")
        print("5. write_first_class ")
        print("6. write_children ")
        print("7. generate_analysis_report ")
        print("8. End Code ")
        choice = input("choose your function: 1-10") #make changes later
        
        if choice == "1":
            load_display_data()
        if choice == "2":
            getGender()
        if choice == "3":
            calculate_basic_stats()
        if choice == "4":
            write_surv()
        if choice == "5":
            write_first_class()
        if choice == "6":
            write_children()
        if choice == "7":
            generate_analysis_report()
        if choice == "8":
            break

main()