from random import shuffle
my_list = [' ','O',' ']
def shuffle_list(my_list):
    shuffle(my_list)
    return my_list
mixed_list = shuffle_list(my_list)

def player_guess():
    guess = ''

    guess = input("enter your choice 0, 1, 2 : ")
    return int(guess)
guess = player_guess()

def check(my_list,guess):
    if my_list[guess] == 'O':
        print("correct")

    else:
        print('wrong guess')

check(my_list,guess)