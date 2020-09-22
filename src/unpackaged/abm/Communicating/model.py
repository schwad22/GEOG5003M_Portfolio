# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:12:12 2020

@author: Student 201386558
Univeristy of Leeds

Reads in data to create an environment
Creates 10 agents
Moves them randomly 100 times
Agents store part environments each time they move
Calculates the finishing position of each agent
Plots the scavenged environment and agents final positions

"""

import matplotlib.pyplot, agentsFramework, csv, sys, random

''' Get input variables from the user and create an empty list '''
num_of_agents = int(sys.argv[1])
num_of_iterations = int(sys.argv[2])
neigbourhood = int(sys.argv[3])
agents = []


''' Open file, read data, add to values to environment list '''
environment = []
fOpen = open("in.txt")
read = csv.reader(fOpen, quoting=csv.QUOTE_NONNUMERIC)
# Loop though row of open csv
for row in read:
    rowList = []
    # Loop through values in row and append to rowList
    for values in row:
        rowList.append(values)
    # Append each list to environment list to create list of lists (matrix)
    environment.append(rowList)
fOpen.close()


''' Initialise the Agent object to add each agents
    position in the empty list ''' 
for i in range(num_of_agents):
    agents.append(agentsFramework.Agent(environment, agents))
#print("Agent 1 is ", agents[0], " and knows agent 2 is ", agents[1])


''' Move each agent in one at a time 100 random positions using the Move
    method then eat 10 values from the environment at their position '''
for j in range(num_of_iterations):
    random.shuffle(agents)
    for i in range(num_of_agents):
        #print(j, i)
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neigbourhood)


''' Plot the agents positions in the 'nibbled' environment '''
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color='red')
matplotlib.pyplot.show()
