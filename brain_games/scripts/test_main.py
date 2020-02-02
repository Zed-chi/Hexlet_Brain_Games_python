from ..cli import welcome_user
from .games.test_game1 import game as calc
from .games.test_game2 import game as even
import prompt


GAMES = [calc, even]
ANSWERS_TO_WIN = 3

def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print("\n")
    print("Games: ")
    for i,v in enumerate(GAMES):        
        print(f"{i}. {v['title']}")
    
    choice = None
    while choice == None or choice > len(GAMES)-1 or choice<0:
        choice = prompt.integer(prompt="Your choice: ")        
    game = GAMES[choice]

    print(game["description"])
    correct_answers = 0
    
    while correct_answers < ANSWERS_TO_WIN:
        if game["game"]():
            correct_answers += 1
    print(f"Congratulations, {name}!")
    return None


if __name__ == "__main__":
    main()
