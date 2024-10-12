
# Ask the user for two numbers, one at a time, and then print the
# result of dividing the first number by the second and also the remainder of the division.

def main():
    dividend : int = int(input("Enter an integer to be divided: "))
    divided: int = int(input("Enter an integer to divide by: "))
    
    quotient = dividend // divided
    remainder = dividend % divided
    
    print(f"The result of division {quotient} and its remainder {remainder}")
    
if __name__ == '__main__':
    main()