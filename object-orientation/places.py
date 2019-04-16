class Country():

    def __init__(self, name, language, area, population, source_pop_data):
        self.name = name
        self.language = language
        self.area = area
        self.population = population
        self.source_pop_data = source_pop_data
        self.states = []
        if int(area) < 0:
            raise ValueError("Value cannot be negative")
        else:
            area = self.area
        if int(population) < 0:
            raise ValueError("Population cannot be negative")
        else:
            population = self.population
        if isinstance(name, str):
            name = self.name
        else:
            raise ValueError("Name must be a string")


    def displayCountry(self):
        print('  Country: ', self.name,
              '  Language: ', self.language, 
              '  Area: ', self.area,
              '  Population: ', self.population,
              '  Source Data: ', self.source_pop_data)
    
    def addState(self, instate):
        self.states.append(instate)

    def displayAll(self):
        for state in self.states:
            state.displayState()
            state.displayLocations()
        
class State():
    
    def __init__(self, name, country, area, population, source_pop_data):
        self.name = name
        self.country = country
        self.area = area
        self.population = population
        self.source_pop_data = source_pop_data
        self.locations = []
        if int(area) < 0:
            raise ValueError("Value cannot be negative")
        else:
            area = self.area
        if int(population) < 0:
            raise ValueError("Population cannot be negative")
        else:
            population = self.population
        if isinstance(name, str):
            name = self.name
        else:
            raise ValueError("Name must be a string")
    
    def displayState(self):
        print('\n\n',
              '       State: ', self.name,
              '       Country: ', self.country,
              '       Area: ', self.area,
              '       Population: ', self.population,
              '       Source Data: ', self.source_pop_data)

    def addLocation(self, inlocation):
        self.locations.append(inlocation)

    def displayLocations(self):
        for loc in self.locations:
            loc.displayLocation()


class Location():

    def __init__(self, name, state, country, coordinates):
        self.name = name
        self.state = state
        self.country = country
        self.coordinates = coordinates
        
        if isinstance(name, str):
            name = self.name
        else:
            raise ValueError("Name must be a string")

        if isinstance(state, str):
            state = self.state
        else:
            raise ValueError("State must be a string")

    def displayLocation(self):
        print('             Location: ', self.name,
              '      Coordinates: ', self.coordinates)
