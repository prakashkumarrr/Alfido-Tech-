def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return celsius_to_kelvin(fahrenheit_to_celsius(f))

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

def temperature_converter():
    print("🌡️ Temperature Converter")
    print("------------------------")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Celsius → Kelvin")
    print("4. Kelvin → Celsius")
    print("5. Fahrenheit → Kelvin")
    print("6. Kelvin → Fahrenheit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        c = float(input("Enter temperature in Celsius: "))
        print("Fahrenheit:", celsius_to_fahrenheit(c))

    elif choice == "2":
        f = float(input("Enter temperature in Fahrenheit: "))
        print("Celsius:", fahrenheit_to_celsius(f))

    elif choice == "3":
        c = float(input("Enter temperature in Celsius: "))
        print("Kelvin:", celsius_to_kelvin(c))

    elif choice == "4":
        k = float(input("Enter temperature in Kelvin: "))
        print("Celsius:", kelvin_to_celsius(k))

    elif choice == "5":
        f = float(input("Enter temperature in Fahrenheit: "))
        print("Kelvin:", fahrenheit_to_kelvin(f))

    elif choice == "6":
        k = float(input("Enter temperature in Kelvin: "))
        print("Fahrenheit:", kelvin_to_fahrenheit(k))

    else:
        print("Invalid choice! Please select from 1 to 6.")

if __name__ == "__main__":
    temperature_converter()
