#!/usr/bin/env python
# encoding: utf-8

# 关于dictionary dic.items()

# create a mapping of state to abbreviation
states = {
        'Oregon': 'OR',
        'Florida': 'FL',
        'California': 'CA',
        'New York': 'NY',
        'Michigan': 'MI'
        }

# create a basic set of states and some cities in them
cities = {
        'CA': 'San Francisco',
        'MI': 'Detroit',
        'FL': 'Jacksonville'
        }

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print some states
print('-' * 10)
print('Michigan\'s abbreviation is: ', states['Michigan'])
print('Florida\'s abbreviation is: ', states['Florida'])

# print every state abbreviation
print('-' * 10)
for state, abbrev in states.items():
    print('{} is abbreviated {}'.format(state, abbrev))

# print every city in state
print('-' * 10)
for abbrev, city in cities.items():
    print('{} has the city {}'.format(abbrev, city))

# now do both at the same time
print('-' * 10)
for state, abbrev in states.items():
    print('{} state is abbreviated {} and has city {}'.format(state, abbrev, cities[abbrev]))

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print('Sorry, no Texas.')

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print('The city for the state \'TX\' is:{}'.format(city))
