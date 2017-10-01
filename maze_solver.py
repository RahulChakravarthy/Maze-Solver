import os
import string
import sys

import numpy
from PIL import Image
from mazes import Maze

'''
Maze Solver
Rahul Chakravarthy
9/4/2017
'''


# @Method check_arg_values : checks and cleans command line input arguments
# @return boolean
def check_arg_values():
    if len(sys.argv) != 3:
        print("Too many or no arguments input error")
        exit(-1)
    else:
        print("Beginning maze solving")
    return


# @Method parse_image_directory : parses a directory and returns file path to all containing images
# @param directory_path string
# @return list containing file paths to all images
def parse_image_directory(directory_path=string):
    contents = os.listdir(directory_path)
    for content in reversed(contents):
        if str(content).find('.png') == -1:
            contents.remove(content)
    return contents


# @Method parse_image : parses each image in images directory
# @param image_path : string path to png file
# @return : return a Maze object
def parse_image(image_path):
    try:
        image = Image.open(image_path).convert('RGB')  # Convert image to greyscale
    except OSError:
        print("Image: " + os.path.basename(image_path) + " is in an incorrect file form... skipping...")
        return -1

    WIDTH, HEIGHT = image.size
    data_pixels = numpy.array(image)
    return Maze(HEIGHT, WIDTH, data_pixels, image)


# @Method breadth_first_search : solves maze using breadth first search algorithm
# @param maze_as_pixel_array : the maze as a 2D array
# @param node_list : list of all nodes of interest in the maze
def breadth_first_search(maze = Maze):
    maze.breadth_first_search()
    return


# @Method depth_first_search : solves maze using depth first search algorithm
# @param maze_as_pixel_array : the maze as a 2D array
# @param node_list : list of all nodes of interest in the maze
def depth_first_search(maze = Maze):
    maze.depth_first_search()
    return


# @Method main : main method for program
def main():
    check_arg_values()
    for image_path in parse_image_directory(sys.argv[1]):
        maze = parse_image(sys.argv[1] + image_path)
        if maze == -1:
            continue
        maze.write__newImage(sys.argv[2] + image_path)
        # breadth_first_search(maze)
        # depth_first_search(maze)


# Main Program Execution
main()
