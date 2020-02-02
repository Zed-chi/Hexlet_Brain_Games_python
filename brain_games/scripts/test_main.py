from ..cli import welcome_user
from .test_game1 import game as calc
from .test_game2 import game as even
import prompt


GAMES = [calc, even]

def main():
    correct_answers = 0
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print("Games:")
    for i,v in enumerate(GAMES):
        print(f"{i}. {v.title}")

    while choice or choice > len(GAMES) or choice<len(GAMES):
        choice = prompt.integer(promt="Your choice", empty=False)        
    game = GAMES[choice]

    while correct_answers < 3:
        if game():
            correct_answers += 1
    print(f"Congratulations, {name}!")
    return None