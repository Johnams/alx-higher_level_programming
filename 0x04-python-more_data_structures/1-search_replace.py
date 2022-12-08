#!/usr/bin/python3
# 1-search_replace.py

def search_replace(my_list, search, replace):
    return [replace if i == search else i for i in my_list]
