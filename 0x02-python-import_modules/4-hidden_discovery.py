#!/usr/bin/python3
# 4-hidden_discovery.py

import hidden_4
if __name__ == "__main__":
    for i in dir(hidden_4):
        if i[0:2] != "__":
            print("{:s}".format(i))