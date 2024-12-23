def createMatrix(matrixDesc):
    
    matrixDescList = list(map(float, matrixDesc[2:])) #Make a list of the description starting from index 2 as floats
    matrixRows = int(matrixDesc[0]) #We determine the number of rows and columns from the first two elements
    matrixCols = int(matrixDesc[1])
    Matrix = []
    
    for i in range(matrixRows): #We iterate through the rows and columns to create the matrix
        rowList = []
        for j in range(matrixCols):
            if matrixDescList[j] not in Matrix: #A check for duplicates.
                rowList.append(matrixDescList[matrixCols * i + j])
        Matrix.append(rowList)
    return Matrix
    
    
#This function multiplies two lists element-wise using zip. 
def Multiplication(a, b):
    result = []
    for i in range(len(a)):
        result.append(a[i] * b[i])
    return result

#used to get a specific column from a matrix
def getCol(matrix, col):
    column = []
    for row in matrix:
        column.append(row[col])
    return column

#used to read input
def readInput():
    return [float(x) for x in input().split()]

transitionMatrix = createMatrix(readInput())
emissionMatrix = createMatrix(readInput())
initialStateProbability = createMatrix(readInput())

#a = [int(x) for x in input().split()]
observationSequence = [int(x) for x in input().split()[1:]] #Start from index 1

initialAlpha = Multiplication(initialStateProbability[0], getCol(emissionMatrix, observationSequence[0]))


def Forward(alpha, observationSeq):
    if len(observationSeq) == 0:
        print(round(sum(alpha), 6))
        return sum(alpha)
    firstTerm = [sum(Multiplication(alpha, getCol(transitionMatrix, i))) for i in range(len(transitionMatrix[0]))] #Length of states
    currentAlpha = Multiplication(firstTerm, getCol(emissionMatrix, observationSeq[0]))
    Forward(currentAlpha, observationSeq[1:])


Forward(initialAlpha, observationSequence[1:])
