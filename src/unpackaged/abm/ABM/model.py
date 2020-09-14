# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 14:18:23 2020

@author: Student 201386558
Univeristy of Leeds

Creates an empty list, populates it with two agents at random positions.
Moves each agents randomly two times then calculates distance between agents
Plots final postitions on a scatter plot  
"""

import random, operator, matplotlib.pyplot

# Create empty list
agents = []

# Add first agent starting position to list
agents.append([random.randrange(99), random.randrange(99)])

# Move first agent randomly twice
if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1

if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1
    
if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1

if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1

# Add second agent starting position to list
agents.append([random.randrange(99), random.randrange(99)])   

# Move second agent randomly twice
if random.random() < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1

if random.random() < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1
    
if random.random() < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1

if random.random() < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1

# Calculate distance between agents 
print(max(agents, key=operator.itemgetter(1)))
pythag = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
print(agents[1][1], agents[1][0], agents[0][1], agents[0][0], pythag)

# Plot the agents positions 
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0], color='green')
matplotlib.pyplot.scatter(agents[1][1],agents[1][0], color='orange')
matplotlib.pyplot.show()