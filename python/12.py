import sys
import numpy as np

def all_paths(Map, loc, visited=[], done = [], twice = False):
    visited = visited + [loc]
    next_pos = [x[1] for x in Map if x[0] == loc] + [x[0] for x in Map if x[1] == loc]
    #next_pos = [x for x in next_pos if (x.islower() and x not in visited) or x.isupper()]
    for x in next_pos:
        if x == 'end':
            done.append(visited + [x])
        elif (x.islower() and ((x not in visited) or (twice and x != 'end' and x != 'start'))) or x.isupper():
            if x in visited and x.islower(): #consume twice
                all_paths(Map, x, visited, done)
            else: #dont
                all_paths(Map, x, visited, done, twice=twice)

    return done

with open(sys.argv[1], 'r') as f:
    Map = np.array([l.strip().split('-') for l in f.readlines()])
    paths = all_paths(Map, 'start', twice=True)
    print(len(paths))
    #ending = [x for x in separate_paths(paths) if 'end' in x]
    #print(ending)