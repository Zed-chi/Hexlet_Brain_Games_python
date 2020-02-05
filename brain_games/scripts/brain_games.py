from brain_games.games import calc, even, prime, progression, gcd
from brain_games import engine


def main():
    engine.run(games=[calc, even, prime, progression, gcd])
