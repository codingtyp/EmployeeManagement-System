from employee import EMP                   # IMPORT LOCAL FILE CLASS (employee.py)


# Creates an empty list to store employee data
employee_list = []


# FUNCTION TO DISPLAY MENU
def main_menu():
    print("*********************************************************")
    print("*              EMPLOYEE MANAGEMENT SYSTEM               *")
    print("*********************************************************")
    print("")


    while True:
        try:
            print("[C]reate")
            print("[R]ead")
            print("[E]xit")
            print("---------")
            menuChoice = input("Choice: ")


            if menuChoice == 'C' or menuChoice == 'c':
                create_data()                        
            elif menuChoice == 'R' or menuChoice == 'r':    
                read_data(employee_list)
            elif menuChoice == 'E' or menuChoice == 'e':
                exit_program()
            else:
                print("\n")
                print(">> INVALID INPUT!")
                print("\n")
        except ValueError:
            print("\n")
            print(">> INVALID INPUT!")
            print("\n")





# FUNCTION TO TAKE USER INPUT, STORE IN THE OBJECT, THEN STORE IN A LIST
def create_data():    
    print()


    # Determine how many data will be entered
    while True:
        try:
            totalEmployees = int(input("How many employees?   "))
            print()
            break
        except ValueError:
            print("\n")
            print(">> INVALID INPUT!")
            print("\n")

    # Loop to iterate through each employee
    for i in range(totalEmployees): 
        # Input   
        print("-----------", int(i + 1), "-----------") 
        empID = int(input("ID?   "))
        empLast = input("Last name?   ")
        empFirst = input("First name?   ")
        empMiddle = input("Middle name?   ")
        empAge = int(input("Age?   "))
        print("-------------------------")
        print(">> Data successfully added!")
        print()
    

        empData = EMP(empID, empLast, empFirst, empMiddle, empAge)                      # Creates the object to store the atributes
        employee_list.append(empData)                                                    # append the data into a list
    return employee_list





# FUNCTION TO SIMPLY DISPLAY ALL DATA
def read_data(employee_list):  
    print("\n")


    if len(employee_list) == 0:
        print(">> No data found!\n\n")
    else:
        viewData = input("How do you like to view the data?  [l-ist/t-able]   ")

        if viewData == 'L' or viewData == 'l':
            print("\n")
            for employee in employee_list:
                print("+-----------------+--------------")
                print("|  ID             | ", employee.get_empID())
                print("|  Last name      | ", employee.get_empLast())
                print("|  First name     | ", employee.get_empFirst())
                print("|  Middle name    | ", employee.get_empMiddle())
                print("|  Age            | ", employee.get_empAge())
                print("+-----------------+--------------")
                print("\n")
        elif viewData == 'T' or viewData == 't':
            print("\n")
            print("+========+=======================+========================+")
            print ("{:<23} {:<20} {:<1}".
            format('|   ID   | ', 'NAME             |', 'Age  | '))
            print("+========+=======================+=========================+")

            for employee in employee_list:
                print ("   {:<14}{:<1}, {:<1} {:<13} {:<1}".format( employee.get_empID(), employee.get_empLast(), employee.get_empFirst(), employee.get_empMiddle(), employee.get_empAge()))
            print("\n")
        else:
            print("\n")
            print(">> INVALID INPUT!")
            print("\n")





# FUNCTION TO EXIT THE PROGRAN
def exit_program():
    print("THANK YOU VERY MUCH!")
    exit()










""""" 
    MAIN CODE 
"""""
# Start program
main_menu()
