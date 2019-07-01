countries = {
    'BR': {
        'name': 'Brazil',
        'currency_code': 'BRL'
    },
    'PL': {
        'name': 'Poland',
        'currency_code': 'PLN'
    },
    'IT': {
        'name': 'Italy',
        'currency_code': 'EUR'
    }
}

currencies = {
    'BRL': 'Brazilian Real',
    'PLN': 'Polish Zloty',
    'EUR': 'Euro'
}

# accessing element
print('Accessing element by key:')
print(countries['BR'])
print('=' * 30)

print('Getting the key list:')
print(countries.keys())
print('=' * 30)

# adding a new key
print('Adding a new key and value.')
countries['FR'] = {
    'name': 'France',
    'currency_code': 'EUR'
}
print('=' * 30)

# iterating over a keylist
print('Iterating and accessing elements:')
for country_key in countries:
    currency_code = countries[country_key]['currency_code']
    country_name = countries[country_key].get('name')
    currency_name = currencies[currency_code]

    print('{}: {}'.format(
        country_name,
        currency_name
    ))
print('=' * 30)

# counting number of keys
print('Counting the number of items:')
print(len(countries))
print('=' * 30)

# removing an item by key
print('Removing an item.')
del countries['FR']
print('=' * 30)

# iterating using list-comprehension
[print(v) for k, v in countries.items()]
