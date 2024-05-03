from Map import Map


def user2coord(coord: str):
    x, y = coord

    alphabet = 'ABCDEFGH'

    return alphabet.index(x.upper()), int(y) - 1


game_map = Map()

while True:
    pass
