# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:12:12 2020

@author: Student 201386558
Univeristy of Leeds

- Reads in data to create an environment
- Creates a number of agents based on user inpit
- Moves agents randomly a number of iterations from user input
- Agents colelct parts of environment as they move around
- Agents check surroundings for nearby agents and share stores
- Plots the positions of the agents as they move
- Environments changes are plotted as they agents 'nibble' it away
- Programme stops when number first agent stores 100 pieces of environment
or number of agents moves input by user are complete

"""

import matplotlib.pyplot, agentsFramework, csv, sys, random, matplotlib.animation

        
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


''' Move each agent, eating the environmentin one at a time 100 random positions using the Move
    method then eat 10 values from the environment at their position '''
carry_on = True
    
def update(frame_number):
    fig.clear()
    global carry_on
    if carry_on == True:
        #for j in range(num_of_iterations):
        random.shuffle(agents)
        for i in range(num_of_agents):
        #print(j, i)
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neigbourhood)
           
        # Stop when first agents get 100 in their store
        for i in range(num_of_agents):
            if (agents[i].store > 100):
                carry_on = False
                print(agents[i], "They win, Stopping Now!")
        # Plot the environment and in turn plot all agents for each iteration of moves
        matplotlib.pyplot.ylim(0, 99)
        matplotlib.pyplot.xlim(0, 99)
        matplotlib.pyplot.imshow(environment)   
        for i in range(num_of_agents):
            matplotlib.pyplot.scatter(agents[i].x, agents[i].y)


def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < num_of_iterations) & (carry_on) :
        yield a	# Returns control and waits next call.
        a = a + 1

''' Plot the agents positions in the 'nibbled' environment '''
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
# Move the agents, make them eat, share with neighbours and plot positions
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
#matplotlib.pyplot.ylim(0, 99)
#matplotlib.pyplot.xlim(0, 99)
#matplotlib.pyplot.imshow(environment) # Doesn't show with animation
matplotlib.pyplot.show()
