#!/usr/bin/env python3

import re

class guard:
    def __init__(self):
        self.minutes_counter = 0
        self.all_minutes = {}
        

from datetime import datetime

if __name__ == '__main__':
    dates = {}
    guards_set = {}
    regex_pattern = re.compile('[0-9]+')

    with open('input_files/input_4.txt', 'r') as input:
        while True:
            line = input.readline()
            if line == '':
                break
            date_string = line[1:line.find(' ')]
            date_object = datetime.strptime(date_string, '%Y-%m-%d')
            date_string = line[line.find(' ') + 1: line.find(']')]
            time_object = datetime.strptime(date_string, '%H:%M')
            if date_object not in dates:
                dates[date_object] = []
            time_action_tuple = (time_object, line[line.find(']') + 2:-1])
            dates[date_object].append(time_action_tuple)
        sorted_dates = sorted(dates.keys())
        guard_number, start, end = 0, 0, 0
        for day in sorted_dates:
            sorted_hours = sorted(dates[day])
            for message in sorted_hours:
                if 'Guard' in message[1]:
                    guard_number = int(regex_pattern.search(message[1]).group(0))
                elif 'falls asleep' in message[1]:
                    start = message[0].minute
                else:
                    end = message[0].minute
                    if guard_number not in guards_set:
                        guards_set[guard_number] = guard()
                        guards_set[guard_number].minutes_counter = end - start
                    else:
                        guards_set[guard_number].minutes_counter += end - start
                    for minute in range(start, end):
                        if minute not in guards_set[guard_number].all_minutes:
                            guards_set[guard_number].all_minutes[minute] = 1
                        else:
                            guards_set[guard_number].all_minutes[minute] += 1

    max_counter = 0
    max_guard_id = 0
    for id, guard in guards_set.items():
        if guard.minutes_counter > max_counter:
            max_guard_id = id
            max_counter = guard.minutes_counter

    max_minute = 0
    max_minute_counted = 0
    for minute, minute_counted in guards_set[max_guard_id].all_minutes.items():
        if guards_set[max_guard_id].all_minutes[minute] > max_minute_counted:
            max_minute = minute
            max_minute_counted = guards_set[max_guard_id].all_minutes[minute]

    print('----------------------')
    print(max_guard_id)
    print(str(max_minute) + ': ' + str(max_minute_counted))