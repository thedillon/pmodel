# This is a sample Python script.
from openap import prop
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.






def yankModels():
    aircraft = prop.aircraft('A320')
    attrs = dir(aircraft)

    # Print the attributes and methods
    for attr in attrs:
        print(attr)
if __name__ == '__main__':
    yankModels()
    