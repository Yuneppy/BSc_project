import Features as ft
import IntronNew as inn
import statistics


# arab donor
arab_don = []
gc_arab_don = []
with open('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_don.pos', 'r') as f1:
    for seq1 in f1:
        arab_don.append(inn.find_introns(seq1.strip()))
        gc_arab_don.append(ft.gc_content(inn.find_introns(seq1.strip())))  
    
# human donor
human_don = []
gc_human_don = []
with open('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/human_don.pos', 'r') as f2:
    for seq2 in f2:
        human_don.append(inn.find_introns(seq2.strip()))
        gc_human_don.append(ft.gc_content(inn.find_introns(seq2.strip())))
        

# arab acceptor
arab_acc = []
gc_arab_acc = []
with open('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_acc.pos', 'r') as f3:
    for seq3 in f3:
        arab_acc.append(inn.find_introns(seq3.strip()))
        gc_arab_acc.append(ft.gc_content(inn.find_introns(seq3.strip())))

# human acceptor
human_acc = []
gc_human_acc = []
with open('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/human_acc.pos', 'r') as f4:
    for seq4 in f4:
        human_acc.append(inn.find_introns(seq4.strip()))
        gc_human_acc.append(ft.gc_content(inn.find_introns(seq4.strip())))


# mean
mean_arab_don = statistics.mean(gc_arab_don)
mean_human_don = statistics.mean(gc_human_don)
mean_arab_acc = statistics.mean(gc_arab_acc)
mean_human_acc = statistics.mean(gc_human_acc)
print('Mean of Arabidopsis donor: ', mean_arab_don)
print('Mean of Human donor: ', mean_human_don)
print('Mean of Arabidopsis acceptor: ', mean_arab_acc)
print('Mean of Human acceptor: ', mean_human_acc)


# median
median_arab_don = statistics.median(gc_arab_don)
median_human_don = statistics.median(gc_human_don)
median_arab_acc = statistics.median(gc_arab_acc)
median_human_acc = statistics.median(gc_human_acc)    
print('Median of Arabidopsis donor: ', median_arab_don)
print('Median of Human donor: ', median_human_don)
print('Median of Arabidopsis acceptor: ', median_arab_acc)
print('Median of Human acceptor: ', median_human_acc)

# standard deviation
std_arab_don = statistics.stdev(gc_arab_don)
std_human_don = statistics.stdev(gc_human_don)
std_arab_acc = statistics.stdev(gc_arab_acc)
std_human_acc = statistics.stdev(gc_human_acc)
print('Standard deviation of Arabidopsis Donor: ', std_arab_don)
print('Standard deviation of Human Donor: ', std_human_don)
print('Standard deviation of Arabidopsis Acceptor: ', std_arab_acc)
print('Standard deviation of Human Acceptor: ', std_human_acc)
        

