from itertools import combinations_with_replacement

if __name__ == "__main__":

    string, size = input().split(" ")

    print(string)
    print(size)
    comb = list(combinations_with_replacement(sorted(string),int(size)))
    #for i in comb:
    #    print("".join(i))
    print(*comb)
