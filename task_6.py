def int_func(*args):
    x = input("Enter any message: ")
    y = []
    # выделяю латинские слова в список
    for i in x:
        if ord(i) in range(ord('a'), ord('z')) or i == " ":
            y.append(i)
    z = "".join(y).split()
    # print(z)
    # объединяю латинские слова из созданного списка в строку, добавляя между ними пробел
    for i in tuple(z):
        y = z.index(i)
        z.insert(y + 1, " ")
        z = list(z)
    sentence = "".join(z)
    return sentence.title()


print(int_func())
