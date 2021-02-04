"""A vaccination calculator."""

__author__ = "730358299"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population = int(input("Population: "))
doses_administered = int(input("Doses Administered: "))
doses_per_day = int(input("Doses Per Day: "))
target_percent = int(input("Target Percent Vaccinated: "))
doses_remaining = population - doses_administered
days_remaining = doses_remaining / doses_per_day
string = str(days_remaining)
print("It will take " + string + " days to fully vaccinate the population.")