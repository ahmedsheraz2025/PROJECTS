 
# Write a program that doubles each element in a list of numbers.


def main():
    numbers: list[int] = [1,2,3,4]
    
    for i in range(len(numbers)):
        j = numbers[i]
        
        # Modified numbers[i] :
        numbers[i] = j*2
    print(numbers)
    
if __name__ == '__main__':
    main()