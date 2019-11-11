#!/usr/bin/env python3.8

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    
    return ', '.join(cars['Jeep'])

def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    
    first_model = [car[0] for car in cars.values()]

    return first_model

def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    
    matches = [model for models in cars.values() for model in models if grep.lower() in model.lower()]

    return sorted(matches)

def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    
    for models in cars.values():
        models.sort()

    return cars

print(get_all_jeeps())
print(get_first_model_each_manufacturer())
print(get_all_matching_models(cars, 'CO'))
print(sort_car_models())