from .scripts.games.brain_calc import game as calc
from .scripts.games.brain_even import game as even
from .scripts.games.brain_gcd import game as gcd
from .scripts.games.brain_progression import game as progression
from .scripts.games.brain_prime import game as prime
from .scripts.brain_games import main


GAMES = [calc, even, gcd, progression, prime]


def run():
    main(GAMES=GAMES)


if __name__ == "__main__":
    run()
