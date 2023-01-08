import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

print("Diabetes predictor using Decision Tree")

diabetes=pd.read_csv('diabetes.csv')
print("Columns of Dataset")
print(diabetes.columns)

print("First 5 records of dataset")
print(diabetes.head())

print("Dimensions of diabetes data : {} ".format(diabetes.shape))

X_train, X_test, y_train, y_test =train_test_split(diabetes.loc[:, diabetes.columns!='Outcome'],diabetes['Outcome'],stratify=diabetes['Outcome'],random_state=66)

tree=DecisionTreeClassifier(random_state=0)
tree.fit(X_train,y_train)

print("Accuracy on training set : {:.3f}".format(tree.score(X_train,y_train)))
print("Accuracy on training set : {:.3f}".format(tree.score(X_test,y_test)))

print("Feature importances :\n{}".format(tree.feature_importances_))

def plot_feature_importance_diabetes(model):
    plt.figure(figsize=(8,6))
    n_features=8
    plt.barh(range(n_features),model.feature_importances_,align='center')
    diabetes_features=[x for i, x in enumerates(diabetes.columns) if i!=8]
    plt.yticks(np.arrange(n_features), diabetes(features))
    plt.xlabel("Feature importance")
    plt.ylabel("Feature")
    plt.tlim(-1,n_features)
    plt.show()
    
    plot_feature_importances_diabetes(tree)
