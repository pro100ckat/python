#!/usr/bin/python
import sys
def reduce(*args):
    result = ''
    _map_result_first = args[0]
    _map_result_second = args[1]
    for key1 in _map_result_first.keys():
        if key1 in _map_result_second:
            result += str(_map_result_first[key1]) + ' ' + str(key1) + ' ' + str(_map_result_second[key1]) + '\n'
    print(result)
if __name__ == "__main__":
    STR = '-\t-\n'
    map_result_first = {}
    map_result_second = {}
    for line in sys.stdin:
        if line == STR:
            continue
        temp = line.replace('\n', '').split('\t')
        if temp[1].isalpha():
            map_result_first.update({temp[0]: temp[1]})
            continue
        map_result_second.update({temp[0]: temp[1]})
    reduce(map_result_first, map_result_second)
