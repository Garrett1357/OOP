import StudentClass as S
import datetime

student_instance = S.Student("StudentID", "Name", "1990-01-01", "classification")


print(f"Student's Age: {S.get_age()} years")

print(f"Registration Dates: {S.get_registration_dates()}")