# Project 1: Employee Management System #
employees = []
def add_employee():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    role = input("Enter role: ")
    salary = float(input("Enter salary: ")) 
    emp = {"name": name, "age": age, "role": role, "salary": salary}
    employees.append(emp)

def display():
    for emp in employees:
        print(emp)

def update_employee():
    name = input("Enter name to update: ")
    for emp in employees:
        if emp["name"] == name:
            emp["salary"] = float(input("New salary: "))

def delete_employee():
    name = input("Enter name to delete: ")
    for emp in employees:
        if emp["name"] == name:
            employees.remove(emp)
# menu
while True:
    print("\n1.Add 2.Display 3.Update 4.Delete 5.Exit")
    choice = input("select one number: ")
    if choice == "1": add_employee()
    elif choice == "2": display()
    elif choice == "3": update_employee()
    elif choice == "4": delete_employee()
    else: break


# Project 2: Student Report Card #
def report():
    name = input("Enter name: ")
    m1 = int(input("Marks1: "))
    m2 = int(input("Marks2: "))
    m3 = int(input("Marks3: "))
    m4 = int(input("Marks4: "))
    total = m1 + m2 + m3 + m4
    avg = total / 4

    if avg >= 75:
        grade = "A"
    elif avg >= 60:
        grade = "B"
    elif avg >= 40:
        grade = "c"
    else:
        grade = "D"
        
    print(f"\nReport Card\nName: {name}\nTotal: {total}\nAverage: {avg:.2f}\nGrade: {grade}")
report() 


# Project 3: Shopping Cart System #
cart = []

def add_item():
    name = input("Product: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))
    cart.append({"name": name, "price": price, "qty": qty})

def total_bill():
    total = 0
    for item in cart:
        total += item["price"] * item["qty"]
    print("Total Bill:", total)

def remove_item():
    name = input("Enter product to remove: ")
    for item in cart:
        if item["name"] == name:
            cart.remove(item)

def display():
    for item in cart:
        print(item)

while True:
    print("\n1.Add 2.Remove 3.Display 4.Total 5.Exit")
    option = input("Select any one option: ")
    if option == "1": add_item()
    elif option == "2": remove_item()
    elif option == "3": display()
    elif option == "4": total_bill()
    else: break


# Project 4: Login & User Validation #
users = {
    'chinguu': 'changuuuu',
    'arav': 'famous',
    'harshini': 'carrot',
    'sakhi': 'sakhti000'
}
username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("Login Successful")
else:
    print("Invalid Credentials")


# Project 5: Unique Visitor Counter #
visitors = set()

def add_visitor(name):
    visitors.add(name)
    print(f"Added: {name}")

def print_unique_count():
    print(f"Total unique visitors: {len(visitors)}")
    print(f"All visitors: {sorted(visitors)}")

add_visitor("ranjith")
add_visitor("mounika")
add_visitor("radha")
add_visitor("radha")
add_visitor("krishna")
add_visitor("kranthi")
add_visitor("kranthi")
print_unique_count()


# Project 6: String Formatter Tool #
name = input("Enter your name: ")
product = input("Enter product name: ")
print("\n--- Formatted Output ---")
print("Customer Name : {}".format(name))
print("Product       : {}".format(product))
print("Sentence      : {} purchased a {}".format(name, product))
print("\n--- Padding Output ---")

# Left aligned
print("Left Align    : {:<40}".format(name))

# Right aligned
print("Right Align   : {:>30}".format(name))

# Center aligned
print("Center Align  : {:^25}".format(name))


# Project 7: Bank Account System #
account = {"name": "", "balance": 0}
def create():
    account["name"] = input("Enter name: ")
    account["balance"] = float(input("Enter balance: "))

def deposit():
    amt = float(input("Amount: "))
    account["balance"] += amt

def withdraw():
    amt = float(input("Amount: "))
    if amt <= account["balance"]:
        account["balance"] -= amt
    else:
        print("Insufficient balance")

def check():
    print("Balance:", account["balance"])

while True:
    print("\n1.Create 2.Deposit 3.Withdraw 4.Check 5.Exit")
    option = input("select any one input: ")
    if option == "1": create()
    elif option == "2": deposit()
    elif option == "3": withdraw()
    elif option == "4": check()
    else: break


# Project 8: Voting System #
votes = {"Grace": 0, "crate": 0, "Prince": 0, "bunny": 0, " rinku": 0}
while True:
    vote = input("Vote (Grace/crate/Prince/bunny/rinku or stop): ")
    if vote == "stop":
        break
    if vote in votes:
        votes[vote] += 1

winner = max(votes, key=votes.get)
print("Winner:", winner)


# Project 9: Course Enrollment #
students = {}

def add_student():
    name = input("Name: ")
    courses = input("Courses (comma separated): ").split(",")
    students[name] = courses

def update():
    name = input("Name: ")
    if name in students:
        students[name] = input("New courses: ").split(",")

def display():
    print(students)

while True:
    print("\n1.Add 2.Update 3.Display 4.Exit")
    type = input("Opinion: ")
    if type == "1": add_student()
    elif type == "2": update()
    elif type == "3": display()
    else: break


# Project 10 : Number Utility Tool #
def number_utils(num):
    print(f"\n{'='*40}")
    print(f"Input Number: {num}")
    print(f"Binary:   {bin(num)[2:].upper():>15}")
    print(f"Octal:    {oct(num)[2:].upper():>15}")
    print(f"Hex:      {hex(num)[2:].upper():>15}")
    print(f"Commas:   {num:,}")
    print(f"{'='*40}")

while True:
    try:
        n = int(input("Enter number (0 to quit): "))
        if n == 0:
            break
        number_utils(n)
    except ValueError:
        print("Enter valid integer!")




