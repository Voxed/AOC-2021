import sys
import numpy as np

with open(sys.argv[1], 'r') as f:    
    sequence = list(map(lambda x: int(x), f.readline().split(',')))            
    boards = np.concatenate([np.array(line.strip().split(), dtype=int) for line in f.readlines()]).ravel().reshape(-1,5,5)
    last_winner = None
    for s in sequence:
        boards = [np.where(b != s, b, -1) for b in boards if b is not None]
        for (i, b) in enumerate(boards):
            if ((b == -1).all(axis=0) + (b == -1).all(axis=1)).any():
                final_num = s
                if last_winner is None:
                    print(f"""Part 1: {b[b != -1].sum()*final_num}""")
                last_winner = b
                boards[i] = None
    print(f"""Part 2: {last_winner[last_winner != -1].sum()*final_num}""")
