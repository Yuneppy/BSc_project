

'''
This file contains all possible biological features that differentiate Arabidopsis and Human
'''

'''
-----------------------------------------------------------------------------
1. Intron length
-----------------------------------------------------------------------------
'''

'''
This function takes a sequence as an input and returns the intron found within the sequence
'''    
def find_introns(sequence):

    # set a list called ‘CTNA’ containing four specific sequence
    # these sequences are consensus motif detected by SpliceRover within 
    intorn
    CTNA = ['CTAA', 'CTCA', 'CTGA', 'CTTA']


    # initialize two empty lists
    # introns contain all the intron candidates
    # new_intron contains only the correct or the most likely intron
    introns = []
    new_intron = []

    # if the file is donor datasets
    if sequence[99] == 'G':

        # since for donor dataset, intron begins right after the splice site
        for i in range(101,200):
            # since intron ends with ‘AG’, if AG sequence exist after donor site, regard them all as candidate introns
            if sequence[i:i+2] == 'AG':         
                introns.append(sequence[101:i]) 

        # identify the genuine intron among candidates
        for j in range(len(introns)):
        # if the intron contains one of the motif among CTNA list, then append that intron into new_intron list
            for k in range(len(CTNA)):
                if CTNA[k] in introns[j]:
                    new_intron.append(introns[j])


    # if the file is acceptor datasets        
    else:
        # since for donor dataset, intron ends right before the acceptor site
        for i in range(97):
            # since intron starts with ‘GT’, if GT sequence exist before acceptor site, regard them all as candidate introns
            if sequence[99-i-2:99-i] == 'GT':
                introns.append(sequence[99-i:99])

        # identify the genuine intron among candidates
        for j in range(len(introns)):
        # if the intron contains one of the motif among CTNA list, then append that intron into new_intron list
            for k in range(len(CTNA)):
                if CTNA[k] in introns[j]:
                    new_intron.append(introns[j])     
 
    # if “new_intron” list is not empty, return the shortest intron 
    # ‘min’ function and ‘key=len’ parameter sorts based on the length  
    if new_intron:
        return min(new_intron, key=len)

    # if “new_intron” list is empty, but introns list is not empty, return the shortest intron from “introns” list
    if introns:
        return min(introns, key=len)
    
    # if “new_intron” and “introns” lists are both empty, return empty string
    return ""  
 

'''
This function takes a sequence as an input and returns the length of the intron, found within the sequence.
It utilized the previously defines ‘find_introns” function.
'''    

def IntronLength(sequence):
    return len(find_introns(sequence))



'''
This function takes a file as an input and reads the sequences from the file, and return three statistical values: mean, median, and standard deviation.
'''    

import statistics
def AverageLength(file):
    sequence_list = []    # contains the sequences read from the file
    len_intron = []       # contains the intron lengths

    # open input file, and append all the sequences without whitespaces
    with open(file, 'r') as f:
        for seq in f:
            sequence_list.append(seq.strip())

    # iterate over each sequence in the sequence_list
    for sequence in sequence_list:
        # call pre-created IntronLength to calulate intron length, and append to the list containing each intron length of all sequences in a file
        len_intron.append(IntronLength(sequence))     
    
    # from the ‘statistics’ module, mean, median, and standard deviation was 
    obtained
    mean_len_intron = statistics.mean(len_intron)
    median_len_intron = statistics.median(len_intron)
    std_len_intron = statistics.stdev(len_intron)

                                       
'''
-----------------------------------------------------------------------------
2. GC content (entire sequence)
----------------------------------------------------------------------------- 
'''
'''
This function takes a sequence as an input and returns the gc-content. It is the percentage of nucleotides in a sequence that are either guanine (G) of cytosine (C)
'''      
def gc_content(seq):
    # count the occurrences of ‘G’ or ‘C’, and sum in gc_count
    gc_count = seq.count('G') + seq.count('C')

    # if there is no ‘G’ or ‘G’ in a sequence, return 0 as the gc-content
    if gc_count == 0:
        return 0
    # calculate the gc-content by dividing gc_count by the sequence length
    else:
        return gc_count/len(seq)
'''
This function takes a file as an input and returns the statistical measures for GC-content for whole sequences in a file. It utilized the pre-created ‘gc_content’ function and the ‘statistics’ module
'''      
import statistics
def average_gc(file):
    # create an empty list to contain each gc-content of every sequqence
    gc_total = []
    # open the input file in read mode
    with open(file, 'r') as f:
        # iterate over each sequence in the file
        for seq in f:
            # calculate gc-content of the sequence using gc_content function
            # append gc-content to the ‘gc_total’ list
            gc_total.append(gc_content(seq))

    # using ‘statistics’ module, calculate statistic data
    mean_gc = statistics.mean(gc_total)
    median_gc = statistics.median(gc_total)
    std_gc = statistics.stdev(gc_total)
    

'''
-----------------------------------------------------------------------------
3. GC content (within intron)
----------------------------------------------------------------------------- 
'''
'''
This function takes a file as an input and returns the statistical measures for GC-content within intron in a file. It utilized the pre-created ‘gc_content’ function and the ‘statistics’ module
'''      
import statistics
def gc_intron(file):
    # create an empty list to contain GC content within introns
    gcIntron = []
    # open the input file
    with open(file, 'r') as f:
        # iterate over each sequence in the file
        for seq in f:
            # calculate gc content within introns using gc_content function
            gcIntron.append(gc_content(find_introns(seq.strip())))

    # calculate statistics: mean, median, standard deviation
    mean_gcIntron = statistics.mean(gcIntron)
    median_gcIntron = statistics.median(gcIntron)
    std_gcIntron = statistics.stdev(gcIntron)



'''
-----------------------------------------------------------------------------
4. Nucleotide Composition
-----------------------------------------------------------------------------  
'''  
'''
This function takes a sequence as an input and returns nucleotide composition
'''      
def NucComp(seq):
    # create a dictionary to collect the counts of each nucleotide
    composition = {'A':0,'C':0,'G':0,'T':0,'N':0}  
    # iterate over each nucleotide in the sequence
    for nucleotide in seq:
        if nucleotide in ['A','G','C','T','N']:    # count up each nucleotide
            composition[nucleotide] += 1
    return composition

'''
-----------------------------------------------------------------------------
5. Consensus sequences
----------------------------------------------------------------------------- 
'''  
'''
This function takes a file as an input and returns consensus sequence
'''      
  
def consensus_sequence(file):
    # create an empty list to collect sequences
    sequences = []
    # open the input file in read mode
    with open(file, 'r') as f:
        # iterate over each sequence in the file
        for seq in f:
            sequences.append(seq)
    
    # create a dictionary to collect the counts of each nucleotide at each 
    position
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

    # initialize an empty string to store the consensus sequence
    consensus = ''

    # iterate over the positions of the consensus counts
    for i in range(len(consensus_counts['A'])):

        # find the maximum count among nucleotides at the current position
        max_count = max(consensus_counts[nucleotide][i] for nucleotide in ['A', 'C', 'G', 'T']) 

        # find the nucleotides with the maximum count at the current position
        consensus_nucleotide = [nucleotide for nucleotide in ['A','C','G','T'] if consensus_counts[nucleotide][i] == max_count][0]   
        
        # add up the consensus sequence 
        consensus += consensus_nucleotide
    return consensus             
             
'''
-----------------------------------------------------------------------------
6. Motif before splice site
----------------------------------------------------------------------------- 
''' 
# import defaultdict  class from the collections module
from collections import defaultdict
def motif_frequency(file):
    # create defaultdict to collect the motif counts before the splice site 
    up_motif_counts = defaultdict(int)        # upstream

    # create defaultdicy to collect the motif counts after the splice site
    down_motif_counts = defaultdict(int)      # downstream

    # open the input file
    with open(file, 'r') as f:
        for seq in f:

            # extract the 3-mer motif before splice site
            up_motif = seq[96:99]      

            # extract the 3-mer motif after splice site  
            down_motif = seq[101:104]

            # add up motif count in both upstream and downstream
            up_motif_counts[up_motif] += 1
            down_motif_counts[down_motif] += 1
    
    # sort upstream motifs in descending order
    sorted_up_counts = sorted(up_motif_counts.items(), key=lambda x: x[1], reverse=True)
    # sort downstream motifs in descending order
    sorted_down_counts = sorted(down_motif_counts.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_up_counts, sorted_down_counts

