# Number Guessing Game

logo = ''''


   _____                      _______ _            _   _                 _               
  / ____|                    |__   __| |          | \ | |               | |              
 | |  __ _   _  ___ ___ ___     | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ / __/ __|    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ | '__|
 | |__| | |_| |  __\__ \__ \    | |  | | | |  __/ | |\  | |_| | | | | | | |_) |  __| |   
  \_____|\__,_|\___|___|___/    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                         
                                                                                         
 '''

import random

print(logo)

# choose random number and start game
random_number = random.choice(range(1, 101))
print("Welcome to the Number Guessing Game!!!")
print("I am thinking of a number between 1 to 100...")
print("Can you guess it")
print("Psst the number is ", random_number)

# choose mode
mode = "something"
while mode != "easy" or mode != "hard":
    mode = input("Type 'easy' for easy mode and 'hard' for hard mode")
    if mode == "easy":
        hint = 10
        break
    elif mode == "hard":
        hint = 5
        break
    else:
        print("Enter easy or hard")
        continue

# hint and checking if number is found or not if it is found loop
found = False
while found is not True or hint != 0:
    def hint_is(x):
        if random_number < x < 101:
            print("Too high")
            return "Lives remaining:{}".format(hint - 1)
        elif random_number > x > 0:
            print("Too low")
            return "Lives remaining:{}".format(hint - 1)
        elif x == random_number:
            found = True
            return found


    x = int(input("Take a guess"))
    game = hint_is(x)
    hint = hint - 1
    if game == True:
        print("Correct.Your number was ", random_number)
        break
    else:
        print(game)

    if hint == 0:
        print("Game Over.Number was ", random_number)
        break
