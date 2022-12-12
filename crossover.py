import random

def read_input_lines(path):
    temp = ""
    with open(path) as f:
        temp = f.read()
    # 문자열 빈 곳 없애기
    temp = temp.replace(" ", "")
    # 텍스트에서 라인 추출
    lines = temp.split("\n")
    return lines

def crossover(lines1, lines2):
    #cline = crossovered result
    cline = []
    #l=1~lines의 크기까지의 정수를 원소로 갖는 배열
    l = list(range(0, len(lines1)))
    #s=lines1에서 다음 세대로 넘어갈 서열의 index
    s = sorted(random.sample(l,random.choice(l)))
    #l의 집합 중 s에 포함된 index는 lines1에서 유전, 포함되지 않으면 lines2에서 유전된다.
    for i in l:
        if(i in s):
            cline.append(lines1[i])
        else:
            cline.append(lines2[i])
    
    return cline


# lines1 = read_input_lines("data\\sequences\\data_2.txt")
# lines2 = read_input_lines("data\\sequences\\data_3.txt")

# print(lines1)
# print(lines2)
# print(crossover(lines1, lines2))