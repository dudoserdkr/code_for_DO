from Object import Object


class Mine(Object):

    def __init__(self, position: tuple[int, int]):
        super().__init__(position)
        self.healt = 1
        Object._ID += 1
        self.id = Object._ID

    def get_body(self):
        return self.position

    def get_area(self):
        deltas = ((i, j) for i in (-1, 0, 1) for j in (-1, 0, 1)
                  if i != 0 or j != 0)

        x, y = self.position

        for dx, dy in deltas:
            new_x = x + dx
            new_y = y + dy

            yield new_x, new_y

    def damage(self):
        return self.get_area()


if __name__ == '__main__':
    mine = Mine((1, 1))
    for i in mine.get_area():
        print(i)
