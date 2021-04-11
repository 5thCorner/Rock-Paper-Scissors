import random


def game():
    global rating
    input_option = input()
    if input_option == '!exit':
        print('Bye!')
        quit()
    elif input_option == '!rating':
        print(f'Your rating: {rating}')
        game()
    elif input_option not in lst_option:
        print('Invalid input')
        game()
    else:
        check_winner(input_option)
        game()


def check_winner(player_option):
    global rating
    comp_rand_opt = random.choice(lst_option)
    if comp_rand_opt == player_option:
        print(f'There is a draw ({player_option})')
        rating = str(int(rating) + 50)
    elif comp_rand_opt not in dct_win_option[player_option]:
        print(f'Sorry, but the computer chose {comp_rand_opt}')
    else:
        print(f'Well done. The computer chose {comp_rand_opt} and failed')
        rating = str(int(rating) + 100)


def read_file():
    with open('rating.txt', 'r', encoding='utf-8') as f:
        lst_rating = f.readlines()
        for i in range(len(lst_rating)):
            lst_rating[i] = lst_rating[i].split()
        return lst_rating


def check_rating(str_name, lst):
    for i in range(len(lst)):
        if str_name == lst[i][0]:
            return lst[i][1]
        else:
            continue
    return '0'


dct_win_option = {
    'water': ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
    'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
}
name = input('Enter your name: ')
print(f'Hello, {name}')
lst_option = input().split(',')
if lst_option == ['']:
    lst_option = ['rock', 'paper', 'scissors']
print("Okay, let's start")
rating = check_rating(name, read_file())
game()
