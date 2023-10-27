#!/usr/bin/python3
"""
12-main
"""
pascal_triangle = __import__('12-pascal_triangle').pascal_triangle
/home/puga/Documents/Holberton Git/holbertonschool-higher_level_programming/python-almost_a_circle/python-data_structures
def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
