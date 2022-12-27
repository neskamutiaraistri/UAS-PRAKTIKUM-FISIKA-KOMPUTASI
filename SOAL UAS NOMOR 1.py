import cv2
import numpy as np
import csv
import time

from sklearn import svm
import pandas as pd

#Database: Gerbang Logika AND
#Membaca data dari file
FileDB = 'database.txt'
Database = pd.read_csv(FileDB, sep=",",header=0)
print(Database)

#x = Data, y = Target
x = Database[[u'a',u'b',u'Target']]
y = Database.Target

clf = svm.SVC()
clf.fit(x,y)

print(clf.predict( [[1,2]] ))
print(clf.predict( [[2,3]] ))
print(clf.predict( [[3,4]] ))
print(clf.predict( [[4,5]] ))
