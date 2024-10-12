
# Converts feet to inches. Feet is an American unit of measurement.
# There are 12 inches per foot. Foot is the singular, and feet is the plural.

FOOT_PER_INCH = 12

def main():
    feet : float = float(input("Enter number of feel: "))
    
    # Converts feet to inches:
    
    convert_feet_to_inches = feet * FOOT_PER_INCH 
    
    # Print it:
    
    print(convert_feet_to_inches)
    
if __name__ == '__main__':
    main()