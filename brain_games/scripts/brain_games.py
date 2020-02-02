from ..cli import welcome_user
from .games.brain_calc import game as calc
from .games.brain_even import game as even
from .games.brain_gcd import game as gcd
from .games.brain_progression import game as progression
from .games.brain_prime import game as prime
import prompt


GAMES = [calc, even, gcd, progression, prime]
ANSWERS_TO_WIN = 3


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print("\n")
    print("Games: ")
    for i, v in enumerate(GAMES):
        print(f"{i}. {v['title']}")

    choice = None
    while choice is None or choice > len(GAMES) - 1 or choice < 0:
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
