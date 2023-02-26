#-------------------------------------------------------------------------
# AUTHOR: Joseph Luna
# FILENAME: knn.py
# SPECIFICATION: runs SKLearn's k nearest neighbor algorithm on CSV file provided for assignment
# FOR: CS 4210- Assignment #2
# TIME SPENT: ~1 hour
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []

#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

#print(db)

#loop your data to allow each instance to be your test set
index = 0
errors = 0
total = len(db)
for pt in db:

    #add the training features to the 2D array X removing the instance that will be used for testing in this iteration. For instance, X = [[1, 3], [2, 1,], ...]]. Convert each feature value to
    # float to avoid warning messages
    X = []
    index2 = 0
    for x in db:
        if not index == index2:
            X.append([float(x[0]), float(x[1])])
        index2 += 1
    # X =
    #print(X)

    #transform the original training classes to numbers and add to the vector Y removing the instance that will be used for testing in this iteration. For instance, Y = [1, 2, ,...]. Convert each
    #  feature value to float to avoid warning messages
    Y = []
    index2 = 0
    for y in db:
        if not index == index2:
            Y.append(1.0 if y[2] == '+' else 0.0)
        index2 += 1
    # Y =
    #print(Y)

    #store the test sample of this iteration in the vector testSample
    testSample = [float(pt[0]), float(pt[1])]
    #testSample =

    #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    #use your test sample in this iteration to make the class prediction. For instance:
    class_predicted = clf.predict([testSample])[0]
    #print(class_predicted)

    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #print(testSample)
    hasError = (class_predicted != (1.0 if pt[2] == '+' else 0.0))
    if hasError:
        errors += 1

    index += 1

#print the error rate
print(f"error rate: {errors/total}")






