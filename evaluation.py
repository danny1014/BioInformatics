def max_len(lines):
    temp = 0
    for line in lines:
        if(temp < len(line)):
            temp = len(line)
    return temp


def read_input_lines(path):
    temp = ""
    with open(path) as f:
        temp = f.read()
    # 문자열 빈 곳 없애기
    temp = temp.replace(" ", "")
    # 텍스트에서 라인 추출
    lines = temp.split("\n")
    return lines

def fill_diff(lines):
    maxLen = max_len(lines)
    temp = 0
    for line in lines:
        diff = maxLen - len(line)
        for x in range(diff):
            line = line + "-"
        lines[temp] = line
        temp = temp +1
    return lines

# 입력되는 sequence의 길이가 동일하다고 가정
# 그 중 모든 sequence의 특정 위치가 "-"일 때 이를 제거하는 함수
def remove_diff(lines):
    indexs = []
    # sequence의 길이 만큼 반복
    for x in range(len(lines[0])):
        condition = True

        # line들의 수 만큼 반복
        for y in range(len(lines)):
            # "-"가 아닌 부분이 있으면 False
            if(lines[y][x] != "-"):
                condition = False
        
        if(condition):
            indexs.append(x)

    indexs.reverse()
    for x in range(len(lines)):
        line = []
        for y in range(len(lines[x])):
            line.append(lines[x][y])
        for y in indexs:
            line.pop(y)
        lines[x] = ''.join(line)

    return lines

def no_change(best, min_generations):
        if len(best) < min_generations:
            return False
        else:
            percent = int(0.2 * len(best))
            last = best[-percent:]

            if variance(last) < 1.05:
                return True

        return False

def variance(vals):
    mean = sum(vals) / len(vals)
    vsum = 0
    for val in vals:
        vsum = vsum + (val - mean)**2
    variance = vsum / len(vals)
    return variance

# [A, T, C, G] 순으로 정의되어 있음
# 즉, A - A : (0, 0) , A - C : (0, 2), G - T : (3, 1) 와 같이 인덱싱
def make_matrix():
    matrix = [[4, 0, 0, 0], [0, 5, -1, -2], [0, -1, 9, -3], [0, -2, -3, 6]]
    return matrix
     

def char_to_int(a):
    if a == 'A':
        return 0
    elif a == 'T':
        return 1
    elif a == 'C':
        return 2
    elif a =='G':
        return 3
    else:
        return -1

def score_lines(line_a, line_b, gap_exit, gap_expan, matrix):
    score = 0
    # previous가 0이면 처음 gap이 나온 것, 1이면 이전에 gap이 나온 것
    previous = 0
    for x in range(len(line_a)):
        a = char_to_int(line_a[x])
        b = char_to_int(line_b[x])
        if( a != -1 and b != -1):
            score += matrix[a][b]
            previous = 0
        else:
            # gap이 처음오는 것이라면
            if previous == 0:
                score = score - gap_exit - gap_expan
                previous = 1
            # gap이 이전에 있었다면
            else: 
                score = score - gap_expan
    return score

def evaluation_func(lines, gap_exit, gap_expan):
    score = 0
    matrix = make_matrix()
    for i in range(1, len(lines)):
        for j in range(0, i):
            score += score_lines(lines[i], lines[j], gap_exit, gap_expan, matrix)
            
    return score
            
# # txt 파일에서 sequence들 가져오기
# lines = read_input_lines("data\\sequences\\data_2.txt")
# # 각 sequence 길이 맞추기 ('-' 삽입) 
# lines = fill_diff(lines)

# matrix =  make_matrix()

# score = evaluation_func(lines)
# print(score)

# lines = ["-----", "A----", "-A-A-"]
# remove_diff(lines)

# print(lines)