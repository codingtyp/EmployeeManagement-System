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
        self.empMiddle = input("Midddle name:   ")
        self.empAge = int(input("Age:   "))
        self.empAddress = input("Address:   ")
        self.empBirth = input("Date of Birth:   ")


    def displayData(self):
        print("Name:           ", self.empLast, ",",self.empFirst, self.empMiddle)
        print("Age:            ", self.empAge)
        print("Address:        ", self.empAddress) 
        print("Date of Birth:  ", self.empBirth)





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
                print("\n")


                # Objects
                emp = Employee()

    
                totalData = int(input("How many data do you want to enter? "))
                i = 0
                for i in range (totalData):
                    print("--------------------")
                    emp.setData()
                    print("--------------------\n")



            elif menuChoice == 'r':
                i = 0
                for i in range (totalData):
                    emp.displayData()
            elif menuChoice == 'u':
                () 
            elif menuChoice == 'd':
                ()
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





# FUNCTION: EXIT
def exit_program():
    print("THANK YOU FOR USING THE SYSTEM!")
    exit()










""""" 
    MAIN CODE 
"""""
# Start program
main_menu()
