import sys

def process_commands(cmds, depth_strat = 'simple'):
    d = h = a = 0
    for (c, m) in cmds:
        (fc, uc, dc) = [int(t == c) for t in ['forward', 'up', 'down']]
        h += m*fc
        a += d*m*fc
        d += m * (-uc + dc) 
    return (d if depth_strat == 'simple' else a)*h

with open(sys.argv[1], 'r') as f:
    cmds = [(c, int(m)) for l in f.readlines() for (c, m) in [l.split(' ')]]
    print(f"""Part 1: {process_commands(cmds, depth_strat='simple')}
Part 2: {process_commands(cmds, depth_strat='aim')}""")