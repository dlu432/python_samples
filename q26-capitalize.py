def split_and_join(line):
    return " ".join([name.capitalize() for name in line.split(' ')])

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
