def is_leap(year):
    if year%4==0:
        if year%100==0:
            return True if year%400==0 else False
        else:
            return True
    else:
        return False


def days_in_months(year,month):
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    return "Invalid month" if month<=0 and month>=13 else 29 if is_leap(year) else month_days[month-1]

year = int(input("enter year"))
month = int(input("enter month"))

print(days_in_months(year,month))