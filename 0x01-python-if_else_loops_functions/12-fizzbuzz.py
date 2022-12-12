#!/usr/bin/python3
def fizzbuzz():
    """Print the numbers from 1 to 100 seperated by a space.

    For multiples of 3, print Fizz instead of the number.
    For multiples of 5, print Buzz instead of the number.
    For multiples of 3 and 5, print FizzBuzz instead of the number.
    """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
