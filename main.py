class Employee:
    empLast = ""
    empFirst = ""
    empMiddle = ""
    empAge = 0
    empAddress = ""
    empBirth = ""


    def autoData(self, empLast, empFirst, empMiddle, empAge, empAddress, empBirth):
        self.empLast = empLast
        self.empFirst = empFirst
        self.empMiddle = empMiddle
        self.empAge = empAge
        self.empAddress = empAddress
        self.empBirth = empBirth

    def setData(self):
        self.empLast = input("Last name:   ")
        self.empFirst = input("First name:   ")
        self.empMiddle = input("Last name:   ")
        self.empAge = int(input("Age:   "))
        self.empAddress = input("Address:   ")
        self.empBirth = input("Date of Birth:   ")


    def displayData(self):
        print("Name:           ", self.empLast, ",",self.empFirst, self.empMiddle)
        print("Age:            ", self.empAge)
        print("Address:        ", self.empAddress) 
        print("Date of Birth:  ", self.empBirth)


        

class Work(Employee):
    def __init__(self, empPosition, empDepartment, empSalary):
        self.empPosition = empPosition
        self.empDepartment = empDepartment
        self.empSalary = empSalary




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
                read_data()
            elif menuChoice == 'u':
                update_data()
            elif menuChoice == 'd':
                delete_data()
            elif menuChoice == 'e':
                exit_program()
            else:
                print("\n")
                print("m>> INVALID INPUT!")
                print("\n")
        except ValueError:
            print("\n")
            print(">> INVALID INPUT!")
            print("\n")





# FUNCTION: CREATE EMPLOYEE DATA
def create_data():
    print("")


    emp = Employee()

    generateChoice = input("Do you want to auto-generate data?   ")

    if generateChoice == 'y':
        emp.setData()
    elif generateChoice == 'n':
        emp.autoData("Doe", "John", "Smith", 20, "Recodo", "September")

    emp.displayData()


    


# FUNCTION: READ EMPLOYEE DATA
def read_data():
    print("")

    emp = Employee()
    emp.displayData()


# FUNCTION: UPDATE EMPLOYEE DATA
def update_data():
    print("")





# FUNCTION: DELETE EMPLOYEE DATA
def delete_data():
    print("")




# FUNCTION: EXIT
def exit_program():
    print("THANK YOU FOR USING THE SYSTEM!")
    exit()








""""" 
    MAIN CODE 
"""""
# Start program
main_menu()
