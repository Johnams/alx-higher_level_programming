#!/usr/bin/python3
# 3-safe-print_division.py

def safe_print_division(a, b):
    """Function that divides 2 integers and prints the result."""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
