def kelvin():
    user_celsius = float(input("Enter the celsius value to be converted to Kelvin and Fahrenheit: "))
    celsius_to_kelvin_value = user_celsius + 273.25
    celsius_to_fahrenheit_value = (user_celsius - 32) * 5 / 9
    user_fahrenheit = float(input("Enter the fahrenheit value to be converted to Celsius and Kelvin: "))
    fahrenheit_to_celsius_value = 5 / 9 * (user_fahrenheit - 32)
    fahrenheit_to_kelvin_value = 5 / 9 * (user_fahrenheit - 32) + 273
    user_kelvin = float(input("Enter the kelvin value to be converted to fahrenheit and celsius:  "))
    kelvin_to_far = 1.8 * (user_kelvin - 273) + 32
    kelvin_to_cel = user_kelvin - 273.15
