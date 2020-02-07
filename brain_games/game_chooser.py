import prompt


def game_chooser(games=None):
    if games:
        print("Available Games: ")
        for i, v in enumerate(games):
            print(f"{i}. {v.title}")

        choice = None
        while choice is None or choice > len(games) - 1 or choice < 0:
            choice = prompt.integer(prompt="Your choice: ")
        game = games[choice]
        return game
