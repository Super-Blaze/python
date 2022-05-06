import datetime
import random
from brew_simulator.brew import BREWING_TIME_IN_DAYS, DAYS_IN_A_YEAR

START_DATE_OF_GRAPE_GROWING = 2022

# A szőlő kint töltött ideje két szüret között
DAYS_GRAPE_SPEND_OUTSIDE = DAYS_IN_A_YEAR - BREWING_TIME_IN_DAYS

# Átlagos napsütés idő tiszta ég mellett
MAXIMUM_SUNSHINE_TIME_IN_SUNNY_DAYS = 12
MINIMUM_SUNSHINE_TIME_IN_SUNNY_DAYS = 8

# Átlagos napsütés idő felhős idő
MAXIMUM_SUNSHINE_TIME_IN_CLOUDY_DAYS = 8
MINIMUM_SUNSHINE_TIME_IN_CLOUDY_DAYS = 2

# A cukor szint meghatározására 2 időjárással számolunk, Napos és felhős.
WEATHER_TYPES = [("Sunny", MINIMUM_SUNSHINE_TIME_IN_SUNNY_DAYS, MAXIMUM_SUNSHINE_TIME_IN_SUNNY_DAYS),
                 ("Cloudy", MINIMUM_SUNSHINE_TIME_IN_CLOUDY_DAYS, MAXIMUM_SUNSHINE_TIME_IN_CLOUDY_DAYS)]


def generate_weather():
    weather = []
    for i in range(DAYS_GRAPE_SPEND_OUTSIDE):
        # 66 %-os eséllyel süt a nap
        random_weather = random.randint(1, 3)
        if random_weather < 3:
            weather.append(WEATHER_TYPES[0])
        else:
            weather.append(WEATHER_TYPES[1])
    return weather

