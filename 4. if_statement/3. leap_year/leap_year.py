 
# # Write a program that reads a year from the user and tells whether
# # a given year is a leap year or not:

def main():
    user_year: int = int(input("Enter a year I'll tell you if it is leap or not: "))
    if user_year % 4 == 0:
        print(f"This is leap year {user_year}")
    else:
        print("This is not a leap year.")
    
    
if __name__ == '__main__':
    main()

