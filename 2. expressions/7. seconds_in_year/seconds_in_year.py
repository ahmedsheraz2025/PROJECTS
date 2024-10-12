
# Use Python to calculate the number of seconds in a year,
# and tell the user what the result is in a nice print statement


DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MINTUES: int = 60


def main():
    second_per_year = (DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MINTUES)
    print(f"There are {second_per_year} seconds in a year!")
if __name__ == '__main__':
    main()