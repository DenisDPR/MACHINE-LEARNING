#!/usr/bin/python

""" 
Use a Naive Bayes Classifier to identify emails by their authors
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

clf = GaussianNB()
fit = clf.fit(features_train,labels_train)

pred = clf.predict(features_test)
accuracy = accuracy_score(pred, labels_test)
print(accuracy)
    
#########################################################