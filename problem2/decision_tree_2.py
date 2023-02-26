#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']
index4 = 0
for ds in dataSets:

    dbTraining = []
    X = []
    Y = []

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)

    #transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    # so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    mappings = []
    for x in range(len(dbTraining[0])):
        mappings.append(dict())
    counter = 1
    for row in dbTraining:
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
    # X = [[1, 1, 1, 1], [1, 2, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [2, 2, 2, 2], [2, 2, 1, 1], [3, 1, 1, 1], [3, 2, 1, 1]]
    #transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    labels = dict()
    counter = 1
    corrects = 0
    total = 0
    for row in dbTraining:
        #print(row)
        item = row[-1]
        #print(item)

        if item in labels:
            Y.append(labels[item])
        else:
            labels[item] = counter
            Y.append(labels[item])
            counter += 1
    #print(Y)
    # Y = [1, 1, 2, 2, 2, 2, 1, 2]

    #loop your training and test tasks 10 times here
    index2 = 0
    accuracy = 0
    for i in range(10):


        if i == 5:
            index2 = 0
        elif i > 5:
            start = 0
        else:
            start = 1

        xNew = X[start:(index2+2)][(index2+2):]
        yNew = Y[start:(index2 + 2)][(index2 + 2):]
        index2 += 1

        #fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3)
        clf = clf.fit(X, Y)

        #read the test data and add this data to dbTest
        dbTest = []
        testTruth = []
        with open('contact_lens_test.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i > 0:  # skipping the header
                    mapped = []
                    index = 0
                    for item in row[0:4]:
                        mapped.append(mappings[index][item])
                        index += 1
                    testTruth.append(2 if row[4] == "Yes" else 1)
                    dbTest.append(mapped)
        #print(dbTest)
        # dbTest =
        index3 = 0
        total = len(dbTest)
        for data in dbTest:
            pass
           #transform the features of the test instances to numbers following the same strategy done during training,
           #and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
           #where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
            class_predicted = clf.predict([data])[0]

           #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
            #print(f"testing equality... found: {class_predicted == testTruth[index3]} ")
            if class_predicted == testTruth[index3]:
                corrects += 1
            index3 += 1
    index4 += 1
    print(f"average for dataset {index4}: {corrects/(total*10)}")
    #find the average of this model during the 10 runs (training and test set)
    #--> add your Python code here

    #print the average accuracy of this model during the 10 runs (training and test set).
    #your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    #--> add your Python code here




