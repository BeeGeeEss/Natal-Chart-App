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

def app_header():
    """Function to set the font and colour of the app header"""    
    figlet = Figlet(font='ogre')
    ascii_art = figlet.renderText("Natal Chart Generator *")
    print(Fore.MAGENTA + ascii_art + "______________________________________________________")

def app_welcome():
    """Function to welcome the user to the app"""
    print(Fore.MAGENTA + "\nWelcome, let's begin...\n")










if __name__ == "__main__":
    app_header()
    app_welcome()
