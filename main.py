"""
Natal Chart Generator - designed to provide Natal Chart data to users.
    Copyright (C) 2025 Brando Smith
    Refer to application documentation for further information.

"""
import sys
from colorama import init, Fore
from pyfiglet import Figlet
from kerykeion import AstrologicalSubject, KerykeionChartSVG, Report

# Initialize colorama
init(autoreset=True)

class QuitApp(Exception):
    """Custom exception to quit the app."""
    print(None)

class AppUser:
    """Class for App Users"""
    def __init__(self, name, year, month, day, hour, minute, latitude, longitude, country, city):
        self.name = name
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.latitude = latitude
        self.longitude = longitude
        self.country = country
        self.city = city

    def format_birth_data(self):
        """Function to format birth data"""
        print(f"Name: {self.name}")
        print(f"Date/Time: {self.year}-{self.month}-{self.day} {self.hour}:{self.minute}")
        print(f"Location: {self.latitude}, {self.longitude}")
        print(f"Timezone: {self.country}/{self.city}")

def get_input(prompt):
    """Function to eliminate the need to write this prompt for each input"""
    full_prompt = f"(Type 'quit' to exit)\n{prompt}"
    value = input(Fore.CYAN + full_prompt)
    if value.strip().lower() == 'quit':
        raise QuitApp
    return value.strip()

def main():
    """Function to set the font and colour of the app header"""  
    try:
        figlet = Figlet(font='ogre')
        ascii_art = figlet.renderText("Natal Chart Generator *")
        print(Fore.MAGENTA + ascii_art + "______________________________________________________")
        print(Fore.MAGENTA + "\n\nWARNING! Your information may be shared with 3rd parties")
        print(Fore.MAGENTA + "\nWelcome, let's begin...\n")

        name = get_input("Enter your name or alias: ").title()
        birthdate = get_input("Enter your birthdate (YYYY-MM-DD): ")
        birthtime = get_input("Enter your birthtime (HH:MM 24 hour time): ")
        latitude = float(get_input("Enter the latitude (e.g. -37.813629): "))
        longitude = float(get_input("Enter the longitude (e.g. 144.963058): "))
        country_capital_city = get_input("Enter your timezone (Country/Capital City: ")
        city_region = get_input("Enter your birth town or city: ")

        try:
            year, month, day = map(int, birthdate.split("-"))
            hour, minute = map(int, birthtime.split(":"))
            country, city_region = country_capital_city.split("/")
        except KeyboardInterrupt:
            print(Fore.RED + "App interrupted. Enter again.")
        except ValueError:
            print(Fore.RED + "Invalid format. Please restart the app and try again.")
        sys.exit()

        user = AppUser(
            name,
            year,
            month,
            day,
            hour,
            minute,
            latitude,
            longitude,
            country,
            city_region
        )

        user.format_birth_data()

        subject = AstrologicalSubject(
            name,
            year,
            month,
            day,
            hour,
            minute,
            city_region,
            country,
            longitude,
            latitude,
        )

        chart = KerykeionChartSVG(subject)
        chart.makeSVG()

        print(Fore.YELLOW + "\nChart generated and saved.")

    except QuitApp:
        print(Fore.WHITE + "\nGoodbye!")
        sys.exit()

if __name__ == "__main__":
    main()
