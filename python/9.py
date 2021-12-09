import sys
import numpy as np

def fillBasin(basinMap, x, y):
    if(basinMap[y, x]):
        return 0
    basinMap[y, x] = True

    size = 1
    if y < basinMap.shape[0] - 1:
        size += fillBasin(basinMap, x, y+1)
    if y > 0:
        size += fillBasin(basinMap, x, y-1)
    if x < basinMap.shape[1] - 1:
        size += fillBasin(basinMap, x+1, y)
    if x > 0:
        size += fillBasin(basinMap, x-1, y)
    
    return size
        

with open(sys.argv[1], 'r') as f:
    heightMap = np.array([list(s.strip()) for s in f.readlines()], dtype=int)
    risk_level = 0
    for x in range(0, heightMap.shape[1]):
        for y in range(0, heightMap.shape[0]):
            curr = heightMap[y,x]
            if y < heightMap.shape[0] - 1:
                if heightMap[y+1,x] <= curr:
                    continue
            if y > 0:
                if heightMap[y-1,x] <= curr:
                    continue
            if x < heightMap.shape[1] - 1:
                if heightMap[y,x+1] <= curr:
                    continue
            if x > 0:
                if heightMap[y,x-1] <= curr:
                    continue
            risk_level += curr + 1

    basinMap = heightMap == 9
    basinSizes = []

    for x in range(0, basinMap.shape[1]):
        for y in range(0, basinMap.shape[0]):
            curr = basinMap[y,x]
            if not curr:
                basinSize = fillBasin(basinMap, x, y)
                basinSizes.append(basinSize)

    print(risk_level)
    print(np.sort(basinSizes)[-3:].prod())
