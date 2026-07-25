def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0: 
        return False
    if year % 4 == 0:
        return True
    else: 
        return False

year = 2003

if is_leap_year(year) == True: 
    print("It's a leap year!")
elif is_leap_year(year) == False: 
    print("It's not a leap year!")
