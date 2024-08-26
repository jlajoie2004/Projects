# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Julie La Joie
# Section:      521
# Assignment:   Lab: Topic 11
# Date:         16 November 2022

# Weather data

with open("WeatherDataCLL.csv") as file:
    lines = file.readlines()

header = lines[0].strip().split(",")
lines.remove(lines[0])
data = {}
for line in lines:
    today = line.strip().split(",")
    data[today[0]] = {}
    for i in range(1, len(header)):
        data[today[0]][header[i]] = float(today[i])

high_temp = []
low_temp = []
precip = []

for key in data:
    high_temp.append(data[key]["Maximum Temperature (F)"])
    low_temp.append(data[key]["Minimum Temperature (F)"])
    precip.append(data[key]["Precipitation (in)"])

max_temp = max(high_temp)
min_temp = min(low_temp)
avg_pre = sum(precip)/len(precip)

print(f'3-year maximum temperature: {max_temp:.0f} F')
print(f'3-year minimum temperature: {min_temp:.0f} F')
print(f'3-year average precipitation: {avg_pre:.3f} inches')

month = input("Please enter a month: ")
year = input("Please enter a year: ")
print("\n")

calendar = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12 }
date1 = str(calendar[month]) + "/"
date2 = "/" + year

avg = []
wind = []
precip2 = []

for i in range(1,32):
    date = date1 + str(i) + date2
    if date in data:
        avg.append(data[date]["Maximum Temperature (F)"])
        wind.append(data[date]["Average Daily Wind Speed (mph)"])
        precip2.append(data[date]["Precipitation (in)"])

avg_temp = sum(avg)/len(avg)
avg_wind = sum(wind)/len(wind)

high_wind = 0
for day in wind:
    if day > 10:
        high_wind += 1

high_wind /= len(wind)/100
avg_precip = sum(precip2)/len(precip2)

rainy = 0
for day in precip2:
    if day > 0:
        rainy += 1

rainy /= len(precip2)/100

print(f'For {month} {year}:')
print(f'Mean maximum daily temperature: {avg_temp:.1f} F')
print(f'Mean daily wind speed: {avg_wind:.2f} mph')
print(f'Percentage of days with precipitation: {rainy:.1f}%')

file.close()



