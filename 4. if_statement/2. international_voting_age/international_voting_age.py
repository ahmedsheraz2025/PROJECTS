 
# # Write a program which asks a user for their age and lets them know if they
# # can or can't vote in the following three fictional countries.

 
 
def main():
    user_age: int = int(input("How old are you: "))
    if user_age >= 48:
        print("You can vote in Mayengua where the voting age is 48.")
    elif user_age >= 25:
        print("You can vote in Stanlauwhere the voting age is 25.")
    elif user_age >= 16:
        print("You can vote in Peturksbouipo where the votingage is 16.")
    
if __name__ == '__main__':
    main()