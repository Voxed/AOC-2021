import numpy as np
import sys

def most_uncommon(numbers):
    return (((1-numbers).sum(axis=0)/len(numbers)).round()).astype(int)

def base10(number):
    return int(''.join(number.astype(str)), 2)

def part_1(numbers):
    print(
f"""Part 1:
    Gamma: {(gamma := base10(1-most_uncommon(numbers)))} 
    Epsilon: {(epsilon := base10(most_uncommon(numbers)))}
    Power consumption: {gamma*epsilon}""")

def best(numbers, ideal_func):
    for bit in (bit for bit in range(0, numbers.shape[1]) if numbers.shape[0] > 1):
        numbers = np.array([v for v in numbers if v[bit] == ideal_func(numbers)[bit]])
    return numbers[0]

def part_2(numbers):
    print(
f"""Part 2:
    OGR: {(ogr := base10(best(numbers.copy(), lambda numbers: 1-most_uncommon(numbers))))} 
    CSR: {(csr := base10(best(numbers.copy(), lambda numbers: most_uncommon(numbers))))}
    Life support rating: {ogr*csr}""")

with open(sys.argv[1], 'r') as f:    
    numbers = np.array([np.array(list(l.strip()), dtype=int) for l in f.readlines()])
    part_1(numbers)
    part_2(numbers)