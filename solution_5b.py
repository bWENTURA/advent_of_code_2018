#!/usr/bin/env python3

import re
import string

def calculate_len(example):
    line = example
    new_line = []
    index = 0
    while index in range(0, len(line) - 1):
        if not ((line[index].isupper() and line[index + 1] == line[index].lower())
            or 
            (line[index].islower() and line[index + 1] == line[index].upper())):
            if len(new_line):
                last_letter = new_line[len(new_line) - 1]
                if not ((last_letter.isupper() and line[index] == last_letter.lower())
                    or
                    (last_letter.islower() and line[index] == last_letter.upper())):
                    new_line.append(line[index])
                else:
                    new_line.pop()
            else:
                new_line.append(line[index])
            if index == len(line) - 2:
                new_line.append(line[index + 1])
        else:
            next = True
            if index == len(line) - 3:
                new_line.append(line[index + 2])
            index += 1
        index += 1
    line = new_line
    return len(line)

if __name__ == '__main__':
    line = []
    with open('input_files/input_5.txt', 'r') as input:
        while True:
            tmp_input = input.readline()
            if tmp_input == '':
                break
            line.extend(tmp_input[:-1])

    letters = [[letter, letter.upper()] for letter in list(string.ascii_lowercase)]
    result = []
    for letters_list in letters:
        example = [letter for letter in line if letter not in letters_list]
        result.append(calculate_len(example))
    print(min(result))