"""
Natal Chart Generator - designed to provide Natal Chart data to users.
    Copyright (C) 2025 Brando Smith
    Refer to application documentation for further information.

"""
import sys
import os
from colorama import init, Fore
from pyfiglet import Figlet
from kerykeion import AstrologicalSubject, KerykeionChartSVG, Report
from validators import (
    validate_date,
    validate_time,
    validate_latitude,
    validate_longitude,
    validate_timezone,
)

# Initialize colorama
init(autoreset=True)

class AppError(Exception):
    """Class for app exceptions"""
class InvalidTimeZoneError(AppError):
    """Class for errors raised when user inputs incorrect timezone"""
class InputCancelledError(AppError):
    """Class for closing the application when user inputs 'quit'"""

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
        birth_city,
        latitude,
        longitude,
        timezone,
        country,
    ):
        self.name = name
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.birth_city = birth_city
        self.latitude = latitude
        self.longitude = longitude
        self.timezone = timezone
        self.country = country

    def format_birth_data(self):
        """Function to format birth data"""
        print(f"Name: {self.name}")
        print(f"Date/Time: {self.year}-{self.month:02}-{self.day:02} {self.hour:02}:{self.minute:02}")
        print(f"Location: {self.birth_city} ({self.latitude}, {self.longitude})")
        print(f"Timezone: {self.timezone}")

def get_input(prompt):
    """Function to eliminate the need to write this prompt for each input"""
    full_prompt = f"(Type 'quit' to exit)\n{prompt}"
    value = input(Fore.CYAN + full_prompt)
    if value.strip().lower() == 'quit':
        raise InputCancelledError("User chose to quit.")
    return value.strip()

def get_validated_input(prompt, validator, error_message):
    """Function to validate each input for correct formatting"""
    while True:
        value = get_input(prompt)
        try:
            return validator(value)
        except ValueError as ve:
            print(Fore.RED + f"{error_message} ({ve})")


def main():
    """Function to set the font and colour at the start of the app"""  
    try:
        figlet = Figlet(font='ogre')
        ascii_art = figlet.renderText("Natal Chart Generator *")
        print(Fore.MAGENTA + ascii_art + "______________________________________________________")
        print(Fore.MAGENTA + "\n\nWARNING! You are about to share sensitive information")
        print(Fore.MAGENTA + "Your information may be shared with 3rd parties")
        print(Fore.MAGENTA + "*Accuracy may vary")
        print(Fore.MAGENTA + "______________________________________________________")
        print(Fore.MAGENTA + "\n\nWelcome, let's begin...\n")

        while True:
            try:
                #User inputs
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
                "Enter the latitude of birth place (e.g. -37.813629): ",
                validate_latitude,
                "Invalid latitude! Please enter a number like -37.813629."
                )

                longitude = get_validated_input(
                "Enter the longitude of birth place (e.g. 144.963058): ",
                validate_longitude,
                "Invalid longitude! Please enter a number like 144.963058."
                )

                timezone = get_validated_input(
                "Enter your timezone of birth country & capital city (e.g. Australia/Melbourne): ",
                validate_timezone,
                "Must match a real timezone like Australia/Melbourne."
                )
                birth_city = get_input("Enter your birth city or town (e.g. Ballarat): ")
                country = timezone.split("/")[0]
                break

            #Error handling
            except ValueError as ve:
                print(Fore.RED + f"\nValidation error: {ve}")
            except KeyboardInterrupt:
                print(Fore.RED + "\nApp interrupted. Please start again!")
            except InputCancelledError:
                print(Fore.WHITE + "\nGoodbye!")
                sys.exit()
            except InvalidTimeZoneError as e:
                print(Fore.RED + f"\nTimezone error: {e}")
            except AppError as e:
                print(Fore.RED + f"\nApplication error: {e}")

        #Instance of the AppUser class
        user_data = AppUser(
            name=name,
            year=year,
            month=month,
            day=day,
            hour=hour,
            minute=minute,
            birth_city=birth_city,
            latitude=latitude,
            longitude=longitude,
            timezone=timezone,
            country=country
        )

        user_data.format_birth_data()

        #Instance of the AstrologicalSubject class
        astro_user = AstrologicalSubject(
            name,
            year,
            month,
            day,
            hour,
            minute,
            birth_city,
            country,
            longitude,
            latitude,
            timezone
        )

        #Uncomment if using 'Generated SVGs' FOlder - Ensures path exists
        output_path = "/home/beegeeess/GitHome/Natal-Chart-App/Generated_SVGs"
        os.makedirs(output_path, exist_ok=True)

        #Uncomment and use this code if Generating SVG files to 'Generated SVGs' Folder
        birth_chart_svg = KerykeionChartSVG(astro_user, new_output_directory="/home/beegeeess/GitHome/Natal-Chart-App/Generated_SVGs")
        birth_chart_svg.makeSVG()
        print(Fore.YELLOW + f"\nChart generated and saved at {output_path}!")

        #Use this code if generating SVGs to the root folder
        birth_chart_svg = KerykeionChartSVG(astro_user)
        birth_chart_svg.makeSVG()
        print(Fore.YELLOW + "\nChart generated!")

        #Generating Sun & Moon highlight in CLI
        print(astro_user.sun)
        print(astro_user.moon)

        #Generating report to CLI
        birth_report = Report(astro_user)
        birth_report.print_report()
        print(Fore.YELLOW + "\nReports generated in the terminal!")

    except KeyboardInterrupt:
        print(Fore.RED + "\nApp interrupted. Please start again!")
    except InputCancelledError:
        print(Fore.WHITE + "\nGoodbye!")
        sys.exit()

if __name__ == "__main__":
    main()
