import IntronNew as inn
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

len_arab_don, len_human_don, len_arab_acc, len_human_acc = [], [], [], []
with open('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_don.pos', 'r') as f1:
    for seq1 in f1:
        len_arab_don.append(inn.IntronLength(seq1))
with open('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/human_don.pos', 'r') as f2:
    for seq2 in f2:
        len_human_don.append(inn.IntronLength(seq2))
with open('shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_acc.pos', 'r') as f3:
    for seq3 in f3:
        len_arab_acc.append(inn.IntronLength(seq3))
with open('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/human_acc.pos', 'r') as f4:
    for seq4 in f4:
        len_human_acc.append(inn.IntronLength(seq4))   
        
# violin plot
datasets = ['Arabidopsis\ndonor', 'Human\nDonor', 'Arabidopsis\nAcceptor', 'Human\nAcceptor']
lengths_all = [len_arab_don, len_human_don, len_arab_acc, len_human_acc]               
data = []
labels = []
for i, lengths in enumerate(lengths_all):
    data.extend(lengths)
    labels.extend([datasets[i]]*len(lengths))
plt.figure(figsize=(10, 8))    
sns.violinplot(x=labels, y=data)               
plt.ylabel('Intron Length') 
plt.title('Intron Length Comparison (Mutation 1: Consensus1)') 
plt.xticks(rotation=45)  

plt.savefig('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/violinplot_length.png') 


