
# Prompt the user to enter the lengths of each side of a triangle
# and then calculate and print the perimeter of the triangle

def main():
    
    # Prompt the user to enter the lengths of each side of a triangle:
    
    user_input_side_1 = int(input("Enter the length first side: "))
    user_input_side_2 = int(input("Enter the length second side: "))
    user_input_side_3 = int(input("Enter the length third side: "))
    
    # Calculate the perimeter of the triangle:
    
    sum_of_all_sides = ("Perimeter of the triangle: " + str(user_input_side_1 + user_input_side_2 + user_input_side_3))
    
    # Print sum of all sides:
    
    print(sum_of_all_sides)
    
if __name__ == '__main__':
    main()
    