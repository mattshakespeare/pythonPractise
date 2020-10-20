temps = [[0.0 for h in range(24)] for d in range(31)]
#
#Matrix magically updated here
#

#Finds the average temperature at noon in a month
total = 0.0

for day in temps:
    total += day[11]

average = total / 31

#Finds the highest temperature during the whole month

highest = -100.00

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

#Counts the days when the temperature at noon was at least 20 degrees
hotDays = 0 

for days in temps:
    if day[11] > 20.0:
        hotDays += 1
