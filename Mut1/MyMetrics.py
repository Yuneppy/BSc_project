from sklearn.metrics import confusion_matrix
def MyMetrics(true, pred):
    tn, fp, fn, tp = confusion_matrix(true, pred).ravel()

    specificity = tn/(tn+fp)
    sensitivity = tp/(tp+fn)

    f1 = 2*tp/(2*tp+fp+fn)

    mcc = ((tp*tn)-(fp*fn))/((tp+fp)*(tp+fn)*(tn+fp)*(tn+fn))**0.5

    return specificity, sensitivity, f1, mcc



    


