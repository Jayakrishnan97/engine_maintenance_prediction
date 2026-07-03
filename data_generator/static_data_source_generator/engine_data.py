from faker import Faker
import random
from datetime import date, timedelta
import csv

fake = Faker()

previous_date = date(2016, 1, 1)
end = date(2022, 12, 31)

statuses = (
    ["INSTALLED"] * 50 +
    ["SPARE"] * 8 +
    ["SHOP"] * 1 +
    ["PRESERVED"] * 1
)
random.shuffle(statuses)

models = (
    ["CFM56-7B26"] * 45 +
    ["CFM56-7B24"] * 10 +
    ["CFM56-7B27"] * 5
)
random.shuffle(models)


fieldnames = [
    "engine_serial_number",
    "engine_model",
    "engine_family",
    "engine_manufacturer",
    "engine_manufacture_date",
    "engine_status"
]

eng_path = "/home/jay/Python_DSA/python/projects/engine_maintenance_prediction/data_source/dim_engine.csv"

with open(eng_path, "w", newline="") as file:

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(1, 61):
        manufacture_date = fake.date_between_dates(previous_date, end)

        engine = {
            "engine_serial_number": f"ESN{700000+i}",
            "engine_model": models[i-1],
            "engine_family": "CFM56",
            "engine_manufacturer": "CFM International",
            "engine_manufacture_date": manufacture_date,
            "engine_status": statuses[i-1]
        }

        writer.writerow(engine)
        previous_date = manufacture_date


    