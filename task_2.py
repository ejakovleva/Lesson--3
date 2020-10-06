def user_data(**kwargs):
    name = input("Enter your name: ")
    last_name = input("Enter your last name: ")
    birth_year = input("Enter your birth year: ")
    city = input("Enter the city of your residence: ")
    email = input("Enter your email address: ")
    phone_number = input("Enter your phone number: ")
    return f'{name} {last_name} {birth_year} {city} {email} {phone_number}'


print(user_data())
