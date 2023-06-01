import FeatureComparison as fc

# only positive
arab_don_train, human_don_train = fc.CompInLength('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_don_train.pos', '/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/human_don_train.pos')
arab_don_test, human_don_test = fc.CompInLength('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_don_test.pos', '/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/human_don_test.pos')
arab_don_valid, human_don_valid = fc.CompInLength('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_don_valid.pos', '/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/human_don_val.pos')
    
arab_acc_train, human_acc_train = fc.CompInLength('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_acc_train.pos', '/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/human_acc_train.pos')
arab_acc_test, human_acc_test = fc.CompInLength('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_acc_test.pos', '/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/human_acc_test.pos')
arab_acc_valid, human_acc_valid = fc.CompInLength('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_acc_valid.pos', '/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/human_acc_val.pos')
    
arab_don_total = arab_don_train + arab_don_test + arab_don_valid
arab_acc_total = arab_acc_train + arab_acc_test + arab_acc_valid
    
human_don_total = human_don_train + human_don_test + human_don_valid
human_acc_total = human_acc_train + human_acc_test + human_acc_valid
 
 
 
av_arab_don_train = sum(arab_don_train)/len(arab_don_train)
av_hum_don_train = sum(human_don_train)/len(human_don_train)  

av_arab_don_test = sum(arab_don_test)/len(arab_don_test)
av_hum_don_test = sum(human_don_test)/len(human_don_test)  
 
av_arab_don_valid = sum(arab_don_valid)/len(arab_don_valid)
av_hum_don_valid = sum(human_don_valid)/len(human_don_valid)  

av_arab_acc_train = sum(arab_acc_train)/len(arab_acc_train)
av_hum_acc_train = sum(human_acc_train)/len(human_acc_train)  

av_arab_acc_test = sum(arab_acc_test)/len(arab_acc_test)
av_hum_acc_test = sum(human_acc_test)/len(human_acc_test)  
 
av_arab_acc_valid = sum(arab_acc_valid)/len(arab_acc_valid)
av_hum_acc_valid = sum(human_acc_valid)/len(human_acc_valid)  
 
av_arab_don = sum(arab_don_total)/len(arab_don_total)
av_human_don = sum(human_don_total)/len(human_don_total)
av_arab_acc = sum(arab_acc_total)/len(arab_acc_total)
av_human_acc = sum(human_acc_total)/len(human_acc_total)


print('Average Intron Length of Arabidopsis donor train: ', av_arab_don_train)
print('Average Intron Length of Human donor train: ', av_hum_don_train)
print('Average Intron Length of Arabidopsis acceptor train: ', av_arab_acc_train)    
print('Average Intron Length of Human acceptor train: ', av_hum_acc_train)

print('Average Intron Length of Arabidopsis donor test: ', av_arab_don_test)
print('Average Intron Length of Human donor test: ', av_hum_don_test)
print('Average Intron Length of Arabidopsis acceptor test: ', av_arab_acc_test)    
print('Average Intron Length of Human acceptor test: ', av_hum_acc_test)

print('Average Intron Length of Arabidopsis donor valid: ', av_arab_don_valid)
print('Average Intron Length of Human donor valid: ', av_hum_don_valid)
print('Average Intron Length of Arabidopsis acceptor valid: ', av_arab_acc_valid)    
print('Average Intron Length of Human acceptor valid: ', av_hum_acc_valid)


print('Average Intron Length of Arabidopsis donor: ', av_arab_don)
print('Average Intron Length of Human donor: ', av_human_don)
print('Average Intron Length of Arabidopsis acceptor: ', av_arab_acc)    
print('Average Intron Length of Human acceptor: ', av_human_acc)
    