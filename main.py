"""
Natal Chart Generator - designed to provide Natal Chart data to users.
    Copyright (C) 2025 Brando Smith
    Refer to application documentation for further information.

"""
import sys
from datetime import datetime
import pytz
from colorama import init, Fore
from pyfiglet import Figlet
from kerykeion import AstrologicalSubject, KerykeionChartSVG, Report

# Initialize colorama
init(autoreset=True)

class QuitApp(Exception):
    """Python class 'Exception' used to quit the app swiftly."""

class AppUser:
    """Class for the app users' birth data"""
    def __init__(
        self,
        name,
        year,
        month,
        day,
        hour,
        minute,
        latitude,
        longitude,
        timezone,
        country,
        city
    ):
        self.name = name
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.latitude = latitude
        self.longitude = longitude
        self.timezone = timezone
        self.country = country
        self.city = city

    def format_birth_data(self):
        """Function to format birth data"""
        print(f"Name: {self.name}")
        print(f"Date/Time: {self.year}-{self.month}-{self.day} {self.hour}:{self.minute}")
        print(f"Location: {self.latitude}, {self.longitude}")
        print(f"Timezone: {self.timezone}")
        #print(f"Timezone: {self.country}/{self.city}")

def get_input(prompt):
    """Function to eliminate the need to write this prompt for each input"""
    full_prompt = f"(Type 'quit' to exit)\n{prompt}"
    value = input(Fore.CYAN + full_prompt)
    if value.strip().lower() == 'quit':
        raise QuitApp
    return value.strip()


def get_validated_input(prompt, validator, error_message):
    """Function to validate each input for correct formatting"""
    while True:
        value = get_input(prompt)
        try:
            return validator(value)
        except ValueError as ve:
            print(Fore.RED + f"{error_message} ({ve})")

def validate_date(date_str):
    """Function to align input with datetime library for formatting"""
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return dt.year, dt.month, dt.day

def validate_time(time_str):
    """Function to align input with datetime library for formatting"""
    tm = datetime.strptime(time_str, "%H:%M")
    return tm.hour, tm.minute

def validate_float(value_str):
    """Function to ensure coordinate input is in decimal format"""
    return float(value_str)

def validate_timezone(tz_str):
    """Function to align input with pytz library for timezone"""
    if tz_str not in pytz.all_timezones:
        raise ValueError("Invalid timezone")
    return tz_str

def main():
    """Function to set the font and colour at the start of the app"""  
    try:
        figlet = Figlet(font='ogre')
        ascii_art = figlet.renderText("Natal Chart Generator *")
        print(Fore.MAGENTA + ascii_art + "______________________________________________________")
        print(Fore.MAGENTA + "\n\nWARNING! Your information may be shared with 3rd parties")
        print(Fore.MAGENTA + "\nWelcome, let's begin...\n")

        while True:
            try:
                #The app input to collect birth data
                # name = get_input("Enter your name or alias: ").title()
                # birthdate = get_input("Enter your birthdate (YYYY-MM-DD): ")
                # birthtime = get_input("Enter your birthtime (HH:MM 24 hour time): ")
                # latitude = float(get_input("Enter the latitude (e.g. -37.813629): "))
                # longitude = float(get_input("Enter the longitude (e.g. 144.963058): "))
                # country_capital_city = get_input("Enter your timezone (Country/Capital City: ")
                # city_region = get_input("Enter your birth town/Country: ")

                name = get_input("Enter your name or alias: ").title()

                year, month, day = get_validated_input(
                    "Enter your birthdate (YYYY-MM-DD): ",
                    validate_date,
                    "Invalid date format! Please use YYYY-MM-DD."
                )

                hour, minute = get_validated_input(
                "Enter your birthtime (HH:MM 24 hour time): ",
                validate_time,
                "Invalid time format! Please use HH:MM (24-hour)."
                )

                latitude = get_validated_input(
                "Enter the latitude (e.g. -37.813629): ",
                validate_float,
                "Invalid latitude! Please enter a number like -37.813629."
                )

                longitude = get_validated_input(
                "Enter the longitude (e.g. 144.963058): ",
                validate_float,
                "Invalid longitude! Please enter a number like 144.963058."
                )

                timezone = get_validated_input(
                "Enter your timezone (e.g. Australia/Melbourne): ",
                validate_timezone,
                "Invalid timezone! Must match a real timezone like Australia/Melbourne."
                )
                country, city = timezone.split("/")

                # #Formatting each input section
                # year, month, day = map(int, birthdate.split("-"))
                # hour, minute = map(int, birthtime.split(":"))
                # country, city_region = country_capital_city.split("/")
                break

            except KeyboardInterrupt:
                #Message printed if user accidentally interrupts the app
                print(Fore.RED + "App interrupted. Enter again.")
            except ValueError:
                #Message printed if the user inputs data in an invalid format
                print(Fore.RED + "Invalid format. Please restart the app and try again.")
                sys.exit()

        #Instance of the AppUser class
        user = AppUser(
            name,
            year,
            month,
            day,
            hour,
            minute,
            latitude,
            longitude,
            timezone,
            country,
            city
        )

        user.format_birth_data()

        user = AstrologicalSubject(
            name,
            year,
            month,
            day,
            hour,
            minute,
            city,
            country,
            longitude,
            latitude,
            timezone,
        )

        birth_chart_svg = KerykeionChartSVG(user, new_output_directory="/home/beegeeess/GitHome/Natal-Chart-App/Generated_SVGs")
        birth_chart_svg.makeSVG()

        print(Fore.YELLOW + "\nChart generated and saved..")

    except KeyboardInterrupt:
        print(Fore.RED + "\nApp interrupted. Please start again!")
    except QuitApp:
        print(Fore.WHITE + "\nGoodbye!")
        sys.exit()

if __name__ == "__main__":
    main()
