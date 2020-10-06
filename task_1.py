def divide(*args):
    x = int(input("Enter a nominator: "))
    y = int(input("Enter a denominator: "))
    try:
        return round(x / y, 3)
    except ValueError:
        return None


print(divide())
