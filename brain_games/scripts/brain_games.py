from brain_games import games as q
from brain_games import engine


def main():
    engine.run(GAMES=[
        q.calc, q.even,
        ]
    )
 