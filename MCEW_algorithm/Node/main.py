# -*- coding: utf-8 -*-
import random
import csv
from my_constant import *
from my_logic import *
from my_visualize import *
PATH = 'point_list.csv'


def main():
    point_list = []
    blist = []
    nlist = []
    b_index = [4, 11, 30, 64, 87]
    n1_index = [0, 7, 8]
    n2_index = [22, 71, 28, 66, 54]
    n3_index = [3, 47]
    n_index = [n1_index, n2_index, n3_index]

    # Create a plane
    fig, ax = create_plane()

    # Create and save a list
    # point_list = create_random_points()
    # save_point_list_into_csv_file(point_list, PATH)
    
    # Get list from existing csv file
    point_list = get_point_list(PATH)

    # Create blist, nlist
    blist, nlist = create_and_visualize_blist_nlist(ax, point_list,
                                                    b_index, n_index)
    # Find children
    find_S(ax, blist, nlist)
    
    # MCEW algorithm
    MCEW(ax, nlist)


if __name__ == '__main__':
    main()
