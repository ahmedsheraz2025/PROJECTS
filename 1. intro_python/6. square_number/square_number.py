
# Ask the user for a number and print its square

def main():
    
    number : float = float(input("Enter the number to see it's square: "))
    
    # Sqaure the user input number:
    
    squared_number = f"Sqaured number is: " + str(number**2)
    
    # Print it:
    
    print(squared_number)
    
if __name__ == '__main__':
    main()