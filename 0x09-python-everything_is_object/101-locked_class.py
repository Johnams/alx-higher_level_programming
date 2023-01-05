#!/usr/bin/python3
# 101-locked_class.py
"""Defines a locked class."""


class LockedClass:
    """Prevents the user from dynamically creating new insance
    attribute except if the new attribute is called first_name."""


    __slots__ = ["first_name"]
