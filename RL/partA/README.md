# Random Agents
## Game Concept
In this assignment we take a look at the KTH fishing game. There is one player in this game who is a diver out at sea (see figure below). 
You are in command of the diver and your goal is to get the highest score possible, obtained through catching some fishes by avoiding others. 
The game is over whenever you catch the king fish.

![game](https://kth.kattis.com/problems/kth.ai.rl1/file/statement/en/img-0001.png)

## Gameplay specifics
The diver can move (UP, DOWN, LEFT, RIGHT). There are two types of fish in the game, jelly fish and one single gold fish. 
There are different (possibly negative) rewards associated with catching each type of fish. 
The fishes do not move. A fish is caught once its position coincides with the diver’s position. 
An episode of the game finishes when the king fish is caught.

The position of the fish is not known to the diver. 
At each time instance, the diver knows it’s own position and when they perform an action, they can observe the immediate reward. 
The diver goes through multiple episodes of the game with fixed fish positions and the goal for the student is to implement the code 
for the diver agent that allows it to find a policy that maximizes the reward in the game.

## Provided code
The code skeleton will be provided for you in Python. You should modify the player file player.py and you may also create new files. 
The files included in the skeleton, other than player.py, may be modified locally but keep in mind that they will be overwritten on Kattis. 
You only need to upload the player file, and of course any additional python files you have created.

Your implementation will be called to retrieve the policy that will be used to evaluate your agent in a given scenario. 
In each step of the learning algorithm, the skeleton queries the environment to receive the reward given the action. 
Be aware that the judge might sometimes also check different functions of the code. 
Therefore, you should not modify any function names or input arguments that are provided in the skeleton. Of course, you can extend the class.

The settings.yml also allows you to vary the use of the graphics interface (toggle visualize_exploration).

## Input
Your interface with the judge is the player file player.py. 
For this first problem, look for a PlayerControllerRandom class within player.py. 
You will edit the self.random_agent() method within the class. After editing player.py, rename it as player_1.py for submission.

A sample scenario is provided in the code skeleton (the settings.yml file). 
You are invited to vary the scenario by modifying the settings.yml to test your RL agent on different scenarios.

## Output
The skeleton handles all the output for you. Avoid using stdin and stdout. (Use stderr for debugging.)

You are able to test your random agent by executing: "python main.py settings.yml". You should be able to see messages printed on the standard output (see Figure below).

![test](https://kth.kattis.com/problems/kth.ai.rl1/file/statement/en/img-0002.png)
