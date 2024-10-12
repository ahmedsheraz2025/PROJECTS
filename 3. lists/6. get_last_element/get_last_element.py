 
def get_last_element(lst):
    print(lst[-1])


def get_lst():
    elem: str = input("Please enter the element or press enter to stop: ")
    lst = []
    while elem != "":
        lst.append(elem)
        elem: str = input("Please enter the element or press enter to stop: ")
    return lst


def main():
    lst = get_lst()
    get_last_element(lst)
    
if __name__ == '__main__':
    main()