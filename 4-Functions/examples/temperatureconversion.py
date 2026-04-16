def convert_temperature(temp,unit):
    """Converts temperature between Celsius and Fahrenheit."""
    if unit == "C":
        fahrenheit = (temp * 9/5) + 32
        return fahrenheit
    elif unit == "F":
        return (temp - 32) * 5/9
    else:
        return "Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit."

print(convert_temperature(27, "C"))  # Output: 32.0
print(convert_temperature(2, "F"))  # Output: 0.0