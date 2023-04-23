#function to convert fahrenheit to celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return round(celsius, 2)

#function to convert celsius to fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit, 2)

#function to convert celsius to kelvin
def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return round(kelvin, 2)

#function to convert kelvin to celsius
def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return round(celsius, 2)

#function to convert fahrenheit to kelvin
def fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    return round(kelvin, 2)

#function to convert kelvin to fahrenheit
def kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return round(fahrenheit, 2)


