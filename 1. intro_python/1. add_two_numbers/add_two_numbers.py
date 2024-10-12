
# Write a Python program that takes two integer inputs from the
# user and calculates their sum. The program should perform the following tasks:


def main():

    # 1. Prompt the user to enter the first number.

    first_number = input("Enter the first number: ")

    # 2. Read the input and convert it to an integer.

    convert_first_number = int(first_number)

    # 3. Prompt the user to enter the second number.

    second_number = input("Enter the second number: ")

    # 4. Read the input and convert it to an integer.

    convert_second_number = int(second_number)

    # 5. Calculate the sum of the two numbers.

    sum_both_numbers = convert_first_number + convert_second_number

    # 6. Print the total sum with an appropriate message.

    print(f"This is the sum of your given numbers: {sum_both_numbers}")
    
if __name__ == '__main__':
    main()