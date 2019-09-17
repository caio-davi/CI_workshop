## Importing Libraries
import pandas as pd
from sklearn import tree, metrics, svm
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.model_selection import StratifiedShuffleSplit
import numpy as np

# Importing dataset
original = pd.read_csv('disease.csv', header=0)

# Creating dataframes for features and classification
snps = original.drop('diagnosis', 1)
diag = original.loc[:,['diagnosis']]

# Normalizing data
for feature in snps.columns:
	df_coded = snps 
	setattr(df_coded, feature, getattr(snps,feature).astype("category").cat.codes)

# creating the crossvalidator 
cv = StratifiedShuffleSplit(n_splits=1, test_size=0.20, random_state=2**10)


for train, test in cv.split(snps, diag):

#   Setting training data
    df_train = snps.loc[train]
    diag_train = diag.loc[train]
    
#   Setting Test data
    df_test  = snps.loc[test]
    diag_test  = diag.loc[test]

### Choosing a classifier

#    clf = SGDClassifier(loss="hinge", penalty="l2", max_iter=5)
#    clf = svm.SVC(gamma='scale', decision_function_shape='ovo')
#    clf = tree.DecisionTreeClassifier(criterion='entropy')
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(8, 5))
#    clf = RandomForestClassifier(n_estimators=100)
#    clf = AdaBoostClassifier(n_estimators=100)
#    clf = NearestCentroid()

#   Training the Classifier:
    clf.fit(df_train,diag_train.pop('diagnosis').tolist())

#   Predicting the test dataset:
    predicted = clf.predict(df_test)

#   Formating before comparing 
    diag_test = diag_test.pop('diagnosis').tolist()

    print("Accuracy: ", metrics.accuracy_score(diag_test, predicted))
    print("Confusion Matrix: \n", metrics.confusion_matrix(diag_test, predicted))
    print("Classifier: ", clf  ) 
