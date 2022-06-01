from employee import Employee                   # IMPORT LOCAL FILE CLASS (employee.py)


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
            print("[U]pdate")
            print("[D]elete")
            print("[E]xit")
            print("---------")
            menuChoice = input("Choice: ")


            if menuChoice == 'c':
                create_data()                        
            elif menuChoice == 'r':    
                read_data(employee_list)
            elif menuChoice == 'u':
                pass 
            elif menuChoice == 'd':
                pass
            elif menuChoice == 'e':
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
    # Input x employees
    totalEmployees = int(input("How many employees? "))

    # Loop to iterate through each employee
    for i in range(totalEmployees): 
        # Input   
        print("\n--------------------")
        print('Enter the data for employee', int(i + 1))   
        empID = int(input("ID?   "))
        empLast = input("Last name?   ")
        empFirst = input("First name?   ")
        empMiddle = input("Middle name?   ")
        print("--------------------\n")
        print()


        
        worker = Employee(empID, empLast, empFirst, empMiddle)                  # Creates the object to store the atributes in
        employee_list.append(worker)                                            # append the data into a list
    return employee_list


def read_data(employee_list):
    for employee in employee_list:
        print("ID:               ", employee.get_empID())
        print("Last name:        ", employee.get_empLast())
        print("First name:       ", employee.get_empFirst())
        print("Middle name:      ", employee.get_empMiddle(),sep='')
        print()

# FUNCTION TO EXIT THE PROGRAN
def exit_program():
    print("THANK YOU FOR USING THE SYSTEM!")
    exit()










""""" 
    MAIN CODE 
"""""
# Start program
main_menu()
