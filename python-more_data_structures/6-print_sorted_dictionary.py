#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dic = dict(sorted(a_dictionary.items()))
    for elem in sorted(sorted_dic.items()):
        print(elem[0] + ":", elem[1])
