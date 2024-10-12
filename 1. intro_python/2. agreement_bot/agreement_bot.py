
# Write a program which asks the user what their favorite animal is,
# and then always responds with "My favorite animal is also ___!"



def main():
    # Asks the user what their favorite animal:

    favorite_animal = input("What's your favorite animal? ")

    # Always responds with "My favorite animal is also ___!:
    
    my_favorite_animal = (f"My favorite animal is also {favorite_animal}")
    
    print(my_favorite_animal)
    
if __name__ == '__main__':
    main()