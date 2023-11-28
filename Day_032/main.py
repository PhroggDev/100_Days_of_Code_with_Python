import datetime as dt

now = dt.datetime.now()

birth_day = dt.datetime(year=1961, month=10, day=3)

print(f"You were born on {birth_day.strftime('%D')}")
