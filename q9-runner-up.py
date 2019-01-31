if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    # set removes duplicates from arr
    newlist = sorted(set(arr))
    print(newlist[-2])
