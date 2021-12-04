import sys
import numpy as np

with open(sys.argv[1], 'r') as f:    
    sequence = list(map(lambda x: int(x), f.readline().split(',')))            
    boards = np.concatenate([list(map(lambda x: int(x), filter(lambda x: x != '', line.strip().split(' ')))) for line in f.readlines()]).ravel()
    boards = [np.array(boards[x:x+5*5]).reshape(5,5) for x in range(0, len(boards), 5*5)]
    last_winner = None
    for s in sequence:
        boards = [b*(-2*(b == s)+1) for b in boards if b is not None]
        for (i, b) in enumerate(boards):
            if np.any([np.all((b < 0)[:, x]) or np.all((b < 0)[x]) for x in range(0, 5)]):
                final_num = s
                if last_winner is None:
                    print(f"""Part 1: {b[b >= 0].sum()*final_num}""")
                last_winner = b
                boards[i] = None
    print(f"""Part 2: {last_winner[last_winner >= 0].sum()*final_num}""")
