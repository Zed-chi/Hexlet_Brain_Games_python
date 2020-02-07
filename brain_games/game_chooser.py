import prompt


def choose_game(games=None):
    if games is None:
        return
    print("Choose a game: ")
    for game_index, game in enumerate(games):
        print(f"{game_index}. {game.TITLE}")

    choice = None
    while choice is None or choice > len(games) - 1 or choice < 0:
        choice = prompt.integer(prompt="Your choice: ")
    game = games[choice]
    return game
