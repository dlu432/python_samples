

if __name__ == '__main__':

    #option 1
    #height, width = map(int,input().split())
    #for i in range(1, height,2):
    #    print(('.|.'*i).center(width,'-'))
    #print("WELCOME".center(width,'-'))
    #for i in range(height-2,-1,-2):
    #    print(('.|.'*i).center(width,'-'))

    #option 2
    height, width = map(int,input().split())
    pattern = [('.|.'*(i*2+1)).center(width,'-') for i in range(height//2)]
    print('\n'.join(pattern + ['WELCOME'.center(width,'-')] + pattern[::-1]))
