# Creates the Employee superclass and initializes attributes
class Employee:
    # init method initializes the name and id attributes
    def __init__(self, empID, empLast, empFirst, empMiddle, empAge):
        self.__empID = empID
        self.__empLast = empLast
        self.__empFirst = empFirst
        self.__empMiddle = empMiddle
        self.__empAge = empAge


    #
    # SETTERS
    #

    # The set method sets the ID attribute
    def set_empID(self, empID):
        self.__empID = empID

    # The set method sets the last name attribute
    def set_empLast(self, empLast):
        self.__empLast = empLast

    # The set method sets the first name attribute
    def set_empFirst(self, empFirst):
        self.__empFirst = empFirst

    # The set method sets the middle name attribute    
    def set_empMiddle(self, empMiddle):
        self.__empMiddle = empMiddle 

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
    def get_empLast(self):
        return self.__empLast

    # The get method returns the first name attribute
    def get_empFirst(self):
        return self.__empFirst

    # The get method returns the middle name attribute
    def get_empMiddle(self):
        return self.__empMiddle    
       
    # The get method sets the age attribute 
    def get_empAge(self):
        return self.__empAge





# Subclass of the Employee class
class Wrok(Employee):
    # init method initializes all the attributes and inherits the super class' attributes
    def __init__(self, empDepartment, empPosition, empSalary):
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
        self.__empempPosition = empPosition
    
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