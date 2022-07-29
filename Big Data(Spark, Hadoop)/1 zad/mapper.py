#!/usr/bin/python
import sys
if __name__ == '__main__':
    for line in sys.stdin:
        if line:
            print('\t'.join(x for x in line.strip().split(" ") if x != ''))