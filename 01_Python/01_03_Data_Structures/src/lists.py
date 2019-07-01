fruits = [
    'Banana',
    'Apple',
    'Grapefruit',
    'Strawberry',
    'Lemon',
    'Orange',
    'Watermelon'
]

# counting the number of items
number_of_items = len(fruits)
print('Fruit count: {}'.format(number_of_items))

# adding a new item at the end of the list
fruits.append('Pineapple')
print('Adding a new item at the end of the list...')
print(fruits)
print('=' * 30)

# adding a new item at a given position
print('Adding a new item at a given position...')
fruits.insert(3, 'Blackberry')
print(fruits)
print('=' * 30)

# find an index by value
print('Find an index by value...')
print(fruits.index('Banana'))
print('=' * 30)

# sorting a list
print('Sorting a list...')
fruits.sort()
print(fruits)
print('=' * 30)

# iterating using for
print('Iterating with index using for and enumerate')
for fruit in enumerate(fruits):
    print('Fruit: {}'.format(fruit))
print('=' * 30)

# accessing the second item
number_of_items = len(fruits)
print('Accessing items:')
print('Second: {}'.format(fruits[1]))
print('Last one: {}'.format(fruits[number_of_items - 1]))
print('From the second to fifth (3,4,5):')
print(fruits[2:5])

print('From the second on... (> 2):')
print(fruits[2:])

print('Up to sixth... (<= 6):')
print(fruits[:6])

print('Last 3 elements:')
print(fruits[-3:])

print('All of them, but the last one:')
print(fruits[:-1])
print('=' * 30)

# removing one item
print('Removing one item.')
del fruits[number_of_items - 1]
print('=' * 30)

# iterating using list-comprehension
print('Iterating using list-comprehension...')
[print('Fruit: {}'.format(f)) for f in fruits]
print('=' * 30)
