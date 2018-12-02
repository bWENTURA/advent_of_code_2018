#!/usr/bin/env python3

import collections

if __name__ == '__main__':
    two = 0
    three = 0
    with open('input_files/input_2.txt', 'r') as input:
        while True:
            box_id = list(input.readline())[:-1]
            if box_id == []:
                break
            counted_set = collections.Counter(box_id)
            counted_values = counted_set.values()
            if 2 in counted_values:
                two += 1
            if 3 in counted_values:
                three += 1
        print(two * three)
