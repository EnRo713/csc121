def make_car(manufacturer, model, **kwargs):
    """Create a dictionary representing a car."""
    car_info = {
        'manufacturer': manufacturer,
        'model': model
    }
    car_info.update(kwargs)
    return car_info

# Call the function with required information and additional key-value pairs
car = make_car('subaru', 'outback', color='blue', tow_package=True)

# Print the dictionary returned by the function
print(car)
