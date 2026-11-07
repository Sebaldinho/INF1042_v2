"""Convertit une température en Celsius vers Fahrenheit et Kelvin."""

try:
    celsius = float(input("Température en degrés Celsius : "))
except ValueError:
    print("Veuillez entrer un nombre valide.")
else:
    if celsius < -273.15:
        print("La température ne peut pas être inférieure à -273.15 °C.")
    else:
        fahrenheit = celsius * 9 / 5 + 32
        kelvin = celsius + 273.15
        print(f"Celsius : {celsius:.2f} °C")
        print(f"Fahrenheit : {fahrenheit:.2f} °F")
        print(f"Kelvin : {kelvin:.2f} K")
