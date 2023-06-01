'''
This file contains all possible features that can lead to the different performance between Arabidopsis and Human
'''


'''
------------------------------------------------------------------------------------------------------------------------------------------------
1. Intron length
------------------------------------------------------------------------------------------------------------------------------------------------
This function returns the intorn length of each sequence
'''
def IntronLength(seq):
    # if the data is for donor site
    intron_length = 0
    if seq[99] == 'G':
        for i in range(101,200):
            if seq[i:i+2] == 'AG':
                intron_length = i-99-2
                break
        return intron_length
    
    # if the data is for acceptor site
    else:
        for i in range(97):
            if seq[99-i-2:99-i] == 'GT':
                intron_length = i+1
                break
        return intron_length

# seq = "ATGTCGCTGCCAGTCGACGTGCTAGCTAGTCGTGACTAGCGTCGACGATCGAGCTAGCGGCGCGCGCGGGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCAGCTAGCTGCTAGCTAGCTAGCTAGCTGACTGCAGCTGACGTCGAGCTGCGCGCGCTCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCTCGCGCGCGCGCGCTAGCTAGCTAGCTAGCTAGCTGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTGCTAGCTGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAG"    
# print('Intron Length: ', IntronLength(seq)) 
# print(IntronLength('CTCATTAAAACTTCTTCCTAAAATACCAAAAAAGCACAGAAGACCTATATCTAAGGAAAAAGAAGCTTATATAATGCTTCAAGGAATATTTCTTAGAAAAGAAAGAAATGTTACTTAAGGGTAAACACTAGCCAATAAGTTGCATGCTTTCAACAGGACCAAATGAAATAGAAAAAGAAATAAACCTATTTATTTAGCTG'))
    
'''
------------------------------------------------------------------------------------------------------------------------------------------------
2. GC content
------------------------------------------------------------------------------------------------------------------------------------------------    
'''    
def gc_content(seq):
    gc_count = seq.count('G') + seq.count('C')
    if gc_count == 0:
        return 0
    else:
        return gc_count/len(seq)

#print('GC Content: ', gc_content(seq))



'''
------------------------------------------------------------------------------------------------------------------------------------------------
3. Codon Usage
------------------------------------------------------------------------------------------------------------------------------------------------    
'''
import pandas as pd
import numpy as np
codon_table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}

def codon_frequency(sequence):
    codon_count = {}
    for i in range(0,len(sequence),3):
        codon = sequence[i:i+3]
        if codon in codon_table:
            if codon in codon_count:
                codon_count[codon] += 1
            else:
                codon_count[codon] = 1
    total_codons = sum(codon_count.values()) 
    codon_freq = {}
    for codon in codon_count:
        codon_freq[codon] = codon_count[codon]/total_codons
    return codon_freq

'''sequence = 'GACCTGTACGACTCTGGCCATGGGGAACAGCCACTGTGTCCCTCAGGCCCCCAGGAGGCTCCGGGCCTCCTTCTCCAGAAAGCCCTCGCTGAAGGGAAACAGGTGAGCGGGGCGTGGGTGCGGCCACCTGGGCGCAGGGCTCCCCCACCCGCTCCGGGGCCAAGCCACGAGACCCCTTGCCTTGTCCCCAGAGAGGACAG'
print(codon_frequency(sequence))'''


def codon_usage_bias(sequence):
    codon_freq = codon_frequency(sequence)
    expected_freq = {}
    for codon in codon_freq:
        amino_acid = codon_table[codon]
        if amino_acid in expected_freq:
            expected_freq[amino_acid] += codon_freq[codon]
        else:
            expected_freq[amino_acid] = codon_freq[codon] 
    obs_exp_ratio = {}
    for codon in codon_freq:
        amino_acid = codon_table[codon]
        obs_exp_ratio[codon] = codon_freq[codon]/expected_freq[amino_acid]
    return obs_exp_ratio

sequence = 'GACCTGTACGACTCTGGCCATGGGGAACAGCCACTGTGTCCCTCAGGCCCCCAGGAGGCTCCGGGCCTCCTTCTCCAGAAAGCCCTCGCTGAAGGGAAACAGGTGAGCGGGGCGTGGGTGCGGCCACCTGGGCGCAGGGCTCCCCCACCCGCTCCGGGGCCAAGCCACGAGACCCCTTGCCTTGTCCCCAGAGAGGACAG'
print(codon_usage_bias(sequence))            
               
'''
It provides information about how selective pressure has influences the usage of different codons for a particular amino acid in a genome
RSCU (=relative synonymous codon usage)
    - is a measure of the deviation of the frequency of occurrence of a codon from the expected frequency, given the overall frequency of the corresponding amino acid in a sequence
    - (observed frequency of a codon)/(expected frequency of the codon)
    - RSCU value of 1 indicated that the observed frequency is equal to the expected frequency
        --> suggesting that there is no bias in the codon usage for that amino acid
    - RSCU value greater than 1 indicates that the observed frequency is higher than expected
    - RSCU value less than 1 indicated that the observed frequency is lower than expected 
    - In general, a codon usage bias value closer to 1 suggests that the codon usage for a particular amino acid is not strongly influenced by selective pressure, while values significantly greater or less than 1 suggest that there is selective pressure influencing codon usage.
'''                   









'''
------------------------------------------------------------------------------------------------------------------------------------------------
4. Nucleotide Composition
------------------------------------------------------------------------------------------------------------------------------------------------    
'''  
def NucComp(seq):
    composition = {
        'A':0,
        'C':0,
        'G':0,
        'T':0
    }  
    for nucleotide in seq:
        composition[nucleotide] += 1
    return composition

#print('Nucleotide Composition: ', NucComp(seq))


'''
------------------------------------------------------------------------------------------------------------------------------------------------
5. Consensus sequences
------------------------------------------------------------------------------------------------------------------------------------------------    
'''    
def consensus_sequence(file):
    sequences = []
    with open(file, 'r') as f:
        for seq in f:
            sequences.append(seq)
    
    consensus_counts = {'A':[], 'C':[], 'G':[], 'T':[]}
    
    for i in range(200):
        pos_counts = {'A':0, 'C':0, 'G':0, 'T':0}
        
        # counting nucleotides at the current position in each sequence
        for sequence in sequences:
            if sequence[i] != 'N':
                pos_counts[sequence[i]] += 1     
            
        # adding counts for the current position to the total counts
        for nucleotide in ['A', 'C', 'G', 'T']:
            consensus_counts[nucleotide].append(pos_counts[nucleotide])
    
    consensus = ''
    for i in range(len(consensus_counts['A'])):
        max_count = max(consensus_counts[nucleotide][i] for nucleotide in ['A', 'C', 'G', 'T']) 
        consensus_nucleotide = [nucleotide for nucleotide in ['A','C','G','T'] if consensus_counts[nucleotide][i] == max_count][0]   
        
        consensus += consensus_nucleotide
    return consensus             
             
     
'''file = '/media/big_hdd/group_1_bioinfo/Bsc/Human_don_train.pos' 
consensus = consensus_sequence(file)
print(consensus)'''



'''
------------------------------------------------------------------------------------------------------------------------------------------------
6. Intron Types
------------------------------------------------------------------------------------------------------------------------------------------------    
'''  



'''
------------------------------------------------------------------------------------------------------------------------------------------------
7. RNA Secondary structure
------------------------------------------------------------------------------------------------------------------------------------------------    
The formation of RNA secondary structure can affect splice site prediction accuracy by hindering the accessibility of splice sites to the splicesome
'''  


import subprocess
from Bio.Seq import Seq

def RNAsecond(sequence):
    sequence = Seq(sequence)
    rna_seq = sequence.transcribe()
    command = ['RNAfold', '-noPS', '-i', f'<(echo {rna_seq})']
    result = subprocess.check_output(command, shell=True, text=True)
    output = result.strip().split('\n')
    rna_structure = output[1].split()[0]
    return rna_structure

'''sequence = 'GACCTGTACGACTCTGGCCATGGGGAACAGCCACTGTGTCCCTCAGGCCCCCAGGAGGCTCCGGGCCTCCTTCTCCAGAAAGCCCTCGCTGAAGGGAAACAGGTGAGCGGGGCGTGGGTGCGGCCACCTGGGCGCAGGGCTCCCCCACCCGCTCCGGGGCCAAGCCACGAGACCCCTTGCCTTGTCCCCAGAGAGGACAG'
print(RNAsecond(sequence))'''