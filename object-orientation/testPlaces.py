from places import Country
from places import State
from places import Location
import pickle
countries = []
states = []
objectlist = []

fileobj = open('location_v1.2b.csv')
lines = fileobj.readlines()
#print(lines)

for line in lines:
    linesplit = line.split(":")
    #print(linesplit)
    try:
        if linesplit[0] == "COUNTRY":
            temp = Country(linesplit[1][5:], linesplit[3][9:], 
                    linesplit[4][5:], linesplit[5][11:], linesplit[6][7:])
            #temp.displayCountry()
            countries.append(temp)


        if linesplit[0] == "STATE":
            temp = State(linesplit[3][10:], linesplit[2][8:], 
                    linesplit[4][5:], linesplit[6][11:], linesplit[7][7:])
            #temp.displayState()
            states.append(temp)
            for country in countries:
                if country.name == temp.country:
                    country.addState(temp)


        if linesplit[0] == "LOCATION":
            temp = Location(linesplit[1][5:], linesplit[2][6:], 
                    linesplit[3][8:], linesplit[4][7:])
            #temp.displayLocation()
            for state in states:
                if state.name == temp.state:
                    state.addLocation(temp)
    
    except ConstructorError as error:
        print(error)

for country in countries:
    country.displayCountry()
    country.displayAll()
    objectlist.append(country)

#pickle.dump(countries, open("places.bin", "wb"))
#with open('places.bin', 'wb') as dataFile:
#        pickle.dump(objectlist, dataFile)

pickle.dump(objectlist, open("places.bin", "wb"))

temp1 = pickle.load(open("places.bin", "rb"))
print(temp1)

for country in temp1:
    country.displayCountry()
    country.displayAll()

