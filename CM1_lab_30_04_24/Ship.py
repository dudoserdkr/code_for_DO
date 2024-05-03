from Object import Object


class Ship(Object):
    def __init__(self, position, orientation, size) -> None:

        """
        :param orientation: 0, тоді корабель стоїть горизонтально, 1 - вертикально
        :param position: [x: int, y:int]
        :param size: int number; 1 <= size <= 4
        """
        super().__init__(position)
        self.orientation = orientation
        self.size = size
        self.health = [1] * self.size
        Object._ID += 1
        self.id = Object._ID

    def get_dx_dy(self) -> tuple[int, int]:
        dx = dy = 0

        if self.orientation == 0:
            dx = 1
        else:
            dy = 1

        return dx, dy

    def get_body(self):
        dx, dy = self.get_dx_dy()

        x, y = self.position

        for i in range(self.size):
            new_x, new_y = x + i * dx, y + i * dy

            yield new_x, new_y

    def get_area(self):
        dy, dx = self.get_dx_dy()
        ship_body_coords = list(self.get_body())

        start_x, start_y = (ship_body_coords[0][0] - dy,
                            ship_body_coords[0][1] - dx)

        yield start_x, start_y

        end_x, end_y = (ship_body_coords[len(ship_body_coords) - 1][0] + dy,
                        ship_body_coords[len(ship_body_coords) - 1][1] + dx)
        yield end_x, end_y

        ship_body_coords = [(start_x, start_y)] + ship_body_coords + [(end_x, end_y)]

        for x, y in ship_body_coords:
            new_x = x + dx
            new_y = y + dy

            yield new_x, new_y

            new_x = x - dx
            new_y = y - dy

            yield new_x, new_y

    def damage(self, x, y) -> bool:
        dx, dy = self.get_dx_dy()

        ship_x, ship_y = self.position

        health_index = abs(x - ship_x) * dx + abs(y - ship_y) * dy

        self.health[health_index] = 0

        if sum(self.health) == 0:
            return True

        return False


if __name__ == '__main__':
    ship = Ship((1, 1), 1, 4)
