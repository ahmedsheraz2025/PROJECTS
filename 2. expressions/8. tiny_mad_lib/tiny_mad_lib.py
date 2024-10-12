
# Write a program which prompts the user for an adjective, then a noun, then a verb,
# and then prints a fun sentence with those words!


SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my"

def main():
    adjective: str = input("Please type an abjective and press enter: ")
    noun: str = input("Please type a noun and press enter: ")
    verb: str = input("Please type a very and press enter: ")
    
    print(f"{SENTENCE_START} {adjective} {noun} {verb}!")

if __name__ == '__main__':
    main()