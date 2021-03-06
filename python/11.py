import sys
import numpy as np

with open(sys.argv[1], 'r') as f:
    matrix = np.array([list(l.strip()) for l in f.readlines()], dtype=int)

    flashes = 0
    i = 0
    all_flash = None
    flashes_after_100 = None
    while all_flash is None or flashes_after_100 is None:
        if (matrix == 0).all():
            all_flash = i
        if i == 100:
            flashes_after_100 = flashes
        matrix = matrix + 1
        while (matrix > 9).any():
            matrix[matrix > 9] = -1
            matrix = np.pad(matrix,((1,1),(1,1)))
            adjacent_flashes = ((matrix == -1).astype(int) + 
                                (np.roll(matrix, 1, axis=1) == -1).astype(int) +
                                (np.roll(matrix, -1, axis=1) == -1).astype(int))
            adjacent_flashes = (adjacent_flashes + 
                                np.roll(adjacent_flashes, 1, axis=0) +
                                np.roll(adjacent_flashes, -1, axis=0))
            matrix = np.where(matrix < 0, matrix, matrix + adjacent_flashes)[1:-1,1:-1]
            matrix[matrix == -1] = -2
        flashes += (matrix == -2).sum()
        matrix[matrix == -2] = 0
        i += 1
    print(flashes_after_100)
    print(all_flash)