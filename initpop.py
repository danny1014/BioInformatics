import random
from GSA import global_align
from GSA import ScoreParam
from evaluation import fill_diff

#line에서 사용할 seq개수

seq1 = "CTATCGAGTCTTCCCTCCCTCCTTCTCTGCCCCCTCCGCTCCCGCTGGAG"
seq2 = "CCCTCCACCCTACAAGTGGCCTACAGGGCACAGGTGAGGCGGGACTGGAC"
seq3 = "AGCTCCTGCTTTGATCGCCGGAGATCTGCAAATTCTGCCCATGTCGGGGC"
seq4 = "TGCAGAGCACTCCGACGTGTCCCATAGTGTTTCCAAACTTGGAAAGGGCG"
seq5 = "GGGGAGGGCGGGAGGATGCGGAGGGCGGAGGTATGCAGACAACGAGTCAG"
seq6 = "AGTTTCCCCTTGAAAGCCTCAAAAGTGTCCACGTCCTCAAAAAGAATGGA"
seq7 = "ACCAATTTAAGAAGCCAGCCCCGTGGCCACGTCCCTTCCCCCATTCGCTC"
seq8 = "CCTCCTCTGCGCCCCCGCAGGCTCCTCCCAGCTGTGGCTGCCCGGGCCCC"
seq9 = "CAGCCCCAGCCCTCCCATTGGTGGAGGCCCTTTTGGAGGCACCCTAGGGC"
seq10 = "CAGGGAAACTTTTGCCGTATAAATAGGGCAGATCCGGGCTTTATTATTTT"
seq = [seq1, seq2, seq3, seq4, seq5, seq6, seq7, seq8, seq9, seq10]



chrom = 10

def init_pop(seq, chrom):
    
    pop = []
    
    for c in range(chrom):
        data= []
        for i in range(len(seq)):
            temp = []

            for j in range(len(seq)):
                if i != j:
                    curr_alignment = global_align(seq[i], seq[j])[0]
                    temp.append(curr_alignment)
            data.append(random.choice(temp))
        
        data = fill_diff(data)
        
        pop.append({"sequence" : data, "evaluation" : 0})
    return pop
    
# pop = init_pop(seq , chrom)

# for x in pop:
#     print(x)