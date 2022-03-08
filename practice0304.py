def guessnum():
    answer = 3
    guess = 0

    while guess != answer:
        guess = int(input('please make guess during 1~6.: '))
        if guess > answer:
            print('bigger than answer')
        elif guess < answer:
            print('smaller than answer')
        else:
            print('bingo')


def printof10():
    i = 1
    while i < 11:
        print(i)
        i += 1  # i = i + 1


def sumof100():
    i = 0
    num_sum = 0
    # while True:
    #     if i > 100:
    #         break
    while i <= 100:
        num_sum = num_sum + i
        i = i + 1
        # print('num_sum: {}, i: {}'.format(num_sum, i))
    print('1+2+......+100 = {}'.format(num_sum))


sumof100()


def sumof50():
    i = 0
    num_sum = 0
    while i <= 100:
        if i % 2 == 1:
            i = i + 1
            continue
        num_sum = num_sum + i
        # print('num_sum: {}, i: {}'.format(num_sum, i))
        i = i + 1

    print('2+4+6......+100 = {}'.format(num_sum))


sumof50()


# for loop practices
def printhelist():
    for i in range(10):
        print(i, end=' ')
    print('\n')
    for i in range(5, 10):
        print(i, end=' ')
    print('\n')
    for i in range(1, 10, 2):
        print(i, end=' ')
    print('\n')
    my_list = [10, -20, 15]


    print('my_list')
    for i in my_list:
        print(i, end=' ')
    print('\n')
    for i in range(len(my_list)):
        print('list index', i, ' : ', my_list[i])
    for index01, i in enumerate(my_list):
        print(index01, i)


printhelist()


def printhestar():
    str = "*"
    space = " "
    s = int(input('輸入高度'))
    i = 1
    while i <= s:
        print(space * (s - i), str * (i * 2 - 1))
        i = i + 1


# printhestar()

def dontprint26():
    for x in range(6):
        if (x == 2 or x == 6):
            continue
        print(x, end=' ')
    print("\n")
