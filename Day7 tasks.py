# Task 1 : Constructors super()

class User:
    def __init__(self, user_name, user_id):
        self.name = user_name
        self.id = user_id

    def display_user(self):
        print(f"Name: {self.name}, ID: {self.id}")

class Student(User):
    def __init__(self, student_name, user_id, department, fees):
        super().__init__(student_name, user_id)
        self.dept = department
        self.fees = fees

    def display_student(self):
        self.display_user()
        print(f"Department: {self.dept}, Fees: {self.fees}")
 
class Faculty(User):
    def __init__(self, faculty_name, user_id, salary):
        super().__init__(faculty_name, user_id)
        self.salary = salary

    def display_faculty(self):
        self.display_user()
        print(f"Salary: {self.salary}")

class TempFaculty(Faculty):
    def __init__(self, temp_faculty_name, user_id, salary, duration):
        super().__init__(temp_faculty_name, user_id, salary)
        self.duration = duration

    def display_temp_faculty(self):
        self.display_faculty()
        print(f"Duration: {self.duration}")

print("---- Student ----")
s = Student("Ranjith", 1011, "Oncology", 40000)
s.display_student()

print("\n---- Faculty ----")
f = Faculty("Sadana", 1144, 110000)
f.display_faculty()

print("\n---- Temp Faculty ----")
t = TempFaculty("Vennela", 422, 55000, "1 Year")
t.display_temp_faculty()


# Task 2 : Applying Abstraction 
from abc import ABC, abstractmethod

class AbstractUser(ABC):
    def __init__(self, user_name, user_id):
        self.name = user_name
        self.id = user_id

class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass

class Student(AbstractUser):
    def __init__(self, user_name, user_id, department, fees):
        super().__init__(user_name, user_id)
        self.department = department
        self.fees = fees

    def get_details(self):
        return f"Student -> Name: {self.name}, ID: {self.id}, Dept: {self.department}, Fees: {self.fees}"

class Faculty(AbstractUser):
    def __init__(self, user_name, user_id, salary):
        super().__init__(user_name, user_id)
        self.salary = salary

    def get_details(self):
        return f"Faculty -> Name: {self.name}, ID: {self.id}, Salary: {self.salary}"

class TempFaculty(Faculty):
    def __init__(self, user_name, user_id, salary, duration):
        super().__init__(user_name, user_id, salary)
        self.duration = duration

    def get_details(self):
        return f"TempFaculty -> Name: {self.name}, ID: {self.id}, Salary: {self.salary}, Duration: {self.duration}"

s = Student("raghu", 121, "Architecture", 90000)
f = Faculty("mounish", 122, 80000)
t = TempFaculty("hrudai", 123, 40000, "6 Months")

print(s.get_details())
print(f.get_details())
print(t.get_details())


#Task 3 : Sorting using key
from abc import ABC, abstractmethod

class AbstractUser(ABC):
    def __init__(self, user_name, user_id):
        self.name = user_name
        self.id = user_id

    @abstractmethod
    def get_details(self):
        pass

class Student(AbstractUser):
    def __init__(self, user_name, user_id, department, fees):
        super().__init__(user_name, user_id)
        self.dept = department
        self.fees = fees

    def get_details(self):
        return f"Student | {self.name} | ID: {self.id} | Dept: {self.dept} | Fees: {self.fees}"

class Faculty(AbstractUser):
    def __init__(self, user_name, user_id, salary):
        super().__init__(user_name, user_id)
        self.salary = salary

    def get_details(self):
        return f"Faculty | {self.name} | ID: {self.id} | Salary: {self.salary}"

class TempFaculty(Faculty):
    def __init__(self, user_name, user_id, salary, duration):
        super().__init__(user_name, user_id, salary)
        self.duration = duration

    def get_details(self):
        return f"TempFaculty | {self.name} | ID: {self.id} | Salary: {self.salary} | Duration: {self.duration}"

students = [
    Student("ranjith",   1001, "Dermitology", 55000),
    Student("krishna",   1002, "oncology", 45000),
    Student("raju",      1003, "Dentistry",  62000),
]

faculty = [
    Faculty("vennelaa",   143, 60000),
    Faculty("seshu",      420, 75000),
    Faculty("mounika",    121, 90000),
    TempFaculty("radha",  2001, 47000, "2 Year"),
]

students.sort(key=lambda x: x.fees)
print("Students sorted by fees :")
for s in students:
    print(" ", s.get_details())
print()

faculty.sort(key=lambda x: x.salary)
print("Faculty sorted by salary :")
for f in faculty:
    print(" ", f.get_details())
print()


#Task 4 : Using Map ()
class Student:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees

students = [
    Student("Ranjith", 70000),
    Student("Raghu", 45000),
    Student("Sagar", 40000),
    Student("Jerry", 35000)
]
names = list(map(lambda s: s.name, students))
print("Student Names:", names)


# Task 5 : Using Filter ()
class Student:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees

    def __repr__(self):
        return f"{self.name} - Fees: {self.fees}"

class Faculty:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f"{self.name} - Salary: {self.salary}"

students = [
    Student("Ranjith", 80000),
    Student("Rahul", 70000),
    Student("Sageetha", 30000),
    Student("Priya", 45000),
]

faculty = [
    Faculty("Harsha", 50000),
    Faculty("Adhitya", 20000),
    Faculty("Meenakshi", 80000)
]

high_fee_students = list(filter(lambda s: s.fees > 50000, students))
print("Students with fees > 50000:")
for s in high_fee_students:
    print(s)
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))
print("\nFaculty with salary > 30000:")
for f in high_salary_faculty:
    print(f) 


# Task 6 : Use reduce() 
from functools import reduce

class Student:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees

class Faculty:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

students = [
    Student("Ranjith", 75000),
    Student("Raghu", 45000),
    Student("Sailesh", 30000)
]

faculty = [
    Faculty("Anikesh", 80000),
    Faculty("Anusha", 60000),
    Faculty("Meenakshi", 95000),
    Faculty("Harsha", 50000)
]

total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
print("Total Fees Collected:", total_fees)

total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)
print("Total Salary of Faculty:", total_salary) 


# Task 7 : Higher Order Function
class Student:
    def __init__(self, user_name, student_fees):
        self.name = user_name
        self.fees = student_fees

    def __repr__(self):
        return f"{self.name} - Fees: {self.fees}"

def process_users(users, func):
    return list(map(func, users))

students = [
    Student("Ranjith", 90000),
    Student("Raghu", 40000),
    Student("Jerry", 70000)
]

names = process_users(students, lambda s: s.name)
print("Student Names:", names)

def filter_high_fees(s):
    return s.fees > 50000

high_fee_students = list(filter(filter_high_fees, students))

print("\nStudents with fees > 50000:")
for s in high_fee_students:
    print(s)


# Final Challenge : mini system

from abc import ABC, abstractmethod
from functools import reduce

# -------- ABSTRACT CLASS ---------------
class AbstractUser(ABC):
    def __init__(self, user_name, user_id):
        self.name = user_name
        self.id = user_id

    @abstractmethod
    def get_details(self):
        pass

# -------- STUDENT ---------------------
class Student(AbstractUser):
    def __init__(self, user_name, user_id, department, fees):
        super().__init__(user_name, user_id)
        self.dept = department
        self.fees = fees

    def get_details(self):
        return f"Student | {self.name} | ID: {self.id} | Dept: {self.dept} | Fees: {self.fees}"

# -------- FACULTY ---------------------
class Faculty(AbstractUser):
    def __init__(self, user_name, user_id, salary):
        super().__init__(user_name, user_id)
        self.salary = salary

    def get_details(self):
        return f"Faculty | {self.name} | ID: {self.id} | Salary: {self.salary}"


# -------- Information of Students and Faculty --------
students = [
    Student("Ranjith", 1001, "CSE", 60000),
    Student("Raghu", 1002, "ECE", 30000),
    Student("Sagar", 1003, "EEE", 70000)
]

faculty = [
    Faculty("Meenakshi", 201, 40000),
    Faculty("Anikesh", 202, 45000),
    Faculty("Anusha", 203, 60000)
]

#-------- 1. Printing All Details -------------
print(" All Student Details:")
student_details = list(map(lambda s: s.get_details(), students))
for s in student_details:
    print(s)

print("\n All Faculty Details:")
faculty_details = list(map(lambda f: f.get_details(), faculty))
for f in faculty_details:
    print(f)

# -------- 2. SORTING DATA -------------
students_sorted = sorted(students, key=lambda s: s.fees)
faculty_sorted = sorted(faculty, key=lambda f: f.salary)

print("\n Students Sorted by Fees:")
for s in students_sorted:
    print(s.get_details())

print("\n Faculty Sorted by Salary:")
for f in faculty_sorted:
    print(f.get_details())

# -------- 3. FILTERING DATA --------
high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))

print("\n Students with Fees > 50000:")
for s in high_fee_students:
    print(s.get_details())

print("\n Faculty with Salary > 30000:")
for f in high_salary_faculty:
    print(f.get_details())

# -------- 4. REDUCING -------------------
total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)

print("\n Total Fees Collected:", total_fees)
print(" Total Salary Paid:", total_salary)