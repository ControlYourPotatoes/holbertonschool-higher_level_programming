#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_set = set(my_list)
    unique_list = (list(uniq_set))
    result = sum(unique_list)
    return(result)
