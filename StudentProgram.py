from StudentClass import Student as S
import datetime

student = S("892588999", "Garrett Austin", "03-02-2001", "Sr") #sets student instance

print(f"Student's Name: {student.Name}") #grabs name
 
print(f"Student's Age: {student.get_age()} years") #grabs age

print(f"Registration Dates: {student.get_registration_dates()}") #grabs reg date