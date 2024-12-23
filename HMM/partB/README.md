# Probability of Emission Sequence
In this task you should show that you know how to calculate the probability to observe a certain emission sequence given a HMM model. 
You will be given the HMM model and a sequence of observations (aka emissions, events, etc) and your task is to calculate the probability for this sequence.

## Input
You will be given three matrices; transition matrix, emission matrix, and initial state probability distribution 
followed by the number of emissions and the sequence of emissions itself. The initial state probability distribution is a row vector encoded as a matrix with only one row. 
Each matrix is given on a separate line with the number of rows and columns followed by the matrix elements (ordered row by row). 
Note that the rows and column size can be different from the sample input. 
It is assumed that there are M different discrete emission types and these are indexed 0 through M-1 in the emission sequence. 
For example, if there were M=3 possible different emissions (could be the three colours red, green and blue for example), 
they would be identified by 0, 1 and 2 in the emission sequence.

## Output
You should output the probability of the given sequence as a single scalar.

## Sample Input
```
4 4 0.0 0.8 0.1 0.1 0.1 0.0 0.8 0.1 0.1 0.1 0.0 0.8 0.8 0.1 0.1 0.0 
4 4 0.9 0.1 0.0 0.0 0.0 0.9 0.1 0.0 0.0 0.0 0.9 0.1 0.1 0.0 0.0 0.9 
1 4 1.0 0.0 0.0 0.0 
8 0 1 2 3 0 1 2 3
```
## Sample Output
```
0.090276
```
