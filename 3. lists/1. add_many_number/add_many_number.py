 
# Write a function that takes a list of numbers and returns the sum of those numbers.


def add_many_number(numbers):
    total_num: int = 0
    for number in numbers:
        total_num += number
    return total_num

def main():
    numbers: list = [1,2,3,4,5,6,7,8,9]
    sum_of_numbers = add_many_number(numbers)
    print(sum_of_numbers)
    
    
if __name__ == '__main__':
    main()