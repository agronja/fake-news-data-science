#!/usr/bin/env python3

import os
import sys
import csv

def main():
    with open('data/True.csv', 'r') as infile, open('data/combined.csv', 'w') as outfile:
        seen = set()
        x = 0
        for line in infile:
            if line in seen:
                continue

            seen.add(line)
            line_write = line.strip().split(',')
            line_write.pop(-1)
            line_write.pop(-1)
            line_write.pop(-1)
            if not x:
                line_write.append('text')
                line_write.append('label\n')
                x += 1
            else:
                line_write.append('1\n')
            outfile.write(",".join(line_write))
        

if __name__ == '__main__':
    main()