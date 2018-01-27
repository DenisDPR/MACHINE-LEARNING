
#!/usr/bin/python
from feature_format import featureFormat
from feature_format import targetFeatureSplit

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

feature_list = ["poi", "total_payments"] 
data_array = featureFormat( enron_data, feature_list)
label, features = targetFeatureSplit(data_array)
len(features)
