import numpy
from matplotlib import pyplot as plt
from nodes import Node
from PIL import Image

class Maze:
    __WIDTH = None
    __HEIGHT = None
    __pixel_array = None
    __node_list = []
    __old_Image = Image
    __new_Image = Image

    def __init__(self, height, width, pixel_array=list, image=Image):
        self.__HEIGHT = height
        self.__WIDTH = width
        self.__pixel_array = pixel_array
        self.__old_Image = image
        self.create_maze_nodes()

    def create_maze_nodes(self):
        for y in range(1, self.__HEIGHT-1):
            for x in range(1, self.__WIDTH-1):
                if self.__check_surrounding_pixels(y, x):
                    self.__node_list.append([y, x])
                    self.__pixel_array[y, x] = 100

    # @Method __check_surrounding_pixels : checks surrounding pixels and returns bool, whether or not current pixel is a node
    def __check_surrounding_pixels(self, y, x):
        # if the pixel is black/wall then ignore it
        if self.__pixel_array[y, x] == 0:
            return False
        else:
            left = self.__pixel_array[y, x-1]
            right = self.__pixel_array[y, x+1]
            top = self.__pixel_array[y-1, x]
            bottom = self.__pixel_array[y+1, x]
            potential_paths = [left, right, top, bottom]
            node_counter = 0
            for x in potential_paths:
                if x == 255: # checks how many possible paths can be taken from the current pixel
                    node_counter += 1
            return x>=3

    def write__newImage(self, path=str):
        self.__new_Image = Image.fromarray(self.__pixel_array)
        self.__new_Image.save(path)

