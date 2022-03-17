
#NOTE : These code takes huge time for execution so wait for the output :)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.svm import SVC


#read the data
data = pd.read_csv('spambase.data', header=None)


#seperate x and y
x = data.drop([57],axis='columns')
y = data.iloc[:,-1]

#split the training and testing set
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)   #test_size specifies size of testing dataset here 30% because we have been specified to use 70% of dataset for training

#Different C values for accuarcy measurements 
C_values = [1, 10, 100]
C1_values = [100, 1000, 10000]      #C1 is used specially for RBM kernel
#Store kernals in a list
kernals = ['linear', 'poly', 'rbf'] 



#linear kernel
for j in C_values:
    model = svm.SVC(C=j,kernel='linear')           #We define model for every kernel
    model.fit(x_train, y_train)                 # .fir is a method used to train the model using training data 
    print(model.score(x_test, y_test))     #score on testing the model on testing dataset

#polynomial kernel
for j in C_values:
    model = svm.SVC(C=j, kernel='polynomial', degree = 2) #degree refers to the highest degree of the polynomial here 2 is used for quadratic kernel.
    model.fit(x_train, y_train)
    print(model.score(x_test, y_test))

#Radial- basis function
for j in C1_values:
    model = svm.SVC(C=j, kernel='rbf')
    model.fit(x_train, y_train)
    print(model.score(x_test, y_test))
