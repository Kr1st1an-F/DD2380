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

observationSequence = [int(x) for x in input().split()[1:]] #Start from index 1

def viterbi(probabilities, states, observationSeq):
    
    if len(observationSeq) == 0: #backtrack to find the most likely sequence
        stateSequence = []
        lastState = probabilities.index(max(probabilities))
        stateSequence.append(lastState)
        for i in range(len(states) - 1, 0, -1):
            stateSequence.insert(0, states[i][lastState])
            lastState = states[i][lastState]

        print(' '.join(map(str, stateSequence)))
        return


    allProbabilities = [] #to hold the probabilites of all states
    for currState in range(len(transitionMatrix[1])): #Loop through all current state in the HMM
        probabilitiesCurrState = []
        for prevState in range(len(transitionMatrix[1])): #Loop through all previous state in the HMM
            #Calculating the probability, given by the lab assignment 
            prob = probabilities[prevState] * transitionMatrix[prevState][currState] * emissionMatrix[currState][observationSeq[0]]
            probabilitiesCurrState.append(prob)
        allProbabilities.append(probabilitiesCurrState)
    
    maxProbability = []
    for probabilitiesCurrState in allProbabilities:
        maxProbability.append(max(probabilitiesCurrState))
    
    stateIndices = []
    for i, probabilitiesCurrState in enumerate(allProbabilities):
        stateIndices.append(probabilitiesCurrState.index(maxProbability[i]))
        
    states.append(stateIndices)
    
    viterbi(maxProbability, states, observationSeq[1:])

probabilities = Multiplication(initialStateProbability[0], getCol(emissionMatrix, observationSequence[0]))

viterbi(probabilities, [len(transitionMatrix[0])], observationSequence[1:])
