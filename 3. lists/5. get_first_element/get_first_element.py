 
 
 
def get_first_element(lst):
    print(lst[0])
 
def get_lst():
    elem: str = input("Please enter element of the list or press enter to stop: ")
    lst = []
    while elem != "":
        lst.append(elem)
        elem: str = input("Please enter element of the list or press enter to stop: ")
    return lst

def main():
    lst = get_lst()
    get_first_element(lst)
    
if __name__ == '__main__':
    main()