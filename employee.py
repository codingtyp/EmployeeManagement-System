# Creates the Employee superclass and initializes attributes
class Employee:
    # init method initializes the name and id attributes
    def __init__(self, empID, empLast, empFirst, empMiddle):
        self.__empID = empID
        self.__empLast = empLast
        self.__empFirst = empFirst
        self.__empMiddle = empMiddle

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