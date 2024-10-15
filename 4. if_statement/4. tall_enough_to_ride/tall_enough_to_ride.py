
# # Write a program which asks the user how tall they are and prints
# # whether or not they're taller than a pre-specified minimum height:


def main():
    user_input: int = int(input("Enter you age: "))
    if user_input >= 10:
        print("You're tall enough to ride.")
    else:
        print("You're not tall enough to ride, Maybe next year.")
    
    
if __name__ == '__main__':
    main()
