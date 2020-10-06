def pow_negative(x, y):
    if x <= 0 or (type(x) != int and type(x) != float):
        print("Enter any positive real number!")
    elif y >= 0 or type(y) != int:
        print("Enter any negative integer!")
    else:
        h = 1
        for i in range(-y - 1):
            h = h * x
        print(1 / (h * x))


pow_negative(4, -2)
