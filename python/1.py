import functools
import sys

def count_decents(lines, decent_func):
    return functools.reduce(lambda state, line: (state[0] + [int(line)], state[1] + decent_func(state[0] + [int(line)])), lines, ([], 0))[1]

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
    part1_decent = lambda stack: 0 if len(stack) < 2 else stack[-1] > stack[-2]
    part2_decent = lambda stack: 0 if len(stack) < 4 else stack[-1] + stack[-2] + stack[-3] > stack[-2] + stack[-3] + stack[-4]
    print(f"""Part 1: {count_decents(lines, part1_decent)}
Part 2: {count_decents(lines, part2_decent)}""")