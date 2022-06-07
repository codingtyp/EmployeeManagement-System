from pickle import TRUE
import employee


# Creates an empty list to store employee data
employee_list = []


# FUNCTION TO DISPLAY MENU
def main():
    print("*********************************************************")
    print("*              EMPLOYEE MANAGEMENT SYSTEM               *")
    print("*********************************************************")
    print("")


    while True:
        try:
            print("[C]reate")
            print("[R]ead")
            print("[D]elete")
            print("[E]xit")
            print("---------")
            menuChoice = input("Choice: ")


            if menuChoice == 'C' or menuChoice == 'c':
                create_data()                        
            elif menuChoice == 'R' or menuChoice == 'r':    
                read_data(employee_list)
            elif menuChoice == 'D' or menuChoice == 'd':
                delete_data(employee_list)
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
    print("\n")


    # Determine how many data will be entered
    while True:
        try:
            totalEmployees = int(input("How many employee/s?   "))
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
        empLN = input("Last name?   ")
        empFN = input("First name?   ")
        empMN = input("Middle name?   ")
        empAge = int(input("Age?   "))
        

        print("\n1. Human Resources")
        print("2. Information Technology")
        print("3. Administration")
        print("4. Accounting and Finance")
        print("5. Marketing and Sales")
        print("6. Customer Service")
        departmentChoice = int(input("Department?   "))

        if departmentChoice == 1:
            empDepartment = "Human Resources"
        elif departmentChoice == 2:
            empDepartment = "Information Technology"
        elif departmentChoice == 3:
            empDepartment = "Administration"
        elif departmentChoice == 4:
            empDepartment = "Accounting and Finance"
        elif departmentChoice == 5:
            empDepartment = "Marketing and Sales"
        elif departmentChoice == 6:
            empDepartment = "Customer Service"
        else:
            print()
            print(">> INVALID INPUT!")
            print()


        print("\n1. Head")
        print("2. Senior")
        print("3. Regular")
        print("4. New")
        print("5. Staff")
        print("6. Intern")
        positionChoice = int(input("Postition?   "))

        if positionChoice == 1:
            empPosition = "Head"
            empSalary = 200000
        elif positionChoice == 2:
            empPosition = "Senior"
            empSalary = 150000
        elif positionChoice == 3:
            empPosition = "Regular"
            empSalary = 100000
        elif positionChoice == 4:
            empPosition = "New"
            empSalary = 50000
        elif positionChoice == 5:
            empPosition = "Staff"
            empSalary = 25000
        elif positionChoice == 6:
            empPosition = "Intern"
            empSalary = 5000
        else:
            print()
            print(">> INVALID INPUT!")
            print()
        
        
        print()
        print(">> Data successfully added!")
        print()


        empData = employee.Worker(empID, empLN, empFN, empMN, empAge, empDepartment, empPosition, empSalary)       # Creates the object to store the atributes
        employee_list.append(empData)                                                                                       # append the data into a list
    
    
    return employee_list





# FUNCTION TO SIMPLY DISPLAY ALL DATA
def read_data(employee_list):  
    print("\n")


     # Check if there is atleast 1 data in the list
    if len(employee_list) == 0:
        print(">> No data found!\n\n")
    else:
        viewData = input("How do you like to view the data?  [l-ist/t-able]   ")


        # Determine what view to be display
        if viewData == 'L' or viewData == 'l':
            print("\n")
            for i in employee_list:
                print("+-------------------+-----------------------=")
                print("|  ID               | ", i.get_empID())
                print("|  Last name        | ", i.get_empLN())
                print("|  First name       | ", i.get_empFN())
                print("|  Middle name      | ", i.get_empMN())
                print("|  Age              | ", i.get_empAge())
                print("+-------------------+---------- ")
                print("|  Department       | ", i.get_empDepartment())
                print("|  Position         | ", i.get_empPosition())
                print("|  Salary           | ", i.get_empSalary())
                print("+-------------------+-----------------------=")
                print("\n")
        elif viewData == 'T' or viewData == 't':
            print("\n")
            # REVIEW TABLE VIEW IS UNSTABLE
            print("+========+===============================+========+========================================+==============+")
            print ("{:<23} {:<20} {:<15} {:<8} {:<1}".
            format('|   ID   |  ', 'NAME             |', 'AGE  | ', 'DEPARTMENT & POSITION          | ', '  SALARY   |'))
            print("+========+===============================+========+========================================+==============+")

            for employee in employee_list:
                print ("   {:<2}         {:<1}, {:<1} {:14} {:<11} {:<1}, {:<15} {:<1}"
                            .format( employee.get_empID(), employee.get_empLN(), 
                            employee.get_empFN(), employee.get_empMN(), 
                            employee.get_empAge(), employee.get_empDepartment(), 
                            employee.get_empPosition(), employee.get_empSalary()))
            print("\n")
        else:
            print("\n")
            print(">> INVALID INPUT!")
            print("\n")





# FUNCTION TO DELETE AN EMPLOYEE DATA BY empID
def delete_data(employee_list):
    print("\n")


    # Check if there is atleast 1 data in the list
    if len(employee_list) == 0:
        print(">> No data found!\n\n")
    else:
        emplyeeCount = len(employee_list)                               # Total employee data in the list 
        count = -1                                                      # Looping whole numbers for display

        print("There are ", emplyeeCount, "employee data stored.")       
        for i in employee_list:       
            count = count + 1
            print("\t", count, "== Employee ID", i.get_empID())
        deleteData = int(input("Which data do you want to delete?   "))
    
        del employee_list[deleteData]                                    # Delete data by index in the list
    

        print()
        print(">> Data successfully deleted")
        print()
    
    
    return employee_list





# FUNCTION TO EXIT THE PROGRAM
def exit_program():
    print("THANK YOU VERY MUCH!")
    exit()










# # #
#                  
#   MAIN CODE   
# 
# # #             
if __name__ == "__main__":
    main()