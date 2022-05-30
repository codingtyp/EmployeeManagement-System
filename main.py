def main_menu():
    print("*********************************************************")
    print("*             EMPLOYEE MANAGEMENT SYSTEM                  *")
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


            if menuChoice.lower == 'c':
                ()
            elif menuChoice.lower == 'r':
                ()
            elif menuChoice.lower == 'u':
                ()
            elif menuChoice.lower == 'd':
                ()
            elif menuChoice.lower == 'e':
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





# FUNCTION: READ EMPLOYEE DATA
def read_data():
    print("")





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
