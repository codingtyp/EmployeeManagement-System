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
                print("m>> INVALID INPUT! Choose between 1 - 3 only!")
                print("\n")
        except ValueError:
            print("\n")
            print(">> INVALID INPUT! Characters and symbols are not accepted")
            print("\n")






# FUNCTION: EXIT
def exit_program():
    print("THANK YOU!")
    exit()








""""" 
    MAIN CODE 
"""""
# Start program
main_menu()
