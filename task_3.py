def my_func(*args):
    x = int(input("Enter the 1st number: "))
    y = int(input("Enter the 2nd number: "))
    z = int(input("Enter the 3d number: "))
    number_list = [x, y, z]
    minimum = min(number_list)
    index = number_list.index(minimum)
    number_list.pop(index)
    return sum(number_list)


print(my_func())

