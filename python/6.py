import sys
import numpy as np

with open(sys.argv[1], 'r') as f:    
    fish = np.unique(np.array(f.read().split(','), dtype=int), return_counts=True)
    state = np.zeros(10)
    state[fish[0]] = fish[1]
    for i in range(0, 256):
        state[[7,9]] = [state[7] + state[0], state[0]]
        state = np.roll(state, -1)
        if i == 79:
            print(state[0:9].sum())
    print(state[0:9].sum())

