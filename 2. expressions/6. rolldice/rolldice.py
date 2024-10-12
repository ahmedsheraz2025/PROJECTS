
# Simulate rolling two dice, and prints results of each roll as well as the total.

NUM_DICE = 5

import random

def main():
    die1 = random.randint(1,NUM_DICE)
    die2 = random.randint(1,NUM_DICE)
    total = die1 + die2
    
    print(f"Dice have {NUM_DICE} sides each")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")
      
    
    
if __name__ == '__main__':
    main()