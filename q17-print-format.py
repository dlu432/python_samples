
def print_full_name(a,b):
    print("Hello {c1} {c2}!. You just delved into python.".format(c1=a, c2=b))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
    
