from game_data import data
from art import logo,vs
import random
from replit import clear



print(logo)

names = []
def player1():
    pick_player = random.choice(data)
    name = pick_player["name"]
    names.append(name)
    description = pick_player["description"]
    country = pick_player["country"]
    followersA = pick_player['follower_count']
    print(f"Compare A: {name}, a {description} from {country}")
    return followersA


def player2():
    pick_player = random.choice(data)
    name = pick_player["name"]
    names.append(name)
    description = pick_player["description"]
    country = pick_player["country"]
    followersB = pick_player['follower_count']
    print(f"Compare B: {name}, a {description} from {country}")
    return followersB

    
def compare():
    global user_not_right
    global user_points
    user_guess = input("Choose who have more followers A or B >>")
    if user_guess == "a" and playerA > playerB:
        print("Nice guess you right get +1\n")
        user_points += 1
    elif user_guess == "b" and playerB > playerA:
        print("Nice guess you right get +1\n")
        user_points += 1
    else:
        print("sorry you are not right meet in the next game\n")
        user_not_right = True
            

user_points = 0
user_not_right = False
while not user_not_right:
    print(f"""
    --------------------------------
    You have {user_points} for now
    --------------------------------
    \n
    """)
    playerA = player1()
    print(vs)
    playerB = player2()
    compare()