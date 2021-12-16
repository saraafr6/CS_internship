"""EXAMINING A LIST In this lab, the task is to read a set of temperature
data (the monthly high temperatures at Heathrow Airport for 1948 through
2016) from a file and then find some basic information: the highest and lowest temperatures, the mean (average) temperature, and the median temperature (the temperature in the middle if all the temperatures are sorted).
The temperature data is in the file lab_05.txt in the source code directory for
this chapter. Because I haven’t yet discussed reading files, here’s the code to
read the files into a list:
temperatures = []
with open('lab_05.txt') as infile:
for row in infile:
temperatures.append(int(row.strip())
You should find the highest and lowest temperature, the average, and the
median. You’ll probably want to use the min(), max(), sum(), len(),
and sort() functions/methods.
BONUS Determine how many unique temperatures are in the list.
"""
temperatures = []
with open("lab_05.txt") as infile:
    for row in infile:
        temperatures.append(int(row.strip()))
minimum = min(temperatures)
maximum = max(temperatures)
average = sum(temperatures) / len(temperatures)
sorted_temperatures = sorted(temperatures)
len_s = len(sorted_temperatures)

if len_s % 2 == 0:
    x = sorted_temperatures[(len_s // 2) - 1]
    y = sorted_temperatures[(len_s // 2)]
    median = (x + y) / 2
else:
    median = sorted_temperatures[len_s // 2]

print("minimum is:", minimum)
print("maximum is:", maximum)
print("average is:", average)
print("median is:", median)

myset = set(temperatures)
unique = len(myset)
print("len temperatures", len(temperatures))
print("unique temperatures is:", unique)
