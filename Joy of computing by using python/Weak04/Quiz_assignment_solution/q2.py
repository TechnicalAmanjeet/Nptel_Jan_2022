def leap_year(year):
    if year % 400 == 0 or year % 4 == 0:
        print("It's a leap year")
    if year % 100 == 0:
        print("Not a leap year")

year = int(input("Enter year : "))
leap_year(year)
