#!/usr/bin/env python3

import collections
import sys

if __name__ == '__main__':
    line_set = list()
    with open('input_files/input_2.txt', 'r') as input:
        while True:
            box_id = list(input.readline())[:-1]
            if box_id == []:
                break
            line_set.append(box_id)
    loop_size = len(line_set)
    for i in range(0, loop_size):
        first_id = line_set[i]
        exit = 0
        for j in range(i + 1, loop_size):
            second_id = line_set[j]
            count = 0
            difference_index = 0
            for index in range(0, len(first_id)):
                if first_id[index] != second_id[index]:
                    if count == 0:
                        count = 1
                        difference_index = index
                    elif count == 1:
                        count = 2
                        break
            if count == 1:
                result = first_id[:difference_index]
                if difference_index is not len(first_id):
                    result = result + first_id[difference_index + 1:]
                    print(''.join(result))
                    sys.exit()
