print("Welcome to the leap year calculator!")
year = int(input("Enter the year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")



#concept If the year is divisible by 4 and not divisible by 100, it is a leap year.
#If the year is divisible by 400, it is a leap year.
#Otherwise, it is not a leap year.