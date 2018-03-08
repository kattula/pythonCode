import csv
import os

inputCSVFile = 'outptut-121608.csv'
#inputCSVFile = 'swarna-output-120249.csv'




def comparisionOfTwoImagesObjects(originalList, predictedList):
    numberOfMatches = 0
    defaultDict = {
        'AC':0,
        'fan':0,
        'lamp':0,
        'sofa':0,
        'washing machine':0,
        'cupboard':0,
        'frame':0,
        'mirror':0,
        'speaker':0,
        'window':0
        }
    for objectClass in originalList:
        #print(objectClass)
        defaultDict[objectClass] = defaultDict[objectClass] + 1
    for objectClass in predictedList:
        if defaultDict[objectClass] > 0:
            defaultDict[objectClass] = defaultDict[objectClass] - 1
            numberOfMatches = numberOfMatches + 1
    return numberOfMatches
    

if __name__== "__main__":

    totalNumberOfObjects = 0
    totalNumberofMatches = 0
    with open(inputCSVFile, "r") as inputFile:
        inputFileReader = csv.reader(inputFile)
        inputFileReader.next()
        for row in inputFileReader:
            originalImageObjects = row[3]
            predictedImageObjects = row[4]
            listOfOriginalImageObjects = originalImageObjects.split('$')
            listOfpredictedImageObjects = predictedImageObjects.split('$')
            totalNumberOfObjects = totalNumberOfObjects + len(listOfOriginalImageObjects)
            numberOfMatches = comparisionOfTwoImagesObjects(listOfOriginalImageObjects, listOfpredictedImageObjects)
            totalNumberofMatches = totalNumberofMatches + numberOfMatches
    accuracy = (totalNumberofMatches * 100) / totalNumberOfObjects
    print(totalNumberOfObjects)
    print(totalNumberofMatches)
    print(accuracy)
    
