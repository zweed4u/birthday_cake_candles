#!/usr/bin/python3


def birthdayCakeCandles(ar):
    max_height = 0
    for candle_height in ar:
        max_height = max(candle_height, max_height)

    number_of_tallest = 0
    for candle in ar:
        if candle == max_height:
            number_of_tallest += 1
    print(number_of_tallest)
    return number_of_tallest


def birthdayCakeCandlesViaBuiltinMethods(ar):
    max_height = max(ar)
    number_of_tallest = ar.count(max_height)
    print(number_of_tallest)
    return number_of_tallest


birthdayCakeCandles([3, 1, 2, 3])
birthdayCakeCandlesViaBuiltinMethods([3, 1, 2, 3])
