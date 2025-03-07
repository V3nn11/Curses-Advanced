"""x = "faina 20, lapte 20, ou 5, unt 5, zahar 5, sare 11"

def show_clatita():
    global x
    ingredients = x.split(", ")
    for ingredient in ingredients:
        print(ingredient)

show_clatita()"""

"""x = "faina 20, lapte 20, ou 5, unt 5, zahar 5, sare 11"

def show_clatita():
    global x
    ingredients = x.split(", ")
    for ingredient in ingredients:
        name = ingredient.split(" ")[0]
        print(name.capitalize())

show_clatita()"""

"""x = "faina 20, lapte 20, ou 5, unt 5, zahar 5, sare 11"

def show_clatita(num_pancakes):
    global x
    ingredients = x.split(", ")
    for ingredient in ingredients:
        name, weight = ingredient.split(" ")
        total_weight = int(weight) * num_pancakes
        print(f"{name.capitalize()} {total_weight}")

# apeleaza functia cu 5 clatite
show_clatita(5)"""


"""x = "faina 20, lapte 20, ou 5, unt 5, zahar 5, sare 11"

def show_clatita(num_pancakes, exclude=""):
    global x
    ingredients = x.split(", ")
    exclude_list = [item.strip().lower() for item in exclude.split(",")]
    
    for ingredient in ingredients:
        name, weight = ingredient.split(" ")
        if name.lower() not in exclude_list:
            total_weight = int(weight) * num_pancakes
            print(f"{name.capitalize()} {total_weight}")

# Example call to the function with 5 pancakes and excluding 'Ou' and 'Sare'
show_clatita(5, exclude='Ou, Sare')"""


"""x = "faina 20, lapte 20, ou 5, unt 5, zahar 5, sare 11"

def show_clatita(num_pancakes, exclude="", need_add=""):
    global x
    ingredients = x.split(", ")
    exclude_list = [item.strip().lower() for item in exclude.split(",")]
    additional_ingredients = need_add.split(", ")

    # ingredientele main
    for ingredient in ingredients:
        name, weight = ingredient.split(" ")
        if name.lower() not in exclude_list:
            total_weight = int(weight) * num_pancakes
            print(f"{name.capitalize()} {total_weight}")

    # ingredientele aditionale
    for ingredient in additional_ingredients:
        if ingredient:
            name, weight = ingredient.split(" ")
            total_weight = int(weight) * num_pancakes
            print(f"{name.capitalize()} {total_weight}")

# apelam le function
show_clatita(5, exclude='Ou, Sare', need_add='Miere 5, Ciocolată 10')"""

import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    player1_score = 0
    player2_score = 0

    for _ in range(3):
        player1_score += roll_dice()
        player2_score += roll_dice()

    print(f"Player 1 score: {player1_score}")
    print(f"Player 2 score: {player2_score}")

    if player1_score > player2_score:
        print("Player 1 wins!")
    elif player2_score > player1_score:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

# Simulate a round of the game
play_game()