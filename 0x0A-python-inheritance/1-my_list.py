#!/usr/bin/python3
# 1-my_list.py
"""Defines an inherited list class Mylist."""

class Mylist(list):
    """Impliments sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a list in a sorted ascendeing order."""
        print(sorted(self))
