import sys

def process_commands(commands, depth_strat = 'simple'):
    aim = horizontal = depth = 0
    for (command, magnitude) in commands:
        magnitude = int(magnitude)
        if command == 'forward':
            horizontal += magnitude
            depth += aim*magnitude if depth_strat == 'aim' else 0
        else:
            magnitude = magnitude * (-1 if command == 'up' else 1)
            aim += magnitude
            depth += magnitude if depth_strat == 'simple' else 0
    return depth*horizontal

with open(sys.argv[1], 'r') as f:
    commands = [cmd.split(' ') for cmd in f.readlines()]
    print(f"""Part 1: {process_commands(commands, depth_strat='simple')}
Part 2: {process_commands(commands, depth_strat='aim')}""")