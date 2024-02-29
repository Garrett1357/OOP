import datetime

class Student:
    def __init__(self,StudentID, Name, DOB, classification):
        self.StudentID = StudentID
        self.Name = Name
        self.DOB = datetime.datetime.strptime(DOB, '%m-%d-%Y') #Formats DOB into M Y D
        self.classification = classification

    def calculate_age(self):
        today = datetime.datetime.today()
        return today.year - self.DOB.year #Calculates age, currently doesnt take days into account
    
    def registration_dates(self):
        if self.classification == 'Sr':
            return ('4/1 through 4/3')
        elif self.classification == 'Jr':
            return ('4/4 through 4/6')
        elif self.classification == 'S':
            return ('4/7 through 4/9')
        elif self.classification == 'F':
            return ('4/10 through 4/12')
        
    def get_age(self):
        return self.calculate_age() #returns calculated age to program
    
    def get_registration_dates(self):
        return self.registration_dates() #returns registration date to program