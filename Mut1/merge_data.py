def merge_files(file1, file2, file3, new_file):
    with open(file1,'r') as f1, open(file2, 'r') as f2, open(file3, 'r')as f3, open(new_file,'w') as f4:
        for line1 in f1:
            f4.write(line1.strip()+'\n')
        for line2 in f2:
            f4.write(line2.strip()+'\n')    
        for i, line3 in enumerate(f3):
            if i < sum(1 for _ in open(file3)) -1:   # check if it is not the last line. to remove the empty space at the last
                f4.write(line3.strip()+'\n')
            else:
                f4.write(line3.strip())     # don't add newline character
          
           

# arab donor positive
merge_files('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_don_train.pos', '/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_don_test.pos','/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_don_valid.pos', '/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_don.pos')       
# arab donor negative
#merge_files('/media/big_hdd/group_1_bioinfo/Bsc/DataSet/Arab_SpliceSite/train.neg', '/media/big_hdd/group_1_bioinfo/Bsc/DataSet/Arab_SpliceSite/test.neg','/media/big_hdd/group_1_bioinfo/Bsc/DataSet/Arab_SpliceSite/valid.neg', '/media/big_hdd/group_1_bioinfo/Bsc/DataSet/Arab_SpliceSite/arab_don.neg')       

# arab acceptor positive
merge_files('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_acc_train.pos', '/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_acc_test.pos','/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_acc_valid.pos', '/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_acc.pos')       
# arab acceptor negative
#merge_files('/media/big_hdd/group_1_bioinfo/Bsc/DataSet/Acceptor_splice_site/arab/acc_ss_train.neg', '/media/big_hdd/group_1_bioinfo/Bsc/DataSet/Acceptor_splice_site/arab/acc_ss_test.neg', '/media/big_hdd/group_1_bioinfo/Bsc/DataSet/Acceptor_splice_site/arab/acc_ss_valid.neg', '/media/big_hdd/group_1_bioinfo/Bsc/DataSet/Acceptor_splice_site/arab/arab_acc.neg')    

# human donor positive
merge_files('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/human_don_train.pos', '/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/human_don_test.pos','/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/human_don_val.pos', '/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/human_don.pos')       
# human donor negative
#merge_files('/media/big_hdd/group_1_bioinfo/Bsc/Human_don_train.neg', '/media/big_hdd/group_1_bioinfo/Bsc/Human_don_test.neg', '/media/big_hdd/group_1_bioinfo/Bsc/Human_don_val.neg', '/media/big_hdd/group_1_bioinfo/Bsc/human_don.neg')     

# human acceptor positive
merge_files('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/human_acc_train.pos', '/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/human_acc_test.pos','/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/human_acc_val.pos', '/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/human_acc.pos')       
# human acceptor negative
#merge_files('/media/big_hdd/group_1_bioinfo/Bsc/Human_acc_train.neg', '/media/big_hdd/group_1_bioinfo/Bsc/Human_acc_test.neg', '/media/big_hdd/group_1_bioinfo/Bsc/Human_acc_val.neg', '/media/big_hdd/group_1_bioinfo/Bsc/human_acc.neg')     
     