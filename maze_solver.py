import string
import os
import sys
from pprint import pprint
from nodes import Node

from PIL import Image

'''
Maze Solver
Rahul Chakravarthy
9/4/2017
'''


# @Method check_arg_values : checks and cleans command line input arguments
# @return boolean
def check_arg_values():
    if len(sys.argv) != 2:
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
# @return : return a 2D array of RGB values corresponding to
def parse_image(image_path):
    image = Image.open(image_path).convert('L')  # Convert image to greyscale
    WIDTH, HEIGHT = image.size
    data = list(image.getData())
    data = [data[offset:offset + WIDTH] for offset in range(0, WIDTH * HEIGHT, WIDTH)]

    # FOR DEBUGGING
    # for y in range(HEIGHT):
    #     row = (data[y][x] for x in range(WIDTH))
    #     print(' '.join('{:3}'.format(value) for value in row))
    return data


# @Method parse_image : parses each image in images directory
# @param image_path : string path to png file
# @return : return a 2D array of RGB values corresponding to
def create_maze_nodes(maze_as_pixel_array):
    # Iterate through the pixel array and create nodes when parameters have been met
    node_list = []
    node_list.append(Node())
    return node_list


# @Method breadth_first_search : solves maze using breadth first search algorithm
# @param maze_as_pixel_array : the maze as a 2D array
# @param node_list : list of all nodes of interest in the maze
def breadth_first_search(maze_as_pixel_array, node_list):
    return


# @Method depth_first_search : solves maze using depth first search algorithm
# @param maze_as_pixel_array : the maze as a 2D array
# @param node_list : list of all nodes of interest in the maze
def depth_first_search(maze_as_pixel_array, node_list):
    return


# @Method main : main method for program
def main():
    check_arg_values()
    for image_path in parse_image_directory(sys.argv[1]):
        maze_as_pixel_array = parse_image(str(os.path.abspath(image_path)))
        nodes = create_maze_nodes(maze_as_pixel_array)


# Main Program Execution
main()
