#!/usr/bin/env python3

def get_data(index, line):
    start, end = index, index
    while line[start] != ' ':
        start -= 1
    while end != len(line) and line[end] != ':':
        end += 1
    return [int(''.join(line[start + 1: index])), int(''.join(line[index + 1 : end]))]

def get_max(coords, sizes):
    max_x, max_y = 0, 0
    for i in range(0, len(coords)):
        temp_x, temp_y = coords[i][0] + sizes[i][0], coords[i][1] + sizes[i][1]
        if temp_x > max_x:
            max_x = temp_x
        if temp_y > max_y:
            max_y = temp_y
    return [max_x, max_y]

def fill_in(coords, sizes, matrix):
    for number_of_element in range(0, len(coords)):
        for vertical in range(coords[number_of_element][1], coords[number_of_element][1] + sizes[number_of_element][1]):
            for horizontal in range(coords[number_of_element][0], coords[number_of_element][0] + sizes[number_of_element][0]):
                if matrix[vertical][horizontal] == '.':
                    matrix[vertical][horizontal] = 'x'
                elif matrix[vertical][horizontal] == 'x':
                    matrix[vertical][horizontal] = '!'

def count(limits, matrix):
    number_of_inches = 0
    for vertical in range(0, limits[1]):
        for horizontal in range(0, limits[0]):
            if matrix[vertical][horizontal] == '!':
                number_of_inches += 1
    return number_of_inches


if __name__ == '__main__':
    coords = []
    sizes = []
    with open("input_files/input_3.txt", 'r') as input:
        while True:
            line = list(input.readline())[:-1]
            if line == []:
                break
            coords.append(get_data(line.index(','), line))
            sizes.append(get_data(line.index('x'), line))
    limits = get_max(coords, sizes)
    matrix = []
    for i in range(0, limits[1]):
        matrix.append(['.' for _ in range(0, limits[0])])
    fill_in(coords, sizes, matrix)
    print(count(limits, matrix))
    
