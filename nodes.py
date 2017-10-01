class Node:
    __x_position = None
    __y_position = None
    __dead_end = False

    __parent = None
    __children = list

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

    def add_child(self, node):
        self.__children.append(node)

    def get_children(self):
        return self.__children

    def set_parent(self, node):
        self.__parent = node

    def get_parent(self):
        return self.__parent
