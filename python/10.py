import sys
import numpy as np

def closes(c1, c2):
    if c1 == '(':
        return c2 == ')'
    if c1 == '[':
        return c2 == ']'
    if c1 == '{':
        return c2 == '}'
    if c1 == '<':
        return c2 == '>'

def complete(line):
    stack = []
    score = 0
    for c in line:
        if c in ['(', '[', '{', '<']:
            stack.append(c)
            continue
        if(len(stack) > 0):
            stack.pop()
    while(len(stack) > 0):
        c = stack.pop()
        score = score*5
        if c == '(':
            score += 1
        if c == '[':
            score += 2
        if c == '{':
            score += 3
        if c == '<':
            score += 4
    return score

def is_corrupt(line):
    stack = []
    for c in line:
        if c in ['(', '[', '{', '<']:
            stack.append(c)
            continue
        if(len(stack) > 0):
            if(not closes(stack.pop(), c)):
                if c == ')':
                    return 3
                if c == ']':
                    return 57
                if c == '}':
                    return 1197
                if c == '>':
                    return 25137
    return 0

with open(sys.argv[1], 'r') as f:
    sumcorr = 0
    sumcomp = []
    incomplete = []
    for l in f.readlines():
        corr = is_corrupt(l.strip())
        if corr == 0:
            sumcomp += [complete(l.strip())]
        sumcorr += corr
    print(sumcorr)
    print(np.median(np.array(sumcomp)))