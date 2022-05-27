import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, options):
    while True:
        response = input(prompt)
        for option in options:
            if option == response:
                return response


def defining_enemy():
    characters_options = ["WITCH", "DRAGON", "BEAR"]
    return random.choice(characters_options)


def intro(current_enemy):
    print_pause("Welcome to 'Aurora Village'")
    print_pause(f"Rumor has it that a {current_enemy} is terrifying "
                "the community")
    print_pause("Your mission is to save the village from the enemy")
    print_pause("You are their last hope!")


def field(has_weapon, defeats, last_place, current_enemy):
    print_pause("---\n"
                "You find yourself at the village's field")
    print_pause("At your right there is a cave\n"
                "At your left there is a forest\n"
                "In front of you there is a house")
    print_pause("Where do you want to go now?")
    print_pause("1. cave\n"
                "2. house\n"
                "3. forest")
    options = ["1", "2", "3"]
    place = valid_input("(Please select 1, 2 or 3)\n", options)
    if place == "1":
        return cave(has_weapon, defeats, last_place, current_enemy)
    elif place == "2":
        house(defeats, last_place)
    elif place == "3":
        forest(has_weapon, last_place, current_enemy)
    field(has_weapon, defeats, last_place, current_enemy)


def cave(has_weapon, defeats, last_place, current_enemy):
    print_pause("You enter in the cave and suddely realize that in "
                f"front of you is the {current_enemy}")
    return fight_or_run(has_weapon, defeats, last_place, current_enemy)


def fight_or_run(has_weapon, defeats, last_place, current_enemy):
    print_pause("What will you want to do?")
    print_pause("1. fight\n"
                "2. run back to field")
    options = ["1", "2"]
    choice = valid_input("(Please select 1 or 2)\n", options)
    if choice == "1":
        return fight(has_weapon, defeats, last_place, current_enemy)
    field(has_weapon, defeats, last_place, current_enemy)


def fight(has_weapon, defeats, last_place, current_enemy):
    last_place[0] = "cave"
    print_pause("You decided to fight")
    print_pause(f"What move do you want to try against the {current_enemy}?")
    print_pause(defining_moves(current_enemy))
    options = ["1", "2", "3"]
    choose_move = valid_input("(Please select 1, 2 or 3)\n", options)
    print_pause("You chose your move")
    print_pause("You try your best...")
    if choose_move == "1":
        if has_weapon[0] == "no":
            return lose_fight(has_weapon, defeats, last_place, current_enemy)
        else:
            print_pause("Congratulations. You won!")
            return play_again()
    else:
        return lose_fight(has_weapon, defeats, last_place, current_enemy)


def defining_moves(current_enemy):
    if current_enemy == "DRAGON":
        return("1. To strike their chest\n"
               "2. To strike their belly\n"
               "3. To strike their head")
    elif current_enemy == "BEAR":
        return("1. To shot at their head\n"
               "2. To shot at their chest\n"
               "3. To shot at their belly")
    elif current_enemy == "WITCH":
        return("1. The 'forabolsonaro spell'\n"
               "2. The 'death spell'\n"
               "3. The 'shield spell'")


def lose_fight(has_weapon, defeats, last_place, current_enemy):
    print_pause("Oh no, you lose the fight :/")
    print_pause("You realize that maybe you chose the wrong move "
                "or you don't have the right weapon yet to fight")
    defeats.append("defeat")
    health_score = recalculate_health_score(defeats)
    print_pause(f"Now your health score is {health_score}/3")
    if health_score == 0:
        print_pause("GAME OVER")
        return play_again()
    fight_or_run(has_weapon, defeats, last_place, current_enemy)


def play_again():
    print_pause("Will you want to play again?")
    print_pause("1. Play again\n"
                "2. End game")
    options = ["1", "2"]
    response = valid_input("(Please enter 1 or 2)\n", options)
    if response == "1":
        print_pause("Loading game...")
        return play_adventure_game()
    elif response == "2":
        print_pause("okay")
        return print_pause("goodbye!")


def recalculate_health_score(defeats):
    health_score = 3
    for defeat in defeats:
        health_score -= 1
    return health_score


def house(defeats, last_place):
    print_pause("The house is empty")
    print_pause("In the living room's center, there is a chest")
    print_pause("You realize that this chest is different from the others "
                "you already saw")
    print_pause("It seems to be the Divine Chest: the one that contains "
                "the Magic Heal Potion, known for curing the ones that "
                "take it")
    health_score = recalculate_health_score(defeats)
    if health_score == 3:
        print_pause("You try to open the chest, but for some reason "
                    "it is too hard")
        print_pause("You decide to do it later")
    else:
        open_chest(defeats, last_place)
    print_pause("It seems that there is nothing more to do here, "
                "so you come back to the field")


def open_chest(defeats, last_place):
    print_pause("Do you want to open the chest? y/n")
    options = ["y", "n"]
    choice = valid_input("(Type 'y' for 'yes' or 'n' for 'no')\n",
                         options)
    if choice == "y":
        if "house" in last_place:
            print_pause("Ops!")
            print_pause("It seems you can't take the potion twice "
                        "in a row =/")
        else:
            print_pause("You open the chest and hope it doesn't be a trap...")
            print_pause("Yeah!\nYou find the Heal Position =D")
            defeats.pop()
            health_score = recalculate_health_score(defeats)
            print_pause(f"Now your health score is {health_score}/3")
            last_place[0] = "house"
    else:
        print_pause("You decided to not open the chest")


def forest(has_weapon, last_place, current_enemy):
    last_place[0] = "forest"
    weapon = defining_weapon(current_enemy)
    print_pause("Now you are in the forest.")
    if has_weapon[0] == "no":
        print_pause("It is dark. You start getting a bad feeling.")
        print_pause("You are almost running back to the field when you "
                    "see something interesting")
        print_pause("You get closer and closer to the odd object which "
                    "gets your attention...")
        print_pause("OMG! o.O")
        print_pause(f"You find the {weapon}!!!")
        print_pause(f"As soon you see the {weapon} you get it.")
        print_pause("It will be helpful when fighting against the "
                    f"{current_enemy}!")
        has_weapon[0] = "yes"
    print_pause(f"Now you already have the {weapon} "
                "there is nothing to do here anymore. "
                "So you come back to the field")


def defining_weapon(current_enemy):
    if current_enemy == "DRAGON":
        return "sword"
    elif current_enemy == "WITCH":
        return "wand"
    elif current_enemy == "BEAR":
        return "fire gun"


def play_adventure_game():
    has_weapon = ["no"]
    defeats = []
    last_place = ["field"]
    current_enemy = defining_enemy()
    intro(current_enemy)
    field(has_weapon, defeats, last_place, current_enemy)


play_adventure_game()
