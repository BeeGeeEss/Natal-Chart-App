"""
Natal Chart Generator - designed to provide Natal Chart data to users.
    Copyright (C) 2025 Brando Smith
    Refer to application documentation for further information.

"""
from colorama import init, Fore
from pyfiglet import Figlet
from kerykeion import AstrologicalSubject, KerykeionChartSVG, Report

# Initialize colorama
init(autoreset=True)

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
 
def get_user_name():
    """Function for user input"""
    name = input(Fore.CYAN + "Type 'quit' at anytime to exit\nEnter your name or alias: ")
    return name.title().strip()

def get_user_birthdate():
    """Function for user input"""
    birthdate = input(Fore.CYAN + "Type 'quit' at anytime to exit\nEnter you birthdate (Format: YYYY-MM-DD): ")
    return birthdate

def get_user_birthtime():
    """Function for user input"""
    birthtime = input(Fore.CYAN + "Type 'quit' at anytime to exit\nEnter you birthtime (Format: HH:MM): ")
    return birthtime

def get_user_latitude():
    """Function for user input"""
    lat = input(Fore.CYAN + "Type 'quit' at anytime to exit\nEnter the latitude of the town that you were born in \n(Format: Find the coordinates of your birth town on google maps, enter the first coordinate, to 6 decimal places (i.e 13.987653 or 543.876532)): ")
    return lat

def get_user_longitude():
    """Function for user input"""
    lon = input(Fore.CYAN + "Type 'quit' at anytime to exit\nEnter the longitude of the town that you were born in \n(Format: Find the coordinates of your birth town on google maps, enter the second coordinate, to 6 decimal places (i.e 13.987653 or 543.876532)): ")
    return lon

def get_user_location():
    """Function for user input"""
    location = input(Fore.CYAN + "Type 'quit' at anytime to exit\nEnter the State and Country that you were born in (Format: Australia/Melbourne): ")
    return location

def get_user_birthplace():
    """Function for user input"""
    birthplace = input(Fore.CYAN + "Type 'quit' at anytime to exit\nEnter the town that you were born in (Format: Ballarat): ")
    return birthplace

def main():
    """Function to set the font and colour of the app header"""    
    figlet = Figlet(font='ogre')
    ascii_art = figlet.renderText("Natal Chart Generator *")
    print(Fore.MAGENTA + ascii_art + "______________________________________________________")
    print(Fore.MAGENTA + "\nWarning! Please be aware that you are entering sensitive data into an app, this information may be shared with third parties. \n\nWelcome, let's begin...\n")

    while True:
        try:
            name = get_user_name()
            birthdate = get_user_birthdate()
            if name.lower() == "quit":
                print(Fore.WHITE + "Goodbye!")
                break
        
            return name

        except KeyboardInterrupt:
            print(Fore.RED + "App interrupted. Enter again.")
    





if __name__ == "__main__":
    main()
