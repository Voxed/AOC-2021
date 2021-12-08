import sys
import numpy as np

def deduce(segments, deduced_segments):
    if segments.shape[0] == 5:
        if np.intersect1d(segments, deduced_segments[1]).shape[0] == 2:
            return 3
        elif np.intersect1d(segments, deduced_segments[4]).shape[0] == 2:
            return 2
        else:
            return 5
    elif segments.shape[0] == 6:
        if np.intersect1d(segments, deduced_segments[7]).shape[0] != 3:
            return 6
        elif np.intersect1d(segments, deduced_segments[4]).shape[0] == 3:
            return 0
        else:
            return 9
    elif segments.shape[0] == 2:
        return 1
    elif segments.shape[0] == 4:
        return 4
    elif segments.shape[0] == 3:
        return 7
    elif segments.shape[0] == 7:
        return 8
    return -1 # Can't deduce yet.

with open(sys.argv[1], 'r') as f:    
    inputs = np.array([
        [np.char.array(list(s)) for s in i.split()] 
        for l in f.readlines() for i in l.split('|')], dtype=object).reshape(-1, 2)

    count = 0
    first_count = 0
    for (train, test) in inputs:
        deduced_segments = [np.array([])] * 10
        while len([s for s in deduced_segments if len(s) == 0]) > 0:
            for seg in train:
                n = deduce(seg, deduced_segments)
                if n >= 0:
                    deduced_segments[deduce(seg, deduced_segments)] = seg

        number_string = ""
        for seg in test:
            for value, deducded_seg in enumerate(deduced_segments):
                if np.intersect1d(seg, deducded_seg).shape[0] == seg.shape[0] == deducded_seg.shape[0]:
                    if value in [1, 4, 7, 8]:
                        first_count += 1
                    number_string += str(value)

        count += int(number_string)

    print(first_count)
    print(count)