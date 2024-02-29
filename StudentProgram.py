from StudentClass import Student as S
import datetime

student = S("892588999", "Garrett Austin", "03-02-2001", "Sr")

print(f"Student's Name: {student.Name}")

print(f"Student's Age: {student.get_age()} years")

print(f"Registration Dates: {student.get_registration_dates()}")