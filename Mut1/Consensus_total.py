import Features as ft

arab_don_tot = ft.consensus_sequence('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_don.pos')
arab_acc_tot = ft.consensus_sequence('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_acc.pos')

human_don_tot = ft.consensus_sequence('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/human_don.pos')
human_acc_tot = ft.consensus_sequence('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/human_acc.pos')            

'''# whole sequence
print('Consensus Sequence of Arabidopsis Donor total pos: ', arab_don_tot)
print('Consensus Sequence of Human Donor total pos: ', human_don_tot)
print('Consensus Sequence of Arabidopsis Acceptor total pos: ', arab_acc_tot)
print('Consensus Sequence of Human Acceptor total pos: ', human_acc_tot)'''


# each 10 position before and after the splicesite
print('Consensus Sequence of Arabidopsis Donor upstream pos: ', arab_don_tot[89:99])
print('Consensus Sequence of Arabidopsis Donor downstream pos: ', arab_don_tot[101:111])

print('Consensus Sequence of Human Donor upstream pos: ', human_don_tot[89:99])
print('Consensus Sequence of Human Donor downstream pos: ', human_don_tot[101:111])

print('Consensus Sequence of Arabidopsis Acceptor upstream pos: ', arab_acc_tot[89:99])
print('Consensus Sequence of Arabidopsis Acceptor downstream pos: ', arab_acc_tot[101:111])

print('Consensus Sequence of Human Acceptor upstream pos: ', human_acc_tot[89:99])
print('Consensus Sequence of Human Acceptor downstream pos: ', human_acc_tot[101:111])




                   