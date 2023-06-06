#!/usr/bin/python3
for numbers in range(0, 100):
    if numbers == 99:
        print(numbers)
    else:
        print("{:0>2d}".format(numbers), end=", ")
