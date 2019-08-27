#!/usr/bin/python

import argparse


def find_max_profit(prices):
    current_buy = prices[0]
    max_profit = 0
    for price in prices:
        current_buy = price if price < current_buy else current_buy
        sell = price - current_buy if current_buy > 0 else 0
        max_profit = sell if sell > max_profit else max_profit
    return max_profit


if __name__ == "__main__":
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description="Find max profit from prices.")
    parser.add_argument(
        "integers", metavar="N", type=int, nargs="+", help="an integer price"
    )
    args = parser.parse_args()

    print(
        "A profit of ${profit} can be made from the stock prices {prices}.".format(
            profit=find_max_profit(args.integers), prices=args.integers
        )
    )

