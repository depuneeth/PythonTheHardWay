states = {
    'Karnataka' : 'KA',
    'Andhra' : 'AP',
    'Tamil Nadu' : 'TN',
    'Kerala' : 'KL',
    'Telangana' : 'TS'
}

city = {
    'KA' : 'Bangalore',
    'AP' : 'Vijayawada',
    'TS' : 'Hyderabad'
}

city['TN'] = 'Tamil nadu'
city['KL'] = 'Kochi'

print('-'* 20)
print("KA state has:", city['KA'])
print("AP state has:",city['AP'])

print('-'* 20)
print("Karnataka state has:", states['Karnataka'])
print("Andhra state has:",states['Andhra'])

print('-'* 20)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

print('-' * 20)
for abbrev, cities in list(city.items()):
    print(f"{abbrev} has the city {cities}")

print('-' * 20)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {city[abbrev]}")
