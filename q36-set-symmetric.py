
if __name__ == "__main__":

    #m = input()
    #m_list = set(map(int, input().split()))
    #n = input()
    #n_list = set(map(int, input().split()))
    # list comprehension way of getting 4 lines of input and only keep 2 lines
    m_list, n_list = [set(map(int, input().split())) for _ in range(4)][1::2]
    m_list_diff = m_list.difference(n_list)
    n_list_diff = n_list.difference(m_list)
    mn_diff = m_list_diff.union(n_list_diff)
    for x in (sorted(mn_diff)):
        print(x)
