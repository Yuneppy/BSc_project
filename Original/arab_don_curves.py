import InputReader as ipr
import Network as ntw
import tensorflow as tf
import MyMetrics as mm
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_recall_curve, auc
plt.ion()


trainX, trainY = ipr.InputReader('/media/big_hdd/group_1_bioinfo/Bsc/DataSet/Arab_SpliceSite/train.pos', '/media/big_hdd/group_1_bioinfo/Bsc/DataSet/Arab_SpliceSite/train.neg')
testX, testY = ipr.InputReader('/media/big_hdd/group_1_bioinfo/Bsc/DataSet/Arab_SpliceSite/test.pos', '/media/big_hdd/group_1_bioinfo/Bsc/DataSet/Arab_SpliceSite/test.neg')
validX, validY = ipr.InputReader('/media/big_hdd/group_1_bioinfo/Bsc/DataSet/Arab_SpliceSite/valid.pos', '/media/big_hdd/group_1_bioinfo/Bsc/DataSet/Arab_SpliceSite/valid.neg')

model = tf.keras.models.load_model('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/arab_donor.h5')

# evaluate the model on the test set
test_loss, test_acc = model.evaluate(testX, testY)

# predict the class probabilities for the test set
y_pred_prob = model.predict(testX)
# get the predicted class labels
y_pred = np.argmax(y_pred_prob, axis=1)
# get the true class labels
y_true = np.argmax(testY, axis=1)

precision, recall, thresholds = precision_recall_curve(y_true, y_pred_prob[:,1])
auprc = auc(recall, precision)

plt.plot(recall, precision, label='AUPRC (area = %0.2f)' % auprc)
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.legend(loc='lower left')
plt.savefig('/media/big_hdd/group_1_bioinfo/Bsc/shared_YS_JB/YSE/arab_donor_auprc.png')