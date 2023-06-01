def find_introns(sequence):
    introns = []
    CTNA = ['CTAA', 'CTCA', 'CTGA', 'CTTA']
    introns = []
    new_intron = []
    if sequence[99] == 'G':
        for i in range(101,200):
            if sequence[i:i+2] == 'AG':
                introns.append(sequence[101:i])
        for j in range(len(introns)):
            for k in range(len(CTNA)):
                if CTNA[k] in introns[j]:
                    new_intron.append(introns[j])
        
    else:
        for i in range(97):
            if sequence[99-i-2:99-i] == 'GT':
                introns.append(sequence[99-i:99])
        for j in range(len(introns)):
            for k in range(len(CTNA)):
                if CTNA[k] in introns[j]:
                    new_intron.append(introns[j])     
    
    if new_intron:
        return min(new_intron, key=len)
    if introns:
        return min(introns, key=len)
    return ""  
 
 

def IntronLength(sequence):
    return len(find_introns(sequence))


def AverageLength(file):
    sequence_list = []
    len_intron = []
    with open(file, 'r') as f:
        for seq in f:
            sequence_list.append(seq.strip())
    for sequence in sequence_list:
        len_intron.append(IntronLength(sequence))        
    return sum(len_intron)/len(len_intron)    
            
                        
                