import pandas as pd
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return (f"{temp}{DEGREE_SYBMOL}")

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    converted_date = datetime.fromisoformat(iso_string).date()
    formatted_date = converted_date.strftime('%A %d %B %Y')
    return formatted_date


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    return round(5/9 * (float(temp_in_farenheit) - 32),1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    total = 0
    for data in weather_data:
        total+=float(data)
    return total/len(weather_data)

def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    csv_data=[]
    with open(csv_file,'r') as file:
        reader = pd.read_csv(file,delimiter=',')
        for row in (pd.DataFrame(reader)).itertuples():
            csv_data.append(list(row[1:]))
        return csv_data


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    for i in range(0, len(weather_data)):
        weather_data[i] = float(weather_data[i])
    try:
        minimum_value = min(weather_data)
        min_index = []
        for i in range(0, len(weather_data)): 
            if (weather_data[i] == minimum_value):
                min_index.append(i)
        min_value_and_position = (minimum_value, min_index[-1])
    except ValueError:
        min_value_and_position = ()
    return min_value_and_position


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    for i in range(0, len(weather_data)):
        weather_data[i] = float(weather_data[i])
    try:
        maximum_value = max(weather_data)
        max_index = []
        for i in range(0, len(weather_data)): 
            if (weather_data[i] == maximum_value):
                max_index.append(i)
        max_value_and_position = (maximum_value, max_index[-1])
    except ValueError:
        max_value_and_position = ()
    return max_value_and_position


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    low_temp = []
    for data in weather_data:
        low_temp.append(data[1])
    lowest_temp = find_min(low_temp)
    coldest_day = convert_date(weather_data[lowest_temp[1]][0])
    coldest_temp = format_temperature(convert_f_to_c(lowest_temp[0]))

    high_temp = []
    for data in weather_data:
        high_temp.append(data[2])
    highest_temp = find_max(high_temp)
    warmest_day = convert_date(weather_data[highest_temp[1]][0])
    warmest_temp = format_temperature(convert_f_to_c(highest_temp[0]))
    average_low = format_temperature(convert_f_to_c(calculate_mean(low_temp)))
    average_high = format_temperature(convert_f_to_c(calculate_mean(high_temp)))
    return (f"{len(weather_data)} Day Overview\n  "
            f"The lowest temperature will be {coldest_temp}, and will occur on {coldest_day}.\n  "
            f"The highest temperature will be {warmest_temp}, and will occur on {warmest_day}.\n  "
            f"The average low this week is {average_low}.\n  "
            f"The average high this week is {average_high}.\n")


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    daily_summary = ''
    for data in weather_data:
        daily_summary+=(f"---- {convert_date(data[0])} ----\n  "
        f"Minimum Temperature: {format_temperature(convert_f_to_c(data[1]))}\n  "
        f"Maximum Temperature: {format_temperature(convert_f_to_c(data[2]))}\n\n")
    return daily_summary
