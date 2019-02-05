
def linsert(list, index, value):
    list.insert(index, value)
    return list

def lprint(list):
    print(list)

def lremove(list, value):
    list.remove(value)
    return list

def lappend(list, value):
    list.append(value)
    return list

def lsort(list):
    return sorted(list)

def lpop(list):
    list.pop()
    return list

def lreverse(list):
    list.reverse()
    return list



if __name__ == "__main__":
    list = []
    #commands = ['insert 0 5', 'insert 1 10', 'insert 0 6', 'print', 'remove 6', 'append 9', 'append 1', 'sort', 'print', 'pop', 'reverse', 'print']
    for _ in range(int(input())):
        args = (input()).split()
        if (args[0] == 'insert'):
            list = linsert(list, int(args[1]), int(args[2]))
        elif (args[0] == 'print'):
            lprint(list)
        elif (args[0] == 'remove'):
            list = lremove(list, int(args[1]))
        elif (args[0] == 'append'):
            list = lappend(list, int(args[1]))
        elif (args[0] == 'sort'):
            list = lsort(list)
        elif (args[0] == 'pop'):
            list = lpop(list)
        elif (args[0] == 'reverse'):
            list = lreverse(list)
        else:
            print('unknown')
