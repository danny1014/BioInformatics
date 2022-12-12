import random
import math

def getIntervalGaps(aligns, i, j):
    # 1. 전방 탐색을 위한 포인터 fsearch_j를 j - 1로 초기화
    fsearch_j = j - 1
    bserch_j = j
    interval_gaps = []
    is_symbol = False
    
    # 2. j 뒤의 gap 탐색(j 포함)
    while not is_symbol:
        if bserch_j > len(aligns[i]) - 1:
            break
        elif aligns[i][bserch_j] == "-":
            interval_gaps.append(bserch_j)
            bserch_j += 1
        else:
            is_symbol = True

    # 3. j 앞의 gap 탐색(j 미포함)
    is_symbol = False
    while not is_symbol:
        if fsearch_j < 0:
            break
        elif aligns[i][fsearch_j] == "-":
            interval_gaps.insert(0, fsearch_j)
            fsearch_j -= 1
        else:
            is_symbol = True

    return interval_gaps


def getMaxLeng(lines):
    max = 0

    for i in lines:
        length = len(i)

        if length >= max:
            max = length
    
    return max

def mutation(child, mutation_rate):
    child_cnt = len(child)

    mutation_prob = round(random.uniform(0,1),2)
    if mutation_prob <= mutation_rate:
        prob = round(random.uniform(0,1),2)

        # 1. Gaps Removal 적용
        if prob < 0.5:
            i = random.randint(0, child_cnt-1)
            j = random.randint(0, len(child[i]) - 1)

            while child[i][j] != "-":
                i = random.randint(0, child_cnt-1)
                j = random.randint(0, len(child[i]) - 1)
        
            interval_gaps = getIntervalGaps(child, i, j)
            start = interval_gaps[0]
            end = interval_gaps[-1]

            child[i] = child[i][:start] + child[i][end+1:]

        # 2. Gaps Addition 적용
        else:
            i = random.randint(0, child_cnt - 1)
            j = random.randint(1, len(child[i]) - 2)
            k = random.randint(1, math.ceil(getMaxLeng(child) * 0.1))
            add = ""

            for num_ in range(k):
                add += "-"
            child[i] = child[i][:j] + add + child[i][j:]
    
    return child


# child = [
#     "AT--G-C-A",
#     "AA--GC-A-",
#     "AT----ACT"
# ]

# print(mutation(child))
