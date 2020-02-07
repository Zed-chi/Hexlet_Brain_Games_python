from brain_games.games import calc, even, prime, progression, gcd
from brain_games import engine
from brain_games.game_chooser import choose_game


def main():
    game = choose_game(games=[calc, even, prime, progression, gcd])
    engine.run(game=game)
