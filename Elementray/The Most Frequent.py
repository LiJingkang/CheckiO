def most_frequent(data):
    """
        determines the most frequently occurring string in the sequence.
    """
    # your code here

    dict_num = {}
    for i in data:
        if i not in dict_num.keys():  # 如果该元素在字典中没有
            dict_num[i] = data.count(i) # key = 在data中出现的次数

    print(dict_num)

    maxNumber = 0
    for i in dict_num: # 便利字典的时候，会默认只用字典的key来遍历
        if dict_num[i] > maxNumber:
            maxNumber = dict_num[i]
            string = i
    return(string)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')

######################
def most_frequent(d):
    max=0
    for i in range(len(d)):
        max=d.count(d[i]) if d.count(d[i])>max else max
        wyn=d[i] if d.count(d[i])==max else wyn
    return wyn

########################
    from collections import Counter
    c = Counter(data)
    return c.most_common()[0][0]
