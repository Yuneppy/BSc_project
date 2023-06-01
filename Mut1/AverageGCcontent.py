import Features as ft
import statistics
arab_don_train, arab_don_test, arab_don_valid, human_don_train, human_don_test, human_don_valid = [],[],[],[],[],[]
arab_acc_train, arab_acc_test, arab_acc_valid, human_acc_train, human_acc_test, human_acc_valid = [],[],[],[],[],[]

# only positive

# donor
with open('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_don_train.pos', 'r') as f1:
    for seq1 in f1:
        arab_don_train.append(ft.gc_content(seq1))
with open('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_don_test.pos', 'r') as f2:
    for seq2 in f2:
        arab_don_test.append(ft.gc_content(seq2))
with open('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_don_valid.pos', 'r') as f3:
    for seq3 in f3:
        arab_don_valid.append(ft.gc_content(seq3))
with open('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/human_don_train.pos', 'r') as f4:
    for seq4 in f4:
        human_don_train.append(ft.gc_content(seq4))
with open('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/human_don_test.pos', 'r') as f5:
    for seq5 in f5:
        human_don_test.append(ft.gc_content(seq5))
with open('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/human_don_val.pos', 'r') as f6:
    for seq6 in f6:
        human_don_valid.append(ft.gc_content(seq6))
        
# acceptor
with open('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_acc_train.pos', 'r') as f7:
    for seq7 in f7:
        arab_acc_train.append(ft.gc_content(seq7))
with open('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_acc_test.pos', 'r') as f8:
    for seq8 in f8:
        arab_acc_test.append(ft.gc_content(seq8))     
with open('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_acc_valid.pos', 'r') as f9:
    for seq9 in f9:
        arab_acc_valid.append(ft.gc_content(seq9))           
with open('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/human_acc_train.pos', 'r') as f10:
    for seq10 in f10:
        human_acc_train.append(ft.gc_content(seq10))
with open('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/human_acc_test.pos', 'r') as f11:
    for seq11 in f11:
        human_acc_test.append(ft.gc_content(seq11))
with open('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/human_acc_val.pos', 'r') as f12:
    for seq12 in f12:
        human_acc_valid.append(ft.gc_content(seq12))    




arab_don_total = arab_don_train + arab_don_test + arab_don_valid
arab_acc_total = arab_acc_train + arab_acc_test + arab_acc_valid 
human_don_total = human_don_train + human_don_test + human_don_valid       
human_acc_total = human_acc_train + human_acc_test + human_acc_valid                             

# total                                                                                    
av_arab_don = sum(arab_don_total)/len(arab_don_total)
av_arab_acc = sum(arab_acc_total)/len(arab_acc_total)
av_human_don = sum(human_don_total)/len(human_don_total)
av_human_acc = sum(human_acc_total)/len(human_acc_total)

'''# train set
av_arab_don_train = sum(arab_don_train)/len(arab_don_train)
av_arab_acc_train = sum(arab_acc_train)/len(arab_acc_train)
av_human_don_train = sum(human_don_train)/len(human_don_train)
av_human_acc_train = sum(human_acc_train)/len(human_acc_train)

# test set
av_arab_don_test = sum(arab_don_test)/len(arab_don_test)
av_arab_acc_test = sum(arab_acc_test)/len(arab_acc_test)
av_human_don_test = sum(human_don_test)/len(human_don_test)
av_human_acc_test = sum(human_acc_test)/len(human_acc_test)

# validation set
av_arab_don_valid = sum(arab_don_valid)/len(arab_don_valid)
av_arab_acc_valid = sum(arab_acc_valid)/len(arab_acc_valid)
av_human_don_valid = sum(human_don_valid)/len(human_don_valid)
av_human_acc_valid = sum(human_acc_valid)/len(human_acc_valid)'''

'''# train
print('Average GC content of Arabidopdid donor train: ', round(av_arab_don_train,4)*100)
print('Average GC content of Human donor train: ', round(av_human_don_train,4)*100)
print('Average GC content of Arabidopsis acceptor train: ', round(av_arab_acc_train,4)*100)
print('Average GC content of Human acceptor train: ', round(av_human_acc_train,4)*100)

# test
print('Average GC content of Arabidopdid donor test: ', round(av_arab_don_test,4)*100)
print('Average GC content of Human donor test: ', round(av_human_don_test,4)*100)
print('Average GC content of Arabidopsis acceptor test: ', round(av_arab_acc_test,4)*100)
print('Average GC content of Human acceptor test: ', round(av_human_acc_test,4)*100)

# validation
print('Average GC content of Arabidopdid donor valid: ', round(av_arab_don_valid,4)*100)
print('Average GC content of Human donor valid: ', round(av_human_don_valid,4)*100)
print('Average GC content of Arabidopsis acceptor valid: ', round(av_arab_acc_valid,4)*100)
print('Average GC content of Human acceptor valid: ', round(av_human_acc_valid,4)*100)'''

# total
print('Average GC content of Arabidopdid donor total: ', round(av_arab_don,4)*100)
print('Average GC content of Human donor total: ', round(av_human_don,4)*100)
print('Average GC content of Arabidopsis acceptor total: ', round(av_arab_acc,4)*100)
print('Average GC content of Human acceptor total: ', round(av_human_acc,4)*100)


# mean
mean_arab_don = statistics.mean(arab_don_total)
mean_human_don = statistics.mean(human_don_total)
mean_arab_acc = statistics.mean(arab_acc_total)
mean_human_acc = statistics.mean(human_acc_total)
print('Mean of Arabidopsis donor: ', mean_arab_don)
print('Mean of Human donor: ', mean_human_don)
print('Mean of Arabidopsis acceptor: ', mean_arab_acc)
print('Mean of Human acceptor: ', mean_human_acc)


# median
median_arab_don = statistics.median(arab_don_total)
median_human_don = statistics.median(human_don_total)
median_arab_acc = statistics.median(arab_acc_total)
median_human_acc = statistics.median(human_acc_total)    
print('Median of Arabidopsis donor: ', median_arab_don)
print('Median of Human donor: ', median_human_don)
print('Median of Arabidopsis acceptor: ', median_arab_acc)
print('Median of Human acceptor: ', median_human_acc)

# standard deviation
std_arab_don = statistics.stdev(arab_don_total)
std_human_don = statistics.stdev(human_don_total)
std_arab_acc = statistics.stdev(arab_acc_total)
std_human_acc = statistics.stdev(human_acc_total)
print('Standard deviation of Arabidopsis Donor: ', std_arab_don)
print('Standard deviation of Human Donor: ', std_human_don)
print('Standard deviation of Arabidopsis Acceptor: ', std_arab_acc)
print('Standard deviation of Human Acceptor: ', std_human_acc)
                                                                
                                                                
                                
                
                
        
                
                                                                                          
                                                                                           
                                                                
                                                                
                                
                
                
        
                