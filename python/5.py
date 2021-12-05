import numpy as np
import sys
import re
import skimage.draw as skd

for b in [False, True]:
    with open(sys.argv[1], 'r') as f:    
        lines = np.array(re.sub(',|->|\n', ' ',  f.read()).split(), dtype=int).reshape(-1, 2, 2)
        coordinates = np.concatenate([np.dstack(skd.line(x1, y1, x2, y2))[0] for ((x1, y1), (x2, y2)) in lines if b or x1 == x2 or y1 == y2])
        print((np.unique(coordinates, axis=0, return_counts=True)[1] > 1).sum())