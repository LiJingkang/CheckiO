##Commit Testdef checkio(text):

    #replace this for solution
    import  string

    # lower函数,小写化
    text = text.lower()
    # max 函数,根据text.count 关键字来返回最大的数
    # 如果相同根据ascii_lowercase 来选择
    return max(string.ascii_lowercase,key=text.count)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")

#######################
from collections import Counter
def checkio(text):
    # count 字典
    count = Counter([x for x in text.lower() if x.isalpha()]) #count字典
    print(count)
    m = max(count.values())
    print(m)
    return sorted([x for (x, y) in count.items() if y == m])[0]
######################
def checkio(text):
    x=len(text)
    text=text.lower()
    pom="abcdefghijklmnopqrstuvwxyz"
    y=len(pom)
    max=0
    pom2=""
    ile=0
    for i in range(y):
        ile=text.count(pom[i])
        if (ile>max):
            max=ile
            pom2=pom[i]
    return pom2
########################
from collections import defaultdict as defaultdict
from collections import OrderedDict as OrderedDict
from operator import itemgetter as itemgetter

def checkio(text):

    # convert to lower case
    text = text.lower()
    text = ''.join(filter(str.isalpha, text))

    # make a structure for unique letter with counts
    holder = defaultdict(int)
    for letter in text: holder[letter] += 1

    # sort letters by alphabet
    holder = OrderedDict(sorted(holder.items()))

    most_frequent_letter = [k for k, v in holder.items() if v == max(holder.values())][0]

    return most_frequent_letter