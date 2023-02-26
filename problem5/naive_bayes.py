#-------------------------------------------------------------------------
# AUTHOR: Joseph Luna
# FILENAME: naive_bayes.py
# SPECIFICATION: runs bayes naive algorithm on training data with test data from csv
# FOR: CS 4210- Assignment #2
# TIME SPENT: ~30 minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv
import math


db = []

#reading the training data in a csv file
with open('weather_training.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        #print(i)
        if i > 0: #skipping the header
            db.append(row[1:6])

#print(db)

#transform the original training features to numbers and add them to the 4D array X.
#For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
mappings = []
X=[]
for x in range(len(db[0])):
    mappings.append(dict())
counter = 1
for row in db:
    index = 1
    newObj = []
    for item in row[:-1]:
        if item in mappings[index - 1]:
            newObj.append(mappings[index - 1][item])
        else:
            mappings[index - 1][item] = len(mappings[index - 1]) + 1
            newObj.append(mappings[index - 1][item])
            counter += 1
        index += 1
    X.append(newObj)
#print(X)
# X =

#transform the original training classes to numbers and add them to the vector Y.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
labels = dict()
labels["Yes"] = 1
labels["No"] = 2
counter = 1
Y = []
for row in db:
    item = row[-1]

    if item in labels:
        Y.append(labels[item])
    else:
        labels[item] = counter
        Y.append(labels[item])
        counter += 1
#print(Y)
# Y =

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)


dbTest = []
#reading the test data in a csv file
with open('weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        #print(i)
        if i > 0: #skipping the header
            dbTest.append(row[1:6])

#print(dbTest)
#print(len(dbTest))

Z = []
#print(mappings)
unmapped = []
counter = 1
for row in dbTest:
    index = 1
    newObj = []
    #print(row[0:4])
    index = 0
    unmapped.append(row)
    for item in row[0:4]:
        newObj.append(mappings[index][item])
        index += 1
    Z.append(newObj)
#print(Z)

#printing the header os the solution
print("{:<5} {:<10} {:<10} {:<10} {:<11} {:<11}".format("Day", "Outlook", "Humidity", "Wind", "PlayTennis", "Confidence"))

#use your test samples to make probabilistic predictions. For instance:
index = 15
#print(unmapped)
for testItem in Z:
    prediction = clf.predict_proba([testItem])[0]
    item = unmapped[index-15]
    doPrint = False
    if prediction[0] >= 0.75:
        doPrint = True
        classify = "Yes"
        predInd = 0
    elif prediction[1] >= 0.75:
        doPrint = True
        classify = "No"
        predInd = 1

    if doPrint:
        print("{:<5} {:<10} {:<10} {:<10} {:<11} {:<11}".format(f"D{index}", item[0], item[1], classify, item[3], round(prediction[predInd], 2)))


    index += 1
