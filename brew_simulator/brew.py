from datetime import date, timedelta
from random import randint, uniform

BREWING_TIME_IN_DAYS = 14

# Ha nem számolunk a terület földrajzi elhelyezkedésével, akkor egy átlagos 12 órás nap szakasszal számolunk
AVERAGE_DAYTIME_IN_HOURS = 12

# Nem számolunk szökőévekkel
DAYS_IN_A_YEAR = 365

# A kezdeti must alkohol szintje
BREW_STARTING_ALCOHOL_PERCENT = 0


def calculate_starting_value_of_sugar(weather):
    sun_time = 0
    for w in weather:
        rand_sun_time = randint(w[1], w[2])
        sun_time += rand_sun_time

    return parse_sun_time_to_grams_of_sugar(sun_time)


def parse_sun_time_to_grams_of_sugar(sun_time):
    print("Suntime : " + str(sun_time))
    if sun_time >= 3000:
        return round(uniform(22.1, 23), 2)
    elif sun_time >= 2800:
        return round(uniform(19.1, 22), 2)
    elif sun_time >= 2400:
        return round(uniform(16.1, 19), 2)
    else:
        return round(uniform(15.1, 16), 2)


def auto_get_starting_date():
    return date.today()


def get_starting_date():
    print("default")
    # TODO


def generate_temperature():
    return round(uniform(22, 26), 2)


def create_starting_brew_data(starting_date, starting_sugar, starting_temperature):
    brew_start_info = {"date": starting_date,
                       "alcohol": BREW_STARTING_ALCOHOL_PERCENT,
                       "sugar": starting_sugar,
                       "temperature": starting_temperature}
    return brew_start_info


def create_brew_data(starting_date, starting_sugar, starting_temperature):
    alcohol_percent = BREW_STARTING_ALCOHOL_PERCENT
    brew_data = []
    for i in range(BREWING_TIME_IN_DAYS - 1):
        starting_date += timedelta(days=1)
        starting_date_string = str(starting_date)
        sugar_decrement_amount = round(uniform(1.5, 1.7), 2)
        if starting_sugar - sugar_decrement_amount > 0:
            starting_sugar -= sugar_decrement_amount
        alcohol_increment_amount = round(uniform(0.8, 1), 2)
        alcohol_percent += alcohol_increment_amount
        starting_temperature += round(uniform(-1, 1), 2)
        brew_data.append({"date": starting_date_string,
                          "alcohol": alcohol_percent,
                          "sugar": starting_sugar,
                          "temperature": starting_temperature})
    return brew_data
