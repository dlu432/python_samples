

if __name__ == '__main__':

"""
    height, width = map(int,input().split())
    for i in range(1, height,2):
        print(('.|.'*i).center(width,'-'))
    print("WELCOME".center(width,'-'))
    for i in range(height-2,-1,-2):
        print(('.|.'*i).center(width,'-'))
"""

    n, m = map(int,input().split())
    pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
    print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
