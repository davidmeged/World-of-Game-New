import random
import time

difficult = 2

def generate_sequence(difficulty):
    number = difficulty
    number_sequence = []
    while number > 0:
        number_sequence.append(random.randint(0, 101))
        number -= 1
    print(number_sequence, end='')
    time.sleep(0.7)
    print('\r', end='')
    return number_sequence

def get_list_from_user(difficulty):
    number = difficulty
    number_sequence = []
    while number > 0:
        number_sequence.append(int(input('Choose number from 0 to 101: ')))
        number -= 1
    return number_sequence

def is_list_equal(random_list, user_list):
    return sorted(random_list) == sorted(user_list)

def play():
    random_sequence = generate_sequence(difficult)
    user_sequence = get_list_from_user(difficult)
    return is_list_equal(random_sequence, user_sequence)

#print(generate_sequence(difficult))
#print((get_list_from_user(difficult)))
#print((is_list_equal([1, 2, 17], [2, 17, 1])))
print(play())