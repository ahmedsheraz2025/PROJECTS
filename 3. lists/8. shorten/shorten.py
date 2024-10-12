

MAX_LENGTH: int = 4
def shorten(lst):
    while len(lst) > MAX_LENGTH:
        i = lst.pop()
        print(i)

def get_lst():
    lst = []
    elem: str = input("Please enter element or press enter to stop: ")
    while  elem != "":
        lst.append(elem)
        elem: str = input("Please enter element or press enter to stop: ")
    return lst

def main():
    lst = get_lst()
    shorten(lst)
    
if __name__ == '__main__':
    main()