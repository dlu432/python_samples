def count_substring(string, sub_string):
    #option 1
    #counter = 0
    #for i in range(0, len(string)-len(sub_string)+1):
    #    if sub_string == string[i:len(sub_string)+i]:
    #        counter += 1

    #option 2
    counter = sum([1 for i in range(len(string)-len(sub_string)+1) if sub_string ==
    string[i:len(sub_string)+i]])
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
