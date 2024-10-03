cars = ['kia', 'prius', 'jeep', 'subaru', 'bmw']

for car in cars:
    '''Changes the capitalization of each car brand name to be
    properly capitalized.'''
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())