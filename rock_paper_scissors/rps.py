#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    outcomes = []
    plays = ["rock", "paper", "scissors"]

    def find_result(times, arr=[]):
        if times == 0:
            outcomes.append(arr)
            return
        for play in plays:
            find_result(times - 1, arr + [play])

    find_result(n, [])
    return outcomes


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print("Usage: rps.py [num_plays]")

