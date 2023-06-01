import InputReader as ipr
import Network as ntw
import tensorflow as tf
import MyMetrics as mm
import numpy as np


from keras.callbacks import CSVLogger
csv_logger = CSVLogger('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/a_acc_training.log', separator=',', append=False)

trainX, trainY = ipr.InputReader('/media/big_hdd/group_1_bioinfo/Bsc/DataSet/Acceptor_splice_site/arab/acc_ss_train.pos', '/media/big_hdd/group_1_bioinfo/Bsc/DataSet/Acceptor_splice_site/arab/acc_ss_train.neg')
testX, testY = ipr.InputReader('/media/big_hdd/group_1_bioinfo/Bsc/DataSet/Acceptor_splice_site/arab/acc_ss_test.pos', '/media/big_hdd/group_1_bioinfo/Bsc/DataSet/Acceptor_splice_site/arab/acc_ss_test.neg')
validX, validY = ipr.InputReader('/media/big_hdd/group_1_bioinfo/Bsc/DataSet/Acceptor_splice_site/arab/acc_ss_valid.pos', '/media/big_hdd/group_1_bioinfo/Bsc/DataSet/Acceptor_splice_site/arab/acc_ss_valid.neg')


#length = len(trainX[0])

#model = ntw.SpliceRover_Model(length)

#history = model.fit(trainX, trainY, epochs=50, batch_size=256, validation_data=(validX, validY), callbacks=[csv_logger])

#model.save('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/arab_acceptor.h5')

'''import matplotlib.pyplot as plt
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(['Train','Test'], loc='upper left')
plt.show()'''

#model = tf.keras.models.load_model('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/arab_acceptor.h5')

#model.summary()

#results = model.evaluate(testX, testY)
#print("test loss, test acc:", results)

#predictions = model.predict(testX).astype('float')
#print("predictions shape:", predictions)


model = tf.keras.models.load_model('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/arab_acceptor.h5')

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


