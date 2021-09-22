#!/usr/bin/env python3

import os
import sys
import csv

def main():
    with open('data/True.csv') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for idxa, rowa in enumerate(csv_reader):
            if idxa == 0:
                continue
            with open('data/True.csv') as csvfile2:
                csv_reader2 = csv.reader(csvfile2, delimiter=',')
                for idxb, rowb in enumerate(csv_reader2):
                    if idxb <= idxa:
                        continue
                    if rowa[0] == rowb[0]:
                        print("duplicate: ", rowa[0], idxa, idxb)


if __name__ == '__main__':
    main()