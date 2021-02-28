"""Main Function for the toolkit."""

import os
import sys
from app_settings import settings_menu
from Parameter_Xref.paramxref import param_xref
from Drive_Connected_Tools.drivetools import drive_tools_main


def startup():
    """Gets terminal size, displays title"""
    clear()
    size = os.get_terminal_size()
    center = size[0] / 2
    print("PF525 Toolkit".center(int(center)))

def clear():
    """Clears the Terminal"""
    os.system('cls')

def main():
    """Main Routine calling separate functions and containing main loop"""
    startup()
    while True:
        print("""Select a tool:
(1) Parameter Cross Reference
(2) Drive Connected Tools
(3) Parameter Help
(4) L5X Generator
(5) Settings
(Q) Quit
""")
        sel = input('>>> ')
        if sel.lower() == "1":
            param_xref()
        elif sel.lower() == "2":
            drive_tools_main()
        elif sel.lower() == "3":
            #TODO Parameter Help
            continue
        elif sel.lower() == "4":
            #TODO L5X Generator
            continue
        elif sel.lower() == "5":
            settings_menu()
        elif sel.lower() == "q":
            sys.exit()
        else:
            print("Invalid Selection")

if __name__ == "__main__":
    main()
