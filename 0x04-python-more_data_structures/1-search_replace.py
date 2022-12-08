#!/usr/bin/python3
# 1-search_replace.py

def search_replace(my_list, search, replace):
    """Replace all occurrences of an element by another in a new list."""
    new_list = my_list.copy()
    for n, i in enumerate(new_list):
        if i  == search:
            new_list[n] = replace
        return (new_list)
