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

import matplotlib.pyplot, agentsFramework

''' Function to calculates distance between 2 agents passed into function '''
def distance_between(agents_row_a, agents_row_b):
    distance = (((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2))**0.5
    return distance

# Create an empty agent list and set up user input variables
num_of_agents = 10
num_of_iterations = 100
agents = []

# Initialise the Agent object to add each agents position in the empty list 
for i in range(num_of_agents):
    agents.append(agentsFramework.Agent())
    

# Move each agent in one at a time 100 random positions using the Move method 
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        #print(j, i)
        agents[i].move()

# Calculate distance between agents 
for i in range(num_of_agents):
    for j in range(i, num_of_agents):
        if i != j:
            distance = distance_between(agents[i], agents[j])
            print(agents[i], agents[j], " are ", distance, "apart")
        else:
            pass

# Plot the agents positions 
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color='green')
matplotlib.pyplot.show()