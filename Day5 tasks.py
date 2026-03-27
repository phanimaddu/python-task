# Task 1: 
# User Info Manager (Functions + Dictionary) # 

# Create a function:
def create_user(name, age, role):
    user = {
        "name": name.title(),
        "age": age,
        "role": role
    }
    return user; 
users = []

# Store multiple users in a list #
users.append(create_user("chinguuuu", 22, "Administrator"))
users.append(create_user("mojo", 18, "dermatologist"))
users.append(create_user("ranger", 36, "interior designer"))
users.append(create_user("jerry", 21, "app engineer"))
users.append(create_user("crate", 32, "mearn stack developer"))
users.append(create_user("harshuuu", 40, "jira "))

# Printing all users #
for user in users:
    print(user) 

# Task 2: Dynamic Calculator (*args)

def calculate_total():
    numbers = []
    print("Enter numbers (type 'done' to finish):")

    while True:
        data = input("> ")
        if data.lower() == 'done':
            break
        try:
            numbers.append(float(data))
        except ValueError:
            print("That's not a number! Try again.")

    if numbers:
        total = sum(numbers)
        print(f"Sum: {total}")
        print(f"Average: {total / len(numbers):.2f}")
    else:
        print("No numbers entered.")

calculate_total() 

# Task 3: Dynamic Configurations (**kwargs) 

def show_config(**settings):
    print("\n latest Configuration")
    for x, y in settings.items(): # x is key, y is value
        print(f"{x}: {y}")

configs = {}
print("Enter settings (type 'done' to stop):")

while True:
    key = input("Key: ")
    if key.lower() == "done":
        break
    
    value = input("Value: ")
    configs[key] = value

show_config(**configs) 

# Task 4: Factorial Service (Recursion) 

def factorial(n):
    if n < 0:
        return "Error : Because of negative value"
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
num = int(input("Enter a number: "))
print(f"Result: {factorial(num)}") 

# Task 5: Memory Optimization (Generator)

def square_generator(n):
    for i in range(1, n + 1):
        yield i * i

print("Memory Optimization & Generator")
n = 27
normal_list = [i * i for i in range(1, n + 1)]
gen = square_generator(n)

print("Normal list:", normal_list)
print("Generator:", gen)
print("Type of list:", type(normal_list))
print("Type of generator:", type(gen))

print("Yielded values from generator:")
for value in gen:
    print(value) 

# Task 6: Exception Handling Module 

def divide():
    try:
        num = float(input("Enter numerator: "))
        den = float(input("Enter denominator: "))
        result = num / den
        print(f"Result: {result:.2f}")

    except ZeroDivisionError:
        print("Error: You cannot division by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")
    finally:
        print("Program Completed")
divide() 

# Task 7: File Handling (Read/Write)

users_list = [
    {"name": "chinguuuu", "age": 25, "role": "Administrator"},
    {"name": "mojo", "age": 20, "role": "jira specialist"},
    {"name": "ranger", "age": 29, "role": "interior designer"},
]

print("File Handling")
filename = "team_data.txt"

# Write user details to file
with open(filename, "w") as file:
    for user in users_list:
        line = f"Name: {user['name']}, Age: {user['age']}, Role: {user['role']}\n"
        file.write(line)

# Read and display content
with open(filename, "r") as file:
    content = file.read()
    print("Content of team_data.txt:")
    print(content)

# Checking the file is closed or not
print("Is file closed after with-block?", file.closed)
print("Program Completed")
