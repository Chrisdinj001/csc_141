def make_car(manufacturer, model, **options):
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
    }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict

my_electra = make_car('hyundai', 'electra', color='black', tow_package=True)
print(my_electra)

my_old_civic = make_car('honda', 'civic', year=2018, color='silver', headlights='popup')
print(my_old_civic)