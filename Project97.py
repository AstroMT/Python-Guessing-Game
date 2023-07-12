# Guessing Game
import random

def game():
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    number = random.choice(number_list)
    chances = 0
    while chances < 5:
        guess = int(input("Guess a number from 1 to 9: "))
        if number == guess:
            print("You are correct!")
            break
        elif number > guess:
            print("Your number was too low!")
        else:
            print("Your number was too high!")
        chances +=1
        if chances == 5:
            print(f'You lose! You used all 5 turns! The number was {number}' )
            break

game()