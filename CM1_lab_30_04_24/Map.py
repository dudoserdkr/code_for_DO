from Ship import Ship
from Mine import Mine
from copy import deepcopy


class Map:
    def __init__(self):
        self.map = [[None for _ in range(8)] for _ in range(8)]
        self.visible_map_for_enemy = [["-" for _ in range(8)] for _ in range(8)]
        self.objects_on_map = {}

    # region user_interface
    def hit(self, hit_x, hit_y):
        assert self._check_coordinates_validity(hit_x, hit_y), "Координати введені неправильно"

        hitted_object = self.map[hit_x][hit_y]

        if isinstance(hitted_object, Ship) or isinstance(hitted_object, Mine):
            if type(hitted_object) == Ship:
                self._ship_hitted(hitted_object, hit_x, hit_y)

            else:
                self._mine_hitted(hitted_object, hit_x, hit_y)

        else:
            self.visible_map_for_enemy[hit_x][hit_y] = 'x'
            self.map[hit_x][hit_y] = 'x'

    def add_object(self, object) -> None:
        if type(object) == Ship:
            ship_area = self._check_ship_area(
                object)  # У ship_area повертається або False, якщо місце зайнято, або непорожній двовимірний масив
            if ship_area:
                self.add_ship(object, ship_area)

        elif type(object) == Mine:
            self.add_mine(object)

    def add_ship2

    def print_map(self, player_map):

        alphabet = 'ABCDEFGH'
        print('', 1, 2, 3, 4, 5, 6, 7, 8, sep='\t')

        for i in range(len(player_map) - 1, -1, -1):
            print(alphabet[i], end='\t')
            for j in range(n):
                element = player_map[j][i]
                if type(element) == Ship:
                    element = '🚢'
                elif type(element) == Mine:
                    element = '💣'
                elif element is None:
                    element = ' '
                print(element, end='\t')
            print()

    def __add__(self, other):
        self.add_object(other)
        return self

    # endregion

    # region incapsulated_methods

    @staticmethod
    def _check_coordinates_validity(x, y):
        return 0 <= x <= 7 and 0 <= y <= 7

    def _check_ship_area(self, ship: Ship) -> bool or list[list]:
        area_coordinates = list(ship.get_area())
        free_space_count = 0  # ship.size + 2 <= free_space_count. Якщо нерівність не виконується - ми не можемо добавити корабель.

        map_copy = deepcopy(self.map)

        for x, y in area_coordinates:
            if self._check_coordinates_validity(x, y):
                if self.map[x][y] is None:
                    map_copy[x][y] = ' '
                    free_space_count += 1
                elif type(self.map[x][y]) == Mine:
                    free_space_count += 1
                else:
                    return False

        if ship.size + 2 <= free_space_count:
            return map_copy

        return False

    def add_ship(self, ship: Ship, map_copy: list[list]) -> None:

        for x, y in list(ship.get_body()):
            if self.map[x][y] is None:
                map_copy[x][y] = ship
            else:
                return
        self.objects_on_map[ship.id] = ship
        self.map = map_copy

    def add_mine(self, mine: Mine) -> None:
        x, y = mine.position

        if self._check_coordinates_validity(x, y):
            if self.map[x][y] is None or isinstance(self.map[x][y], str):
                self.map[x][y] = mine

    def _ship_hitted(self, hitted_ship: Ship, hit_x, hit_y):

        is_ship_totally_destroyed = hitted_ship.damage(hit_x, hit_y)

        if is_ship_totally_destroyed:
            ship_body_coordinates = list(hitted_ship.get_body())

            for x, y in ship_body_coordinates:
                self.visible_map_for_enemy[x][y] = '💥'
                self.map[x][y] = '💥'

            ship_area_coordinates = list(hitted_ship.get_area())

            for x, y in ship_area_coordinates:
                if self._check_coordinates_validity(x, y):
                    self.visible_map_for_enemy[x][y] = 'x'
                    self.map[x][y] = 'x'

            del self.objects_on_map[hitted_ship.id]
            print("Ви знищили корабель")

        else:
            self.map[hit_x][hit_y] = '⛝'
            self.visible_map_for_enemy[hit_x][hit_y] = '⛝'
            print('Ваш постріл влучив у частину корабля')

    def _mine_hitted(self, hitted_mine, hit_x, hit_y):
        mine_hitted_area = hitted_mine.damage()
        self.map[hit_x][hit_y] = '✡'
        self.visible_map_for_enemy[hit_x][hit_y] = '✡'

        for x, y in mine_hitted_area:
            if self._check_coordinates_validity(x, y):
                self.hit(x, y)

    # endregion


if __name__ == '__main__':
    car = Map()

    s1 = Ship((1, 1), 0, 3)
    s2 = Ship((6, 6), 1, 2)
    s3 = Ship((2, 2), 1, 3)

    m1 = Mine((1, 3))

    print(s1.id)
    print(s2.id)
    print(s3.id)
    print(m1.id)

    car += m1
    car += s3
    car += s2
    car += s1

    MAP = car.map
    n = len(MAP)

    car.print_map(car.visible_map_for_enemy)

    car.hit(1, 3)
    car.hit(6, 6)
    car.hit(6, 7)

    car.print_map(car.visible_map_for_enemy)

    print(car.objects_on_map)
