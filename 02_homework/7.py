from random import randint

random_computer_num = randint(0, 100)
user_num = int(input('num: '))

while user_num != random_computer_num:
    if user_num > random_computer_num:
        print('The guessed number is less!')
    else:
        print('The guessed number is bigger!')
    user_num = int(input('num: '))
print('You guessed the number!')
print('The guessed number is ' + str(random_computer_num))
