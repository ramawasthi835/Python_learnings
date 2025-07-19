# CELSIUS TO FAHRENHEIT CONVERTER

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit and return the result."""
    fahrenheit = (9/5 * celsius) + 32
    return fahrenheit

# Get temperature input from the user
try:
    temp_celsius = float(input("🌡️ Enter temperature in Celsius: "))
    temp_fahrenheit = convert_to_fahrenheit(temp_celsius)
    print(f"✅ Temperature in Fahrenheit: {temp_fahrenheit:.2f}°F")
except ValueError:
    print("❌ Invalid input. Please enter a numeric value.")

