
if __name__ == "__main__":

    # Method 1: Easy to read code to get unique values
    country = set()
    for x in range(int(input())):
        country.add(input())
    print(len(country))

    # Method 2: create list then conver to set to remove duplicate
    #print(len(set([input() for x in range(int(input())) ])))
    # Method 3: only work with set
    #print( len({input() for x in range(int(input()))}) )
