"""
Tim Meek II
Created: 5/11/21
Last Updated: 5/13/21

The purpose of this program is to show all of the possible solutions
of how N people can cross a bridge in pairs with one of them returning
back to the original side until all people have successfully crossed.
This solution will use a brute force method of solving and will organize 
all possible combinations based on how long it took the group to 
successfully cross the bridge.
"""

import itertools    # use the combinations function from itertools
import matplotlib.pyplot as plt   # use to graph output data
import numpy as np

sideA = []          # list
crossingTimes = {}  # dictionary
sideB = []          # list
startingTime = 0    # int
solutions = []      # list

def findSolutions(sideA, sideB, solution, solutions, runningTime):
    if len(sideA) > 0:
        pairs = [] # will store all possible pairs that can cross together
        comb = itertools.combinations(sideA, 2) # iterator for the determined solutions

        # append all possible combinations of pairs to iterator
        for a, b in comb:
            pairs.append((a, b)) 

        # send each pair to crossBridge method
        for pair in pairs:
            crossBridge(sideA[:], sideB[:], pair, solution, solutions, runningTime)


# Move pair from sideA to sideB
def crossBridge(sideA, sideB, pair, solution, solutions, runningTime): 
    if len(sideA) > 0:
        sideA.remove(pair[0])     # remove from sideA
        sideA.remove(pair[1])
        sideB.append(pair[0])     # append to sideB
        sideB.append(pair[1])
        solution += str(pair[0]) + '+' + str(pair[1])   # add move to the solution list
        runningTime += max(crossingTimes[pair[0]], crossingTimes[pair[1]]) # add the time of the slowest person

        # Once all individuals have crossed all solutions and the total time are then stored in solutions list
        if len(sideA) == 0:
            solutions.append((solution, runningTime))
        for person in sideB:
            returnTorch(sideA[:], sideB[:], person, solution, solutions, runningTime)       
        

# Returns the torch back from sideB to sideA
def returnTorch(sideA, sideB, person, solution, solutions, runningTime):
    sideB.remove(person)
    sideA.append(person)
    solution += ',  ' + str(person) + ',  ' # add this move to the solution
    runningTime += crossingTimes[person]    # add persons crossing time to the running time
    findSolutions(sideA[:], sideB[:], solution, solutions, runningTime)     # repeat findSolutions with data


# !!! Data processed by the brute force algorithm goes here !!! #
sideA = ['A', 'B', 'C', 'D']  # Name of people need to cross bridge
crossingTimes = {'A':10, 'B':5, 'C':2, 'D':1} # How long each person takes to cross
sideB = [] # Original set of those who have already crossed, if any
startingTime = 0
solutions = []  # will store all possible solutions

# Call findSolutions function
findSolutions(sideA, sideB, '', solutions, startingTime)

# sort solutions from fastest to slowest using lambda function
sortedSolutions = sorted(solutions, key=lambda x: x[1])

# format output
solutionCount = 0
listOfTimes = []
outputSolution = ''
for solutions in sortedSolutions:
    solutionCount +=1
    outputSolution = 'Solution '+ str(solutionCount) +' =  [ '+ str(solutions[0]) +' ]'  # solutions[0] stores the string of how the individuals crossed
    print(outputSolution)
    print('     Time: ', solutions[1], 'min') # solutions[1] stores the int of how many minutes it took for that solution
    print('*'*(len(outputSolution)))
    listOfTimes.append(solutions[1])   # append data for histagram
    
# visualize output times as histogram
fig, ax = plt.subplots(figsize = (10, 5))
ax.hist(listOfTimes, bins=25, edgecolor="black");
plt.title("Distribution of Solutions by Time")
plt.xlabel("Time (min)")
plt.ylabel("Count")

# display median line
median_time = np.median(listOfTimes)
ax.axvline(median_time, color="black", ls="--", label="Median time")
ax.legend();