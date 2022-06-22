import glob
import os
import math
import cv2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Models from Scikit-Learn
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

# Model Evaluations
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import plot_roc_curve
from PyQt5 import QtGui, QtCore


import warnings
warnings.filterwarnings("ignore")

class traitClass:

    def __init__(self):
        self.alldata = pd.read_csv("dataSet/heart-disease.csv")
        self.shape = self.alldata.shape
        self.data = self.alldata.tail(self.shape[0]-15).reset_index(drop=True)
        self.data15 = self.alldata.head(15)
        self.X = self.data.drop("target", axis=1)
        self.y = self.data["target"]
        self.folds = 3
        self.data15_Pred = None

        self.knn = None

        self.svm = None

        self.dtree = None

        self.rforest = None

        self.data15_Pred = None

        self.addFields(self.data15, 1, "linear", 16, 31)

    def addFields(self, df1, k, name, mp, n):
        self.data15_Pred = None
        df = df1.copy()
        ###############
        self.knn = KNeighborsClassifier(n_neighbors=k)
        self.knn.fit(self.X, self.y)

        self.svm = SVC(kernel=name)
        self.svm.fit(self.X, self.y)

        self.dtree = DecisionTreeClassifier(max_depth=mp)
        self.dtree.fit(self.X, self.y)

        self.rforest = RandomForestClassifier(n_estimators=n)
        self.rforest.fit(self.X, self.y)

        ###############
        X = df.drop("target", axis=1)
        y_knn = self.knn.predict(X)
        y_svm = self.svm.predict(X)
        y_dtree = self.dtree.predict(X)
        y_rforest = self.rforest.predict(X)
        df["y_knn"] = y_knn
        df["y_svm"] = y_svm
        df["y_dtree"] = y_dtree
        df["y_rforest"] = y_rforest
        self.data15_Pred = df


    def traitement(self, l, k, name, mp, n):
        df = pd.DataFrame([l], columns=self.data.columns)
        self.addFields(df, k, name, mp, n)

        return self.data15_Pred["y_knn"][0],self.data15_Pred["y_svm"][0],self.data15_Pred["y_dtree"][0],self.data15_Pred["y_rforest"][0]


