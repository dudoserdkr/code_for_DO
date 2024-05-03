from abc import ABCMeta, abstractmethod


class Object(metaclass=ABCMeta):
    _ID = 0

    @abstractmethod
    def __init__(self, position):
        self.position = position

    @abstractmethod
    def get_body(self):
        pass

    @abstractmethod
    def get_area(self):
        pass


if __name__ == '__main__':
    if [None, None, None]:
        print(1)
