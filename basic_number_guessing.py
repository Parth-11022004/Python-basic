import random

def easy():
    for i in range(1,11):
        print(f"Chance {i}")
        var = False
        user_num = int(input('Enter number: '))
        if num == user_num:
            print('You win !')
            var = True
            break
        elif (num < user_num):
            print('Too high, guess again')
        else:
            print('Too low, guess again')
    if var is not True:
        print('U lose !')
        print(f"The number was: {num}")
def hard():
    for i in range(1,6):
        print(f"Chance {i}")
        var = False
        user_num = int(input('Enter number: '))
        if num == user_num:
            print('You win !')
            var = True
            break
        elif (num < user_num):
            print('Too high, guess again')
        else:
            print('Too low, guess again')
    if var is not True:
        print('U lose !')
        print(f"The number was: {num}")
     
while True:  
    num = random.randint(1,100)
    difficulty = input('''choose difficulty: easy or hard
                        easy: you get 10 chances to guess the number
                        hard: you get 5 changes to guess the number\n''')
    if difficulty == 'easy':
        easy()
    elif difficulty == 'hard':
        hard()
    else:
        print('Enter a valid difficulty')
        continue
                 
    play_again = input('Do you wanna play again? ')
    if play_again == 'no':
        break
    else:
        continue    
