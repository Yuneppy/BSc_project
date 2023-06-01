# only positive files
import IntronNew as inn
import statistics

len_arab_don, len_human_don, len_arab_acc, len_human_acc = [], [], [], []
with open('/media/big_hdd/group_1_bioinfo/Bsc/DataSet/Arab_SpliceSite/arab_don.pos', 'r') as f1:
    for seq1 in f1:
        len_arab_don.append(inn.IntronLength(seq1))
with open('/media/big_hdd/group_1_bioinfo/Bsc/human_don.pos', 'r') as f2:
    for seq2 in f2:
        len_human_don.append(inn.IntronLength(seq2))
with open('/media/big_hdd/group_1_bioinfo/Bsc/DataSet/Acceptor_splice_site/arab/arab_acc.pos', 'r') as f3:
    for seq3 in f3:
        len_arab_acc.append(inn.IntronLength(seq3))
with open('/media/big_hdd/group_1_bioinfo/Bsc/human_acc.pos', 'r') as f4:
    for seq4 in f4:
        len_human_acc.append(inn.IntronLength(seq4))   

# mean
mean_arab_don = statistics.mean(len_arab_don)
mean_human_don = statistics.mean(len_human_don)
mean_arab_acc = statistics.mean(len_arab_acc)
mean_human_acc = statistics.mean(len_human_acc)
print('Mean of Arabidopsis donor: ', mean_arab_don)
print('Mean of Human donor: ', mean_human_don)
print('Mean of Arabidopsis acceptor: ', mean_arab_acc)
print('Mean of Human acceptor: ', mean_human_acc)


# median
median_arab_don = statistics.median(len_arab_don)
median_human_don = statistics.median(len_human_don)
median_arab_acc = statistics.median(len_arab_acc)
median_human_acc = statistics.median(len_human_acc)    
print('Median of Arabidopsis donor: ', median_arab_don)
print('Median of Human donor: ', median_human_don)
print('Median of Arabidopsis acceptor: ', median_arab_acc)
print('Median of Human acceptor: ', median_human_acc)

# standard deviation
std_arab_don = statistics.stdev(len_arab_don)
std_human_don = statistics.stdev(len_human_don)
std_arab_acc = statistics.stdev(len_arab_acc)
std_human_acc = statistics.stdev(len_human_acc)
print('Standard deviation of Arabidopsis Donor: ', std_arab_don)
print('Standard deviation of Human Donor: ', std_human_don)
print('Standard deviation of Arabidopsis Acceptor: ', std_arab_acc)
print('Standard deviation of Human Acceptor: ', std_human_acc)
