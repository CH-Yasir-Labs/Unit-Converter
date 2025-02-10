#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chyas
#
# Created:     06/02/2025
# Copyright:   (c) chyas 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
print("---- Unit Converter ----\n")

# List of available conversions
conversions_available = [
    (1, 'km', 'miles'),
    (2, 'miles', 'km'),
    (3, 'lbs', 'kg'),
    (4, 'kg', 'lbs'),
    (5, '°F', '°C'),
    (6, '°C', '°F')
]

# Display available conversions
print("Available Conversions:")
for conversion_number, from_unit, to_unit in conversions_available:
    print(f"{conversion_number}. {from_unit} → {to_unit}")

# User selects a conversion with validation
try:
    conversion_index = int(input("\nEnter the number of conversion to use: ")) - 1
    if conversion_index not in range(len(conversions_available)):
        raise ValueError  # Triggers the error handling below
except ValueError:
    print("❌ Invalid input! Please enter a valid number.")
    exit()

# Get selected conversion
conversion_number, from_unit, to_unit = conversions_available[conversion_index]

# Get value from user
try:
    from_value = float(input(f"Enter value in {from_unit}: "))
except ValueError:
    print("❌ Invalid input! Please enter a numeric value.")
    exit()

# Perform the conversion
if conversion_number == 1:  # km to miles
    to_value = from_value * 0.621371
elif conversion_number == 2:  # miles to km
    to_value = from_value * 1.60934
elif conversion_number == 3:  # lbs to kg
    to_value = from_value * 0.453592
elif conversion_number == 4:  # kg to lbs
    to_value = from_value * 2.20462
elif conversion_number == 5:  # Fahrenheit to Celsius
    to_value = (from_value - 32) / 1.8
elif conversion_number == 6:  # Celsius to Fahrenheit
    to_value = (from_value * 1.8) + 32

# Display the result
print(f"\n✅ {from_value} {from_unit} = {to_value:.2f} {to_unit}")
