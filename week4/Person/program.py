from datetime import datetime

f_name = input("Enter first name: ")
s_name = input("Enter second name: ")
t_name = input("Enter third name: ")
b_year = input("Enter birth year: ")
b_year = int(b_year)
now = datetime.now()
c_year = now.year

person = {
    "first_name": f_name,
    "second_name" : s_name,
    "third_name": t_name,
    "birth_year": b_year,
    "current_age": c_year - b_year
    
    }
print(person)

