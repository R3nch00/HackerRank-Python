import calendar
month,day,year=list(map(int,input().split())) #Taken input of month.day,year
Day=calendar.weekday(year,month,day) #Get the weekday of given input
print((calendar.day_name[Day]).upper()) #Used calendar.day_name to get the day name of weekday & Output shown into Uppercase
