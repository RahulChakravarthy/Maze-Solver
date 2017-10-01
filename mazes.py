from PIL import Image


class Maze:
    __WIDTH = None
    __HEIGHT = None
    __pixel_array = None
    __node_list = []
    __start_point = None
    __end_point = None
    __old_Image = Image
    __new_Image = Image

    __current_pixel = [None, None]

    def __init__(self, height, width, pixel_array=list, image=Image):
        self.__HEIGHT = height
        self.__WIDTH = width
        self.__pixel_array = pixel_array
        self.__old_Image = image
        self.find_start_end_positions()
        self.create_maze_nodes()

    def find_start_end_positions(self):
        # Assume first entrance pixel is start and second is end
        # Check top line
        for x in range(1, self.__WIDTH - 1):
            if self.__pixel_array[1, x, 2] != 0:
                self.__pixel_array[1, x] = [255, 123, 167]
                if self.__start_point is None:
                    self.__start_point = [1, x]
                elif self.__end_point is None:
                    self.__end_point = [1, x]

        # Check left line
        for y in range(1, self.__HEIGHT - 1):
            if self.__pixel_array[y, 1, 2] != 0:
                self.__pixel_array[y, 1] = [255, 123, 167]
                if self.__start_point is None:
                    self.__start_point = [y, 1]
                elif self.__end_point is None:
                    self.__end_point = [y, 1]
        # Check Right line
        for y in range(1, self.__HEIGHT - 1):
            if self.__pixel_array[y, self.__WIDTH - 2, 2] != 0:
                self.__pixel_array[y, self.__WIDTH - 2] = [255, 123, 167]
                if self.__start_point is None:
                    self.__start_point = [y, self.__WIDTH - 2]
                elif self.__end_point is None:
                    self.__end_point = [y, self.__WIDTH - 2]
        # Check Bottom line
        for x in range(1, self.__WIDTH - 1):
            if self.__pixel_array[self.__HEIGHT - 2, x, 2] != 0:
                self.__pixel_array[self.__HEIGHT - 2, x] = [255, 123, 167]
                if self.__start_point is None:
                    self.__start_point = [self.__HEIGHT - 2, x]
                elif self.__end_point is None:
                    self.__end_point = [self.__HEIGHT - 2, x]
        return

    def create_maze_nodes(self):
        for y in range(1, self.__HEIGHT - 1):
            for x in range(1, self.__WIDTH - 1):
                if self.__check_surrounding_pixels(y, x):
                    self.__node_list.append([y, x])
                    self.__pixel_array[y, x] = 100

    # @Method __check_surrounding_pixels : checks surrounding pixels and returns bool, whether or not current pixel is a node
    def __check_surrounding_pixels(self, y, x):
        # if the pixel is black/wall then ignore it
        if self.__pixel_array[y, x, 2] == 0:
            return False
        else:
            left = self.__pixel_array[y, x - 1, 2] != 0
            right = self.__pixel_array[y, x + 1, 2] != 0
            top = self.__pixel_array[y - 1, x, 2] != 0
            bottom = self.__pixel_array[y + 1, x, 2] != 0
            potential_paths = [left, right, top, bottom]

            return not ((left and right) or (top and bottom)) or (sum(potential_paths) >= 3)

    def breadth_first_search(self):
        self.__current_pixel = self.__current_pixel
        self.__go_to_nearest_node()
        return

    def __go_to_nearest_node(self):

        return

    def depth_first_search(self):
        return

    def write__newImage(self, path=str):
        self.__new_Image = Image.fromarray(self.__pixel_array)
        self.__new_Image.save(path)
