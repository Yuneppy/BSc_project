import InputReader as ipr
import Network as ntw
import tensorflow as tf
import MyMetrics as mm
import numpy as np


from keras.callbacks import CSVLogger
csv_logger = CSVLogger('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/a_acc_training.log', separator=',', append=False)

trainX, trainY = ipr.InputReader('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_acc_train.pos', '/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_acc_train.neg')
testX, testY = ipr.InputReader('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_acc_test.pos', '/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_acc_test.neg')
validX, validY = ipr.InputReader('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_acc_valid.pos', '/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_acc_valid.neg')


#length = len(trainX[0])

#model = ntw.SpliceRover_Model(length)

#history = model.fit(trainX, trainY, epochs=50, batch_size=256, validation_data=(validX, validY), callbacks=[csv_logger])

#model.save('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_acceptor.h5')



model = tf.keras.models.load_model('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/Mutated_Sequences/Consensus_Sequence/arab_acceptor.h5')

#model.summary()

#results = model.evaluate(testX, testY)
#print("test loss, test acc:", results)

#predictions = model.predict(testX).astype('float')
#print("predictions shape:", predictions)



# evaluate the model on the test set
test_loss, test_acc = model.evaluate(testX, testY)

# predict the class probabilities for the test set
y_pred_prob = model.predict(testX)
# get the predicted class labels
y_pred = np.argmax(y_pred_prob, axis=1)
# get the true class labels
y_true = np.argmax(testY, axis=1)


specificity, sensitivity, f1, mcc = mm.MyMetrics(y_true, y_pred)

print("Specificity:", specificity)
print("Sensitivity:", sensitivity)
print("F1 score:", f1)
print("MCC:",mcc)

