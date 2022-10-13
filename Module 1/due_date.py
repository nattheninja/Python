# create variables for time units
print("What day is this assignment due? (MM/DD/YYYY)")
day = input("Day?")
month = input("Month?")
year = input("Year?")

print("What time is this assignment due? (HH:MM)")
time_hour = input("Time in hours?")
time_min = input("Time in minutes?")
am_pm = input("AM or PM?")

print("Module 1 Assignment is due on " + \
      month + "/" + day + "/" + year + " at " + \
      time_hour + ":" + time_min + " " + am_pm + " EST.")
