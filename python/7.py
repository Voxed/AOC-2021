import sys
import numpy as np

def calc_cost(x, crabs, exp=False):
    return ((np.power(crabs-x, 2)*exp + np.abs(crabs-x))/(1 + exp)).sum()

with open(sys.argv[1], 'r') as f:    
    crabs = np.array(f.read().split(','), dtype=int)
    for exp in [False, True]:
        print(np.array([calc_cost(x, crabs, exp) for x in range(crabs.min(), crabs.max()+1)]).min())
