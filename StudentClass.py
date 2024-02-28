import datetime

class Student:
    def __init__(self,StudentID, Name, DOB, classification):
        self.StudentID = StudentID
        self.Name = Name
        self.DOB = datetime.datetime.strptime(DOB, '%Y-%m-%d')
        self.classification = classification

    def calculate_age(self):
        today = datetime.datetime.today()
        return today.year - self.DOB.year - ((today.month, today.day) < (self.DOB.month, self.DOB.day))
    
    def registration_dates(self):
        if self.classification == 'Sr':
            return '4/1 thru 4/3'
        elif self.classification == 'Jr':
            return '4/4 thru 4/6'
        elif self.classification == 'S':
            return '4/7 thru 4/9'
        elif self.classification == 'F':
            return '4/10 thru 4/12'
        
    def get_age(self):
        return self.calculate_age()
    
    def get_registration_dates(self):
        return self.registration_dates()