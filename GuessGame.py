import random

difficult = 10

def generate_number(difficult):
    return random.randint(1, difficult)

def get_guess_from_user(difficult):
    return int(input(f'Choose you number from 1 to {difficult}: '))

def compare_result(secret_number, user_choice):
    return secret_number == user_choice

def play():
    secret_number = generate_number(difficult)
    user_choice = get_guess_from_user(difficult)
    result = compare_result(secret_number, user_choice)
    return result

print(play())