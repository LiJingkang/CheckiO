def checkio(array):

    if len(array) == 0:
        return 0

    evenIndexesSum = 0

    # 取出数组中偶数位的数的和
    for i in range(len(array)):  # range函数的用法。  len()取长度
        if  not i % 2:
            evenIndexesSum += array[i]

    print(evenIndexesSum)
    return evenIndexesSum * array[len(array) - 1]


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
