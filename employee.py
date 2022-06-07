# Creates the Employee superclass and initializes attributes
class Employee:
    # init method initializes the name and id attributes
    def __init__(self, empID, empLN, empFN, empMN, empAge):
        self.__empID = empID
        self.__empLN = empLN
        self.__empFN = empFN
        self.__empMN = empMN
        self.__empAge = empAge


    #
    # SETTERS
    #

    # The set method sets the ID attribute
    def set_empID(self, empID):
        self.__empID = empID

    # The set method sets the last name attribute
    def set_empLN(self, empLN):
        self.__empLN = empLN

    # The set method sets the first name attribute
    def set_empFN(self, empFN):
        self.__empFN = empFN

    # The set method sets the middle name attribute    
    def set_empMN(self, empMN):
        self.__empMN = empMN 

    # The set method sets the age attribute 
    def set_empAge(self, empAge):
        self.__empAge = empAge


    #
    # GETTERS
    #

    # The get method returns the ID attribute
    def get_empID(self):
        return self.__empID

    # The get method returns the last name attribute
    def get_empLN(self):
        return self.__empLN

    # The get method returns the first name attribute
    def get_empFN(self):
        return self.__empFN

    # The get method returns the middle name attribute
    def get_empMN(self):
        return self.__empMN    
       
    # The get method sets the age attribute 
    def get_empAge(self):
        return self.__empAge





# Subclass of the Employee class
class Worker(Employee):
    # Initializes all the attributes and inherits the super class' attributes
    def __init__(self, empID, empLN, empFN, empMN, empAge, empDepartment, empPosition, empSalary):
        Employee.__init__(self, empID, empLN, empFN, empMN, empAge)
        self.__empDepartment = empDepartment
        self.__empPosition = empPosition
        self.__empSalary = empSalary


    #
    # SETTERS
    #

    # The set method sets the department attribute
    def set_empDepartment(self, empDepartment):
        self.__empDepartment = empDepartment

    # The set method sets the position attribute
    def set_empempPosition(self, empPosition):
        self.__empPosition = empPosition
    
    # The set method sets the salary attribute
    def set_empempSalary(self, empSalary):
        self.__empSalary = empSalary


    #
    # GETTERS
    #

    # The get method returns the department attribute
    def get_empDepartment(self):
        return self.__empDepartment

    # The get method returns the position attribute
    def get_empPosition(self):
        return self.__empPosition

    # The get method returns the salary attribute
    def get_empSalary(self):
        return self.__empSalary