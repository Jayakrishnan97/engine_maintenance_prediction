import numpy as np
from config import WEATHER_CONDITIONS, DELAY_PROBABILITY, CANCEL_PROBABILITY

def generate_weather(n):
    return np.random.choice(WEATHER_CONDITIONS, n)


def generate_delay(n):
    delays = np.where(
        np.random.rand(n) < DELAY_PROBABILITY,
        np.random.randint(5, 120, n),
        0
    )
    return delays


def generate_status(n):
    rand = np.random.rand(n)

    status = []
    for r in rand:
        if r < CANCEL_PROBABILITY:
            status.append("CANCELLED")
        elif r < CANCEL_PROBABILITY + DELAY_PROBABILITY:
            status.append("DELAYED")
        else:
            status.append("COMPLETED")

    return status