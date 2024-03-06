# 3.1 How many seconds are in an hour? Use the interactive interpreter as a calculator and multiply the number of
# seconds in a minute (60) by the number of minutes in an hour (also 60).
# 3.2 Assign the result of the calculation of the previous assignment (seconds in an hour) to
# a variable called seconds_per_hour.
# 3.3 How many seconds are there in a day? Use the seconds_per_hour variable.
# 3.4. Count the number of seconds in a day again, but this time store the result in the seconds_per_day variable.
# 3.5. Divide the value of seconds_per_day by the value of seconds_per_hour using floating point division (/).
# 3.6 Divide the value of the seconds_per_day variable by the value of the seconds_per_hour variable
# using integer division (//). Does the result match the answer from the previous paragraph without the .0 at the end?
print(60 * 60)
seconds_per_hour = 3600
print(seconds_per_hour)
seconds_per_day = 24 * seconds_per_hour
print(seconds_per_day)
seconds_per_day / seconds_per_hour
print(seconds_per_day / seconds_per_hour)
seconds_per_day // seconds_per_hour
print(seconds_per_day // seconds_per_hour)
