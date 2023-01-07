
fruits = {
    "Apple" : 130,
    "Avocado" : 50,
    "Banana" : 111,
    "Cantaloupe" : 50,
    "Grapefruit" : 60,
}

fruit_asked = input('Fruit: ')

for key in fruits:
    if key == fruit_asked:
        print('Calories:', fruits[key])
    

