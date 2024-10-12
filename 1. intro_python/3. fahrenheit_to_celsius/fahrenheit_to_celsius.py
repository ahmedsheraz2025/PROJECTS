
# Write a program which prompts the user for a temperature in Fahrenheit
# and outputs the temperature converted to Celsius.

def main():
    
    # Input the user for a temperature in Fahrenheit:
    
    user_input_fahrenheit = int(input("Enter the temperature in Fahrenheit: "))
    
    # Convert Fahrenheit into Celsius:
    
    degree_celsius = (user_input_fahrenheit - 32)* 5.0/9.0
    
    # Outputs the temperature converted to Celsius:
    
    print(degree_celsius)
    
if __name__ == '__main__':
    main()