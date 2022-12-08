#!/usr/bin/python3
# 10-best_score.py

def best_score(a_dictionary):
    result = 0
    if a_dictionary:
        for key in a_dictionary:
            if a_dictionary[key] > result:
                result = a_dictionary[key]
                winner = key
        return winner
