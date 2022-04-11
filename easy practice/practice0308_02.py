def printHello(text):
    print('hello ' + text)


printHello('isaac')
printHello('Dana')
print(printHello('Joe'))


def printHello(name_list):
    print('hello ', end='')
    for i in name_list:
        print(i, end=' ')


printHello(['isaac', 'amy', 'andy'])
