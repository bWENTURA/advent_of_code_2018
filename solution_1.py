#!/usr/bin/env python3

import os

if __name__ == '__main__':
    state = 0
    frequency_set = set()
    frequency_twice_reached = False
    while not frequency_twice_reached:
        with open('1_input.txt', 'r') as input:
            while True:
                try:
                    line = input.readline()
                    if line == '':
                        break
                    state = state + int(line)
                    if state not in frequency_set:
                        frequency_set.add(state)
                    else:
                        frequency_twice_reached = True
                        break
                    # print('Change = ' + str(int(line)))
                    # print(state)
                except:
                    print("Exception happened.")
    print("Frequency reached twice is: " + str(state))