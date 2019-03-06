

if __name__ == "__main__":
    n, m = input().split()

    number = list(map(int, input().split()))

    a_set = set(map(int, input().split()))
    b_set = set(map(int, input().split()))

    print(sum((i in a_set) - (i in b_set) for i in number))
