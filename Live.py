
#name = input('Enter you name: ')

def welcome(name):
    print(f'Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.')


def load_game():
    while True:
        user_game_choice = int(input('\nPlease choose a game to play:\n\t1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n\t'
        '2. Guess Game - guess a number and see if you chose like the computer\n\t'
        '3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n'))
        if 1 <= user_game_choice <= 3:
            break
    while True:
        user_choice = int(input('Please choose game difficulty from 1 to 5: '))
        if 1 <= user_choice <= 5:
            break

