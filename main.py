#1. Check whether the year is a leap year or not

# Input: year to check
year = 2024
# Leap year: divisible by 4 and not by 100, or divisible by 400
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
 print(f"{year} is a leap year.")
else:
 print(f"{year} is NOT a leap year.")

 #2. Check whether the number is positive, negative or zero

# Input: number to check
num = -7
if num > 0:
 print(f"{num} is a positive number.")
elif num < 0:
 print(f"{num} is a negative number.")
else:
 print("The number is zero.")


#3. Program to print Largest of three numbers

# Input: three numbers
a = 12
b = 45
c = 27
# Compare the numbers
if a >= b and a >= c:
 largest = a
elif b >= a and b >= c:
 largest = b
else:
 largest = c
print(f"The largest of {a}, {b} and {c} is: {largest}")
