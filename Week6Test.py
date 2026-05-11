from operator import truediv

# propmting for user input
name = input('Enter your name? ')
print(f'Hello, {name}!')

#Handling integer input
while True:
    try:
        age = int(input('How old are you? '))
        print(f'{name}! You are {age} years old.')
        break
    except ValueError as ve:
        print("")
    except Exception as e:
        print("")