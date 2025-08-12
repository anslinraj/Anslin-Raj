# ___________________ Hand Cricket using exception handling _________________'''
import random

print('--Great cricket tournament begins--')
play_user = 0
play_comp = 0
user_choice = input('Enter odd/even: ').lower()
decide = ['BAT','BALL']
if user_choice == 'even':
    comp_choice = 'odd'
else:
    comp_choice = 'even'
print(f'Computer gets {comp_choice}')
print('--Play for toss--')
user = int(input('Enter a num(1-6): '))
comp = random.randint(1,6)
print(f'Computer plays {comp}')
a = user + comp
play = ''
play1 = ''
if (a % 2 == 0 and user_choice == 'even') or (a % 2 != 0 and user_choice == 'odd'):
    print('User won toss!!!')
    play = input('Bat or Ball: ').upper()
else:
    print('Computer won toss!!!')
    play1 = random.choice(decide)
    print(f'Computer chooses to {play1}')

if play == 'BAT' or play1 == 'BALL':
    play_user = 1
else:
    play_comp = 1

score_user = 0
score_comp = 0

if play_user == 1:
    print('--User is batting--')
    while True:
        try:
            user1 = int(input('Play (1-6): '))
            if user1 < 0 or user1 > 7:
                print('Enter valid number between 1 and 6')
                continue
        except ValueError:
            print('Invalid input. Try again.')
            continue
        comp1 = random.randint(1,6)
        print(f'Computer puts {comp1}')
        if user1 == comp1:
            print(f'User OUT!! with score {score_user}')
            break
        else:
            score_user += user1
        
    print('--Computer is batting--')
    while score_comp <= score_user:
        try:
            user2 = int(input('Play (1-6): '))
            if user2 < 0 or user2 > 7:
                print('Enter valid number between 1 and 6')
                continue
        except ValueError:
            print('Invalid input. Try again.')
            continue
        comp2 = random.randint(1,6)
        print(f'Computer plays {comp2}')

        if user2 == comp2:
            print(f'Computer OUT!! with score {score_comp}')
            break
        else:
            score_comp += comp2

else:
    print('--Computer is batting--')
    while True:
        try:
            user2 = int(input('Play (1-6): '))
            if user2 < 0 or user2 > 7:
                print('Enter valid number between 1 and 6')
                continue
        except ValueError:
            print('Invalid input. Try again.')
            continue
        comp2 = random.randint(1,6)
        print(f'Computer plays {comp2}')

        if user2 == comp2:
            print(f'Computer OUT!! with score {score_comp}')
            break
        else:
            score_comp += comp2

    print('--User is batting--')
    while score_user <= score_comp:
        try:
            user1 = int(input('Play (1-6): '))
            if user1 < 0 or user1 > 7:
                print('Enter valid number between 1 and 6')
                continue
        except ValueError:
            print('Invalid input. Try again.')
            continue
        comp1 = random.randint(1,6)
        print(f'Computer puts {comp1}')
        if user1 == comp1:
            print(f'User OUT!! with score {score_user}')
            break
        else:
            score_user += user1  

print('--MATCH RESUL--')
print(f'User score: {score_user}')
print(f'Computer score: {score_comp}')

if score_user > score_comp:
    print('USER WINS')
elif score_user < score_comp:
    print('COMPUTER WINS')
else:
    print('MATCH DRAW')