class Node:
    __x_position = None
    __y_position = None

    def __init__(self):
        return

    def __init__(self, x, y):
        self.__x_position = x
        self.__y_position = y

    def set_x_position(self, x=int):
        self.__x_position = int

    def set_y_position(self, y=int):
        self.__y_position = y

    def get_x_position(self):
        return self.__x_position

    def get_y_position(self):
        return self.__y_position
