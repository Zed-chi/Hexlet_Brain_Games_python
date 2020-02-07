from brain_games.games import calc, even, prime, progression, gcd
from brain_games import engine
from brain_games import game_chooser


def main():
    game = game_chooser(games=[calc, even, prime, progression, gcd])
    engine.run(game=game)
