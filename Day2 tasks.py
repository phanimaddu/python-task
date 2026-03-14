# Bitwise Operator Tasks (1–8)
# Task 1 - AND
a = 10
b = 6
print(a & b)

# Task 2 - OR
x = 12
y = 5
print(x | y)

# Task 3 - NOT
num = 8
print(~num)

# Task 4 - XOR
a = 15
b = 9
print(a ^ b)

# Task 5 - left shift by 2
num = 7
print(num << 2)

# Task 6 - right shift by 1
num = 20
print(num >> 1)

# Task 7 - Get two values from user input and print AND result
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("AND result:", a & b)

# Task 8 - Get two values from user input and print XOR result
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("XOR result:", a ^ b)

# String Tasks (9–14)
# Task 9 - replication 4 times
word = "hi"
print(word*4)

#Task 10 - replication 3 times
word2 = "python"
print(word2*3)

# Task 11 - combine 2 strings using + operator
text1 = "super"
text2 = "man"
print(text1+text2)

# Task 12  - combine 3 strings
a = "hello"
b = " "
c = "world"
print(a + b + c)

# Task 13 - get value from user and print 5 times
a = input("Enter the text to repeat 5 times : ")
print((a + " ")*5)

# Task 14 -  get two strings from user input and concatenate
str1 = input("Enter first text: ")
str2 = input("Enter second text: ")
answer = str1 + str2
print(answer)

# Input & Type Casting Tasks (15–20)
# Task 15 - get name from user and print data type
name = input("Enter your name: ")
print(type(name))

# Task 16 - get age from user and convert to integer
age = int(input("Enter your age: "))
print(age)
# int() is used to convert the user input (string) into an integer.

# Task 17 - get 2 numbers from user and print their sum
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)

# Task 18 - get 2 marks from user and print its average
mark1 = float(input("Enter first mark: "))
mark2 = float(input("Enter second mark: "))
average = (mark1 + mark2) / 2
print("Average:", average)

# Task 19 - get two numbers from user and print 3*a*2 + b - 2
a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))
print(3*a*2 + b - 2)

# Task 20 - get number from user and print before and after typecaste
num = input("Enter the Number: ")
print("Before type casting : ",type(num))
num = int(num)
print("After type casting : ", type(num))

# Unit Digit Tasks (21–25)
# Task 21 - get number as str input and print last digit
num = input("Enter a number: ")
print("Last digit:", num[-1])

# Task 22 - get number and print unit digit using % operator
num = int(input("Enter a number: "))
print("Unit digit:", num % 10)

# Task 23 - get number and remove last digit using // operator
num = int(input("Enter a number: "))
print("Number after removing last digit:", num // 10)

# Task 24 - Take a number and print the second last digit
num = int(input("Enter a number: "))
print("Second last digit:", (num // 10) % 10)

# Task 25 - Take 5 digit number and print last digit
num = int(input("Enter a 5 digit number: "))
print("Last digit:", num % 10)

# If Statement Tasks (26–30)
# Task 26 - if check 10>=5
if 10 >= 5:
    print("10 is greater than or equal to 5")

# Tast 27 - get number from user ad check greater than 50
a = int(input("Enter the number : "))
if a > 50:
    print(a, "is greater than 50")

# Task 28 - get age and check age ≥ 18
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible")

# Task 29 - check number greater than 100
num = int(input("Enter a number: "))
if num > 100:
    print("The number is greater than 100")

# Task 30 - check number ≥ 0
num = int(input("Enter a number: "))
if num >= 0:
    print("The number is greater than or equal to 0")

# If-Else Tasks (31–34)
# Task 31 - Check odd or even 
a = int(input("enter the Number : "))
if a%2==0:
    print("Its an Even number")
else:
    print("Its an Odd number")

# Task 32 - check if pass or fail (pass ≥ 35)
marks = int(input("Enter your marks: "))
if marks >= 35:
    print("Pass")
else:
    print("Fail")

# Task 33 - check if it is positive or negative
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
else:
    print("Negative number")

# Task 34 - check if it is greater than 10 or not
num = int(input("Enter a number: "))
if num > 10:
    print("Number is greater than 10")
else:
    print("Number is not greater than 10")

# Nested If Tasks (35–37)
# Task 35 - job eligibility program
age = int(input("Enter age: "))
height = int(input("Enter height (cm): "))
weight = int(input("Enter weight (kg): "))
if age >= 18:
    if height >= 160:
        if weight >= 60:
            print("Selected")
        else:
            print("Rejected")
    else:
        print("Rejected")
else:
    print("Rejected")

# Task 36 - college admission program
marks = int(input("Enter the marks : "))
age = int(input("Enter the age : "))
if marks >= 60:
    if age >= 17:
        print("Admission Granted")
    else:
        print("Admission Rejected")
else:
    print("Admission Rejected")

# Task 37 - sports selection program
age = int(input("Enter age: "))
height = int(input("Enter height (cm): "))
weight = int(input("Enter weight (kg): "))
if age >= 16:
    if height >= 150:
        if weight >= 50:
            print("Selected")
        else:
            print("Rejected")
    else:
        print("Rejected")
else:
    print("Rejected")

# Match Statement Tasks (38–40)
# Task 38 - day name using match
day = int(input("Enter a number (1-7): "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid number")

# Task 39 - match number with colors
num = int(input("Enter the Number (1-3) : "))
match num:
    case 1:
        print("Red")
    case 2:
        print("Blue")
    case 3:
        print("Green")
    case _:
        print("Invalid Number")

# Task 40 - match number with fruits
num = int(input("Enter a number (1-4): "))
match num:
    case 1:
        print("Apple")
    case 2:
        print("Mango")
    case 3:
        print("Orange")
    case 4:
        print("Banana")
    case _:
        print("Invalid number")


        