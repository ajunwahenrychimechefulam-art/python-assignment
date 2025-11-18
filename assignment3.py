salary = float(input("Enter basic salary: "))
bonus = float(input("Enter bonus: "))
tax = float(input("Enter tax rate (e.g., 0.1 for 10%): "))

gross = salary + bonus
tax_amount = tax * gross
net = gross - tax_amount

print("Gross Pay:", gross)
print("Tax Amount:", tax_amount)
print("Net Pay:", net)


#Login System (3 Attempts)
# Username = Promise
# Password = 12345
# User has only 3 tries.
# If wrong 3 times → print "Account locked".
# If correct → "Welcome back".

username = "Promise"
password = "12345"

for attempt in range(3):
    user = input("Enter username: ")
    pwd = input("Enter password: ")

    if user == username and pwd == password:
        print("Welcome back")
        break
    else:
        print("Incorrect credentials")

else:
    print("Account locked")



# Student Grade Analyzer
# Ask for 4 scores.
# Calculate average and assign grade:
# A = 70–100
# B = 60–69
# C = 50–59
# F = below 50
# Also print highest and lowest

scores = []
for i in range(1, 5):
    score = float(input(f"Enter score {i}: "))
    scores.append(score)

avg = sum(scores) / 4

if 70 <= avg <= 100:
    grade = "A"
elif 60 <= avg <= 69:
    grade = "B"
elif 50 <= avg <= 59:
    grade = "C"
else:
    grade = "F"

print("Average:", avg)
print("Grade:", grade)
print("Highest Score:", max(scores))
print("Lowest Score:", min(scores))


# ATM Withdrawal Simulation
# Start balance = 5000
# Ask for amount.
# If amount > balance → “Insufficient funds”
# If amount <= 0 → “Invalid amount”
# Else subtract and show new balance.

balance = 5000
amount = float(input("Enter withdrawal amount: "))

if amount > balance:
    print("Insufficient funds")
elif amount <= 0:
    print("Invalid amount")
else:
    balance -= amount
    print("Withdrawal successful. New balance:", balance)

#     Membership Login
# members = ("Favor", "Blessing", "Joy")
# password = abc123
# If name in members AND password correct → Access granted
# If name in members but password wrong → Password incorrect
# Else → Not registered

members = ("Favor", "Blessing", "Joy")
password = "abc123"

name = input("Enter your name: ")
pwd = input("Enter password: ")

if name in members and pwd == password:
    print("Access granted")
elif name in members and pwd != password:
    print("Password incorrect")
else:
    print("Not registered")


# Phone Network Checker
# Ask for number.
# If starts with 070/080 → MTN
# 081 → Airtel
# 090 → Glo
# Else → Unknown network

number = input("Enter phone number: ")

if number.startswith(("070", "080")):
    print("MTN")
elif number.startswith("081"):
    print("Airtel")
elif number.startswith("090"):
    print("Glo")
else:
    print("Unknown network")

# Two-Number Comparison
# Ask for two numbers.
# Print:
# – Which is larger
# – If they are equal
# – If their sum is even or odd

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Larger / equal
if a > b:
    print(a, "is larger")
elif b > a:
    print(b, "is larger")
else:
    print("Both numbers are equal")

# Even or odd sum
total = a + b
if total % 2 == 0:
    print("The sum is even")
else:
    print("The sum is odd")


#  Shopping Discount Program
# Ask for price + quantity.
# If total ≥ 20000 → 10% discount
# Else → no discount
# Print full breakdown.

price = float(input("Enter price: "))
qty = int(input("Enter quantity: "))

total = price * qty

if total >= 20000:
    discount = 0.10 * total
else:
    discount = 0

net = total - discount

print("Total:", total)
print("Discount:", discount)
print("Amount Payable:", net)


#  Bus Fare System
# Ask for age + student (yes/no).
# Age < 10 → Free
# 10–17 → Half price
# 18+ → Full price
# BUT if student → always Half price

age = int(input("Enter your age: "))
student = input("Are you a student (yes/no)? ").lower()

if student == "yes":
    print("Half price")
else:
    if age < 10:
        print("Free")
    elif 10 <= age <= 17:
        print("Half price")
    else:
        print("Full price")


#  Electricity Bill Calculator
# Ask units used.
# 0–100 → ₦25/unit
# 101–200 → ₦35/unit
# 201+ → ₦45/unit
# Calculate and print bill.

units = int(input("Enter units used: "))

if units <= 100:
    rate = 25
elif units <= 200:
    rate = 35
else:
    rate = 45

bill = units * rate
print("Your electricity bill is ₦", bill)


