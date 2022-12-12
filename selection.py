import math
import random

def selection(mutliple_aligns):

    # 0. evaluation 정규화해서 저장하기
    normal_eval = []
    for align in mutliple_aligns:
        normal_eval.append(align["evaluation"])

    min_eval = min(normal_eval)
    if min_eval < 0 :
        for i in range(len(normal_eval)):
            normal_eval[i] += -(min_eval)

    # 1. evaluation에 따른 prob 구하기
    eval_sum = 0
    for eval in normal_eval:
        eval_sum += eval
    mating_pool = []
    eval_prob = []
    if eval_sum !=0:
        for eval in normal_eval:
            eval_prob.append(math.ceil((eval/eval_sum )* 100))

        # 2. prob에 따른 mating pool 구축 --> 룰렛 휠 셀렉션 원리 이용
        
        for i in range(len(eval_prob)):
            for j in range(eval_prob[i]):
                mating_pool.append(mutliple_aligns[i])
    else:
        mating_pool = mutliple_aligns
    # 3. 부모 선택 진행
    parent1 = random.choice(mating_pool)
    parent2 = random.choice(mating_pool)

    # while (parent1 == parent2):
    #     parent2 = random.choice(mating_pool)

    return (parent1, parent2)

# multiple_aligns = [
#                     {"aligns" : "1T-G---A-C\nAA--TT--G-\nAG--TT--G-", "evaluation":3}, 
#                     {"aligns" : "2T-G---A-C\nAA--TT--G-\nAG--TT--G-", "evaluation":1}, 
#                     {"aligns" : "3T-G---A-C\nAA--TT--G-\nAG--TT--G-", "evaluation":10}, 
#                     {"aligns" : "4T-G---A-C\nAA--TT--G-\nAG--TT--G-", "evaluation":2}, 
#                     {"aligns" : "5T-G---A-C\nAA--TT--G-\nAG--TT--G-", "evaluation":13}, 
#                     {"aligns" : "6T-G---A-C\nAA--TT--G-\nAG--TT--G-", "evaluation":5}, 
#                     {"aligns" : "7T-G---A-C\nAA--TT--G-\nAG--TT--G-", "evaluation":23}, 
#                     {"aligns" : "8T-G---A-C\nAA--TT--G-\nAG--TT--G-", "evaluation":9}
#                  ]

# p1, p2 = selection(multiple_aligns)
# print(p1, p2)

