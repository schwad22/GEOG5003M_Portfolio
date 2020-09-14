# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:12:12 2020

@author: Student 201386558
Univeristy of Leeds

Creates an empty list, populates it with ten agents at random positions.
Moves each agent in turn randomly 100 times
Uses a function to calculate distance between agents passed to it
Loops to pass two agents at a time to dstance function
Plots final postitions on a scatter plot  
"""

import random, matplotlib.pyplot, agentsFramework

# Function to calculates distance between 2 agents passed into function
def distance_between(agents_row_a, agents_row_b):
    distance = (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5
    return distance

# Create an empty agent list and 
num_of_agents = 10
num_of_iterations = 100
agents = []

# Create agents 
for i in range(num_of_agents):
    agents.append([random.randint(0,99), random.randint(0,99)])

# Move each agent in turn by one position 100 times 
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        #print(j, i)
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100

# Calculate distance between agents 
for i in range(num_of_agents):
    for j in range(i, num_of_agents):
        if i != j:
            distance = distance_between(agents[i], agents[j])
            print(agents[i], agents[j], " are ", distance, "apart")
        else:
            pass
'''
print(max(agents, key=operator.itemgetter(1)))
pythag = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
print(agents[1][1], agents[1][0], agents[0][1], agents[0][0], pythag)
'''

# Plot the agents positions 
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0], color='green')
matplotlib.pyplot.show()