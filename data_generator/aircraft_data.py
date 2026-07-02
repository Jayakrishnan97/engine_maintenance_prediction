from faker import Faker
import random
from datetime import date, timedelta
import csv

fake = Faker()


previous = date(2012,1,1)
end = date(2020,12,31)

statuses = (
    ["ACTIVE"] * 24 +
    ["STORAGE"] * 3 +
    ["MAINTENANCE"] * 1 +
    ["RETIRED"] * 2 
)

random.shuffle(statuses)

models = (
    ["B737-800"] * 20 +
    ["B737-700"] * 5 +
    ["B737-900ER"] * 3 +
    ["BBJ"] * 2
)

random.shuffle(models)

folder_path = "/home/jay/Python_DSA/python/projects/engine_maintenance_prediction/data_source/dim_aircraft.csv"

fieldnames = [
    "aircraft_registration",
    "aircraft_manufacture_date",
    "aircraft_status"
]

with open(folder_path, 'w', newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(1,31):
        manufacture_date = fake.date_between_dates(previous, end)
        
        aircraft = {
            "aircraft_registration" : f"VT-JAA{i:03d}",
            "aircraft_manufacture_date" : manufacture_date,
            "aircraft_status" : statuses[i-1]
        }

        writer.writerow(aircraft)
        previous = manufacture_date