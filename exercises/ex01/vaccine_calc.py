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
days_remaining = int((doses_remaining / doses_per_day) * (target_percent / 100))
string_days_remaining = str(days_remaining)
string_percent = str(target_percent)
today: datetime = datetime.today()
days_rem_td: timedelta = timedelta(days_remaining)
future: datetime = today + days_rem_td
print("We will reach " + string_percent + "% vaccination in " + string_days_remaining + " days")
print(future.strftime("%B %d, %Y"))
