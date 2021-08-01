import art
import random
import game_data


# function prints A and B and returns value of B
def update_b():
    print(art.logo)
    print("Compare A:{}, a {}, from {}".format(choose_a['name'], choose_a['description'], choose_a['country']))
    print(art.vs)
    choose_b = choose_a
    while choose_b in already_chosen:
        choose_b = random.choice(game_data.data)
        continue
    print("Against B:{}, a {}, from {}".format(choose_b['name'], choose_b['description'], choose_b['country']))
    already_chosen.append(choose_b)
    return choose_b


# initial A
game_over = False
already_chosen = []
correct_count = 0
choose_a = random.choice(game_data.data)

# add choice to already chosen list
already_chosen.append(choose_a)

# game start
while game_over is False:
    game_update = update_b()

    # take valid input
    take_input = "X"
    while take_input != "A" or take_input != 'B':
        take_input = input("Who has more followers? Type 'A' or 'B'").upper()
        if take_input == 'A' or take_input == 'B':
            break
        else:
            print('Enter A or B')

    # checking if users choice is right or wrong
    if take_input == 'A':
        if choose_a['follower_count'] > game_update['follower_count']:
            print("You got {} correct answers".format(correct_count + 1))
        else:
            print("Game over. You got {} correct".format(correct_count))
            game_over = True
            break

    elif take_input == 'B':
        if game_update['follower_count'] > choose_a['follower_count']:
            choose_a = game_update
            print("You got {} correct answers".format(correct_count + 1))
        else:
            print("Game over. You got {} correct".format(correct_count))
            game_over = True
            break

    correct_count += 1
print("Thanks for playing!")
