#This function takes a matrix description and creates a matrix based on this description.
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


#Performs multiplication between two matrices (a and b)
def Multiplication(a, b): 
    rows = len(a) #We get the rows from matrix 1 (a)
    columns = len(b[0]) #We get the colums from matrix 2 (b)
    result = [[0] * columns] * rows #We populate our new matrix with 0s
    for i in range(rows):
        for j in range(columns):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j] #standard matrix multiplication
    return result

def readInput():
    return [float(x) for x in input().split()]

def main():
    
    transitionMatrix = createMatrix(readInput())
    emissionMatrix = createMatrix(readInput())
    initialStateProbability = createMatrix(readInput())

    #We first calculate the other two matrices to later predict the relevant matrix (emission)
    firstMultiplication = Multiplication(initialStateProbability, transitionMatrix) 
    
    #Now we calculate the relevant matrix with the sum of the previous calculation
    Distribution = Multiplication(firstMultiplication, emissionMatrix)

    #Here we round up the resulting probabilities to three decimal places
    Distribution = [[round(elem, 3) for elem in row] for row in Distribution]

    #These lines is just for formatting and printing.
    probability = [item for sublist in Distribution for item in sublist]
    t_str_prob = ' '.join([str(l_elem) for l_elem in probability])
    print(str(len(Distribution)), str(len(Distribution[0])), t_str_prob)

if __name__ == "__main__":
    main()
