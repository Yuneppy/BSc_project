import tensorflow as tf
import numpy as np

# import os

# tf.compat.v1.disable_eager_execution()

#tf.debugging.set_log_device_placement(False)
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
#os.environ['CUDA_VISIBLE_DEVICES'] = '1'
#os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'

def onehot(seq):
    seq2=[]
    mapping = {"A":[1., 0., 0., 0.], "C": [0., 1., 0., 0.], "G": [0., 0., 1., 0.], "T":[0., 0., 0., 1.], "N":[0., 0., 0., 0.]}
    for i in seq:
      seq2.append(mapping[i]  if i in mapping.keys() else [0., 0., 0., 0.]) 
    return np.array(seq2)


def InputReader(pos_file, neg_file):
    pos = []
    neg = []
    with open(pos_file, 'r') as f:
      pos = [onehot(line.rstrip()) for line in f]
    with open(neg_file, 'r') as f:
      neg = [onehot(line.rstrip()) for line in f]

    Y = [1] * len(pos)
    Y.extend([0] * len(neg))

    pos.extend(neg)
    
    X = np.array(pos)
    Y = np.array(Y)
    

    xval = X.reshape(-1,200,4)
    yval = tf.keras.utils.to_categorical(Y, num_classes=2)
    
   
    return xval, yval

#print(InputReader('/media/big_hdd/group_1_bioinfo/Bsc/DataSet/h_acc_ss_train.pos', '/media/big_hdd/group_1_bioinfo/Bsc/DataSet/h_acc_ss_train.neg'))
