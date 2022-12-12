import evaluation
from evaluation import evaluation_func
from evaluation import no_change
from selection import selection
from initpop import init_pop
from crossover import crossover
from mutation import mutation

text_num = "1"
# txt 파일에서 sequence들 가져오기
lines = evaluation.read_input_lines(f"data\\sequences\\data_{text_num}.txt")
# 각 sequence 길이 맞추기 ('-' 삽입) 
lines = evaluation.fill_diff(lines)
# line 들에는 평가값을 구하려는 sequence들의 배열이 들어 있다.

# 비교를 위한 clustal_w 데이터 가져오기
clustal_w_liens = evaluation.read_input_lines(f"data\\sequences\\clustal_{text_num}.out")


# 반복을 위한 변수 정의
chromosomes = 100 # 한 세대의 데이터 수
generations = 400 # 최대 반복 수
min_generations = 200 # 최소 반복 수
mutation_rate = 0.05 # 변이 확률 (5%)
gap_exit = 1
gap_expan = 0.7

def test():


    # 반복 횟수를 측정하기 위한 변수
    generation = 0
    # 세대 별 최대 평가값 및 sequence들을 저장하기 위한 변수
    best_evaluation = []
    best_sequence = []

    # 초기 세대 생성
    # 한 데이터의 구조
    # sequence : [배열], evaluation : 평가값
    pop = init_pop(lines, chromosomes) #population 0

    while (generation < generations):
        # print(generation)
        # 최대값들이 저장되기 위해 가장 낮은 값 설정
        max_value = -9999 # 최대값의 evaluation
        max_index = 0 # 최대값의 idnex
        # 세대의 데이터들에 대한 evaluation 측정
        for x in range(len(pop)):
            #  각 데이터에 대한 evalution 계산
            pop[x]["evaluation"] = evaluation_func(pop[x]["sequence"], gap_exit, gap_expan)

            # 각 세대의 최대 평가값을 저장하기 위한 부분
            if(max_value <pop[x]["evaluation"]):
                max_value = pop[x]["evaluation"]
                # sequence를 찾기 위한 인덱스 저장
                max_index = x
        # 현재 세대 최대 평가값 저장
        best_evaluation.append(max_value)
        best_sequence.append(pop[max_index]["sequence"])

        if no_change(best_evaluation, min_generations):
            print("no variation\n")
            break

        # crossover를 통하여 새롭게 생성한 데이터들이 저장될 배열
        new_pop = []

        # 전체 생성된 데이터 수 만큼 세로운 데이터 생성
        for x in range(chromosomes):
            # 현제 세대에서 특정 데이터 2개 선정
            p1, p2 = selection(pop)
            # 두 데이터를 crossover하여 새로운 데이터 생성 
            data = crossover(p1["sequence"], p2["sequence"])
            data = mutation(data, mutation_rate)

            # 서로 다른 길이의 sequence를 crossover하여 이후 evalution에 문제 발생 가능
            # 따라서 길이를 맞춰주는 과정을 추가해야 한다.
            data = evaluation.fill_diff(data) # 길이 맞추기
            data = evaluation.remove_diff(data) # gap만 있는 열 없애기

            # new pop에 생성한 데이터 추가
            new_pop.append({"sequence": data, "evaluation": 0})

            
        # 새로운 데이터에 대한 evaluation 계산
        for x in range(len(new_pop)):
            new_pop[x]["evaluation"] = evaluation_func(new_pop[x]["sequence"], gap_exit, gap_expan)

        # 각 population 들을 evalution 순으로 정렬한다. 
        # reverse를 적용하여 큰 순으로 정렬된다. ( pop[0]: 큰 값 -> pop[chrom-1]: 작은 값)
        pop = sorted(pop, key=lambda pop: pop["evaluation"], reverse=True)
        # reverse를 안 적용하여 작은 순으로 정렬된다. ( pop[0]: 작은 값 -> pop[chrom-1]: 큰 값)
        new_pop = sorted(new_pop, key=lambda new_pop: new_pop["evaluation"], reverse= False)

        # 수정사항 있음 그냥 반으로 잘라 붙이는 것으로 만들기
        # pop을 50% new_pop을 50% 비율로 섞는다.
        # 반으로 자를 index 구하기 
        slice_index_a = int(len(pop)/2)
        # pop 반 자르기
        pop_temp = pop[:slice_index_a]
        # new pop 반 자르기
        new_pop_temp = new_pop[slice_index_a:]
        # 반으로 자른거 합치기
        pop_temp.extend(new_pop_temp)
        # 현재 population을 위에서 새롭게 만든 population으로 교체
        pop = new_pop_temp

        # 한 세대 증가
        generation += 1

    pop = sorted(pop, key=lambda pop: pop["evaluation"], reverse=True)
    print( "SAGA Result : " + str(pop[0]["evaluation"]))

    for x in pop[0]["sequence"]:
        print(x)

    return pop[0]["evaluation"]

total_sum = 0.0
max_value = 0.0
for test_num in range(1):

    print("current test num: " + str((test_num+1)))
    temp = test()
    if temp > max_value:
        max_value = temp
    total_sum =  total_sum + temp

print("clustal_w Result : " + str(evaluation_func(clustal_w_liens, gap_exit, gap_expan)))
for x in clustal_w_liens:
    print(x)

print("최대 : "+str(max_value))
print("평균 : "+str(total_sum/5))