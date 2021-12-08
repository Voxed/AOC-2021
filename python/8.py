import sys
import numpy as np

segment_features = np.array([
    [6, 2, 3, 3], [2, 2, 2, 2], [5, 1, 2, 2], [5, 2, 3, 3], [4, 2, 4, 2],
    [5, 1, 3, 2], [6, 1, 3, 2], [3, 2, 2, 3], [7, 2, 4, 3], [6, 2, 4, 3],
])

def deduce(segment, deductions):
    similarities = (deductions & segment).sum(axis=1)
    feature = np.concatenate(([segment.sum()], similarities[[1,4,7]]))
    return np.argmax((feature == segment_features).sum(axis=1))

with open(sys.argv[1], 'r') as f:
    segments = [[[np.where(np.in1d(np.arange(7), (np.array([ord(c) for c in s]) - 97)), 1, 0) for s in seq.split()] for seq in l.split('|')] for l in f.readlines()]
    count = 0
    count_nums = 0
    for (train, output) in segments:
        segment_deductions = np.full((10,7), -1)
        while((segment_deductions == -1).sum() > 0):
            for segment in train:
                segment_deductions[deduce(segment, segment_deductions)] = segment
        deduced_ouput = np.array([deduce(seg, segment_deductions) for seg in output])
        count_nums += np.in1d(deduced_ouput, [1,4,7,8]).sum()
        count += int(''.join([str(num) for num in deduced_ouput]))
    print(count_nums)
    print(count)