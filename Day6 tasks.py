# Task 1 : Encapsulation (User Class)
class User:
    def __init__(self):
        self.__user_name = None
        self.__pwd = None

    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    def get_user(self):
        return self.__user_name

    def register(self):
        print(f"Registering user: {self.__user_name}")

    def login(self):
        print(f"Logging in: {self.__user_name}")

user_name = input("Enter username: ")
pwd = input("Enter password: ")

user = User()

user.set_user(user_name, pwd)

user.register()
user.login()

# Task 2 : Inheritance

class User:
    def register(self):
        print("Registering user...")

    def login(self):
        print("Logging in...")

class Student(User):
    def student_greet(self):
        print("Hello Student")

class Faculty(User):
    def faculty_greet(self):
        print("Hello Faculty")

class TempFaculty(Faculty):
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")

s1 = Student()
s1.register()        
s1.login()           
s1.student_greet()   

f1 = Faculty()
f1.register()        
f1.login()          
f1.faculty_greet()   

tf1 = TempFaculty()
tf1.register()            
tf1.login()               
tf1.faculty_greet()      
tf1.tempFaculty_greet()   

u1 = User()
u1.register()
u1.login()

u1.student_greet() 
u1.faculty_greet()  

# Task 3: Method Overriding 

class User: 
    def greet(self):
        print("Welcome User")

class Student(User):
    def greet(self):
        print("Welcome Student")    

class Faculty(User):
    def greet(self):
        print("Welcome Faculty")

student = Student()             
faculty = Faculty()
student.greet()
faculty.greet()

# Task 4: Method Chaining 

class User:
    def register(self):
        print("registered")
        return self

    def login(self):
        print("logined")
        return self

    def greet(self):
        print("enjoy everyone")
        return self
    
user = User()   
user.login().greet().register() 

# Task 5: Mini User System 

class User:
    users_count = 0

    def __init__(self):
        self.__user_name = None
        self.__pwd = None
        User.users_count += 1

    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    def get_user(self):
        return self.__user_name

    def register(self):
        print(f"Registering user: {self.__user_name}")
        return self

    def login(self):
        print(f"Logging in: {self.__user_name}")
        return self

    def greet(self):
        print("Welcome User")
        return self
    
class Student(User):
    def greet(self):
        print("Welcome Student")
        return self
    
class Faculty(User):
    def greet(self):
        print("Welcome Faculty")
        return self
    
student = Student()
student.set_user("harshuu", "000000")
student.login().greet().register()

faculty1 = Faculty()
faculty1.set_user("tom", "213213")
faculty1.login().greet().register()

faculty2 = Faculty()
faculty2.set_user("king", "143341")
faculty2.login().greet().register()

faculty3 = Faculty()
faculty3.set_user("jullet", "789456")
faculty3.login().greet().register()

faculty4 = Faculty()
faculty4.set_user("phani", "252525")
faculty4.login().greet().register()

print(f"Total users created: {User.users_count}")












