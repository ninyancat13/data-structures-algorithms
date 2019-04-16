from places import *

print("\nTesting Addition\n")

    #def __init__(self, name, language, area, population, source_pop_data):
try:
    Europe = Country("Europe", "English", "123", -1000, "Census")
except ValueError:
    print("Test Passed")
else:
    print("Test Failed")



    #def __init__(self, name, country, area, population, source_pop_data):
try:
    Florida = State("Florida", "America", "-345", "3422", "Census")
except ValueError:
    print("Test Passed")
else:
    print("Test Failed")


    #def __init__(self, name, state, country, coordinates):
try:
    KingsPark = Location("KingsPark", 100, "Australia", "322")
except ValueError:
    print("Test Passed")
else:
    print("Test Failed")
