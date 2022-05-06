import json
import webbrowser
from brew_simulator.brew import calculate_starting_value_of_sugar, BREW_STARTING_ALCOHOL_PERCENT, \
    auto_get_starting_date, get_starting_date, generate_temperature, create_starting_brew_data, create_brew_data
from brew_simulator.weather_generator import generate_weather


def simulate(run_mode):
    # A program auto mod check-je
    is_auto = run_mode == "auto"
    # Legeneráljus az időjárást az év minden napjára, kivéve a szüret és maga az erjedés szakaszában
    weather = generate_weather()
    brew_data = {"data": []}
    # A kezdeti értékeket beállítjuk
    starting_date, starting_sugar, starting_temperature = create_starting_values(is_auto, weather)
    # Létrehozzuk az erjedés 0. napjának adatait, mai kezdődátummal, ha auto mod-ban fut a program
    starting_date_string = str(starting_date)
    starting_brew_data = create_starting_brew_data(starting_date_string, starting_sugar, starting_temperature)
    generated_brew_data = create_brew_data(starting_date, starting_sugar, starting_temperature)
    brew_data["data"].append(starting_brew_data)
    for brew_dict in generated_brew_data:
        brew_data["data"].append(brew_dict)
    create_json_file(brew_data)


def create_starting_values(is_auto, weather):
    starting_sugar = calculate_starting_value_of_sugar(weather)
    starting_date = auto_get_starting_date() if is_auto else get_starting_date()
    starting_temperature = generate_temperature()
    return starting_date, starting_sugar, starting_temperature


def create_json_file(brew_data):
    with open('test.json', 'w') as file:
        json.dump(brew_data, file, indent=4)
        webbrowser.open('test.json')
