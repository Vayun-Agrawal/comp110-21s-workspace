"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730358299"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    daystotarget: int = int(days_to_target(population, doses, doses_per_day, target))
    targdate: str = future_date(daystotarget)
    print("We will reach " + str(target) + "% vaccination in " + 
    str(daystotarget) + " days, which falls on " + str(targdate) + ".")


def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """Calculates the number of days left until target percentage is reached."""
    totdose: int = (population * 2)
    daysleft: float = (totdose * (target / 100)) - (doses)
    day: int = round(daysleft / doses_per_day)
    return(day)


def future_date(x: int) -> str:
    """Calculates the date on which the target percentage of vaccination will be reached."""
    datetoday: datetime = datetime.today()
    days2: timedelta = timedelta(x)
    tardate: datetime = datetoday + days2
    returndate: str = str(tardate.strftime("%B %d, %Y"))
    return(returndate)


if __name__ == "__main__":
    main()
