def sum_of_numbers(*args):
    z = 0
    while True:
        x = input("Enter numbers split by a tab ('you can stop the program by entering 'q'): ").split()
        y = []
        for i in x:
            if i != "q":
                y.append(int(i))
        z = z + sum(y)
        print(f'{sum(y)}({z})')
        if "q" in x:
            break
    return z


print(sum_of_numbers())
