
if __name__ == '__main__':
    s = input()
    # option 1
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))

    # option 2
    for cmd in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
        print(any(eval("c." + cmd + "()") for c in s))
