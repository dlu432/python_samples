def swap_case(s):
    new_string = ""
    #print(string.swapcase())  butilt in function
    for i in range(len(string)):
        #print(string[i])
        if (string[i].islower()):
            new_string += string[i].upper()
        else:
            new_string += string[i].lower()
    #print(new_string)
    return new_string

if __name__ == '__main__':
    string = "ABCDefgHIJKlmnop 123 QRS tuv WX yz"
    print(swap_case(string))
