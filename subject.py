#!/usr/bin/env python3
import csv
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

def main():
    subjects = dict()
    with open('data/Fake.csv', newline='') as csvfile:
        fake = csv.reader(csvfile, delimiter=',')
        x = 0
        for row in fake:
            if x != 0:
                subjects[row[-2]] = subjects.get(row[-2], 0) + 1
            x += 1
    
    '''
    objects = subjects.keys()
    y_pos = np.arange(len(objects))
    performance = subjects.values()

    plt.bar(y_pos, performance, align='center', alpha=0.5, color='red')
    plt.xticks(y_pos, objects, rotation=40)
    plt.ylabel('Frequency')
    plt.title('Fake subjects')
    plt.tight_layout()

    plt.savefig('fake_freq.png')

    subjects = dict()
    '''
    with open('data/True.csv', newline='') as csvfile:
        real = csv.reader(csvfile, delimiter=',')
        x = 0
        for row in real:
            if x != 0:
                subjects[row[-2]] = subjects.get(row[-2], 0) + 1
            x += 1
    
    objects = subjects.keys()
    
    y_pos = np.arange(len(objects))
    performance = subjects.values()

    plt.figure()

    c = ['tomato', 'tomato', 'tomato', 'tomato', 'tomato', 'tomato', 'lightskyblue', 'lightskyblue']
    plt.bar(y_pos, performance, align='center', alpha=0.5, color=c)
    plt.xticks(y_pos, objects, rotation=40)
    plt.ylabel('Frequency')
    plt.title('Data Subjects')

    custom_fig = [Line2D([0], [0], color='tomato', lw=4),
                  Line2D([0], [0], color='lightskyblue', lw=4)]
    plt.legend(custom_fig, ['Fake News', 'Real News'])
    plt.tight_layout()


    plt.savefig('freq.png')

    

if __name__ == '__main__':
    main()