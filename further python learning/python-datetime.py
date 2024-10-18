#Time concepts used from the Python DateTime Library!!!

#Checkpoint - 
import datetime
x = datetime.datetime.now()
today = datetime.date.today()
#Now(date, time down to the decimal seconds) below
print(x)
#The date today(as a date with hyphens xxxx-xx-xx) below
print(today)
#Local Time below
print(x.strftime("%X"))
#2 Digit Day below
print(x.strftime("%d"))
#2 Digit Month below
print(x.strftime("%m"))
#4 Digit Year below
print(x.strftime("%Y"))

#Challenge - Birthday Countdown!
#THIS CHALLENGE WAS LEFT UNCOMPLETED.

#Challenge - New Years Resolution Check In
import datetime
x = datetime.datetime.now()
month = (x.strftime("%m"))
day = (x.strftime("%d"))
print("It has been " + month + " months and " + day + " days since your New Years resolution. How are you doing?")

#Challenge - The Age of Programming
import datetime
x = datetime.datetime.now()
year = int(x.strftime("%Y"))
years = str(year - 1972)
print("It has been " + years + " years since the first computer program ever. Look how far we have come!")

#Challenge - Is it a Leap Year?
import datetime
x = datetime.datetime.now()
year = int(x.strftime("%Y"))
time = year - 2020
calculation = time % 4
if calculation == 0:
    print("This year " + str(year) + ", is a leap year")
else:
    print("This year " + str(year) + ", is not a leap year")

#Challenge - Holidays!
import datetime
x = datetime.datetime.now()
if month == 1:
    print("Feliz dia de los Reyes Magos!")
elif month == 2:
    print("Happy Valentines Day!")
elif month == 3:
    print("Happy St.Patrick's Day!")
elif month == 4:
    print("Happy Easter!")
elif month == 5:
    print("Happy Memorial Day!")
elif month == 6:
    print("Happy Juneteenth!")
elif month == 7:
    print("Happy Independence Day!")
elif month == 8:
    print("Happy American Family Day!")
elif month == 9:
    print("Happy Labor Day!")
elif month == 10:
    print("Happy Halloween!")
elif month == 11:
    print("Happy Thanksgiving!")
else:
    print("Merry Christmas!")