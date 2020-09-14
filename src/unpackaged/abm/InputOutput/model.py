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

import matplotlib.pyplot, agentsFramework, csv


''' Function to calculates distance between 2 agents passed into function '''


def distance_between(agents_row_a, agents_row_b):
    distance = (((agents_row_a.x - agents_row_b.x)**2) + 
                ((agents_row_a.y - agents_row_b.y)**2))**0.5
    return distance


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


''' Create an empty agent list and set up input variables '''
num_of_agents = 10
num_of_iterations = 100
agents = []


''' Initialise the Agent object to add each agents
    position in the empty list ''' 
for i in range(num_of_agents):
    agents.append(agentsFramework.Agent(environment))


''' Move each agent in one at a time 100 random positions using the Move
    method then eat 10 values from the environment at their position '''
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        #print(j, i)
        agents[i].move()
        agents[i].eat()


''' Calculate distance between agents by calling function '''
for i in range(num_of_agents):
    for j in range(i, num_of_agents):
        # Dont check distance to self
        if i != j:
            distance = distance_between(agents[i], agents[j])
            print(agents[i], agents[j], " are ", distance, "apart")
        else:
            pass


''' Plot the agents positions in the 'nibbled' environment '''
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color='red')
matplotlib.pyplot.show()
