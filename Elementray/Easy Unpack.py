def easy_unpack(elements):
    """
        returns a tuple with 3 elements - first, third and second to the last
    """
    # your code here

    # 取出对应元素 tuple 中的元素。 -2 是从末尾取
    # tuple 是一个不可变的list。 没有方法，可以使用in来遍历
    t = (elements[0], elements[2], elements[-2])

    return t


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
    print('Done! Go Check!')

##################
def easy_unpack(elements):
    return tuple([list(elements)[0], list(elements)[2], list(elements)[-2]])

