# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:32:48 2020

@author: Student 201386558
Univeristy of Leeds

Class containing:
    A method to initialise the agents initial position
    A Move method, to randomly move the agent 1 postion
    An Eat method to subtract from an input dataset and store the values 
    A method to search set distance surroundings for other agents
    A method to share stores with agents
    
    Function to return the string representation of the agents postiton object
    
    Properties to protect the self.x & self.y variables with get and set method
"""


import random


class Agent():


    def __init__(self, environment, agents, y, x):
        ''' 
        Initialise the Agent object.
        
        Positional arguments:
            environment - a matrix for the agents to interact with.
            agents - a list of all agents.
            y - the int coordinate for the Y axis for agent.
            x - the int coordinate for the Y axis for agent.
        '''
        if (x == None):
            # If input x is empty create random 
            self._x = random.randint(0, 100)
        else:
            self._x = x
        if (y == None):
            # If input y is empty create random 
            self._y = random.randint(0, 100)
        else:
            self._y = y
        self.environment = environment
        self.store = 0
        self.agents = agents
 

    def __str__(self):
        '''
         Provides a string object for agents position.
         
         Returns:
             Description of agents postion as X & Y and their store supplies.
        '''
        return "x=" + str(self._x) + " y=" + str(self._y) + " store has " + str(self.store)


    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    def getx(self):
        return self._x
    
    def setx(self, value):
        self._x = value
  

    @property
    def y(self):
        """I'm the 'y' property."""
        return self._y

    def gety(self):
        return self._y
    
    def sety(self, value):
        self._y = value


    def move(self):
        '''
        Move the agents X & Y one step randomly.
        '''
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100
            
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100
            
            
      
    def eat(self):
        '''
        Agents store take 10 pieces of the environment
        from their location or whatever is left if less than 10.
        '''
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
        else:
            self.store += self.environment[self._y][self._x]
            self.environment[self._y][self._x] = 0
  
    
    ''' Check nearby for nearby agents and share store if close '''       
    def share_with_neighbours(self, neigbourhood):
        '''
        Locate other agents within a neighbourhood range and share stores.
        
        Positional argument:
            neighbourhood - distance of the neighbourhood.
        '''
        #print(neigbourhood)
        for agent in self.agents:
            if(self != agent):  # Dont check distance with themself
                dist = self.distance_between(agent)
                if dist <= neigbourhood:
                    sum = self.store + agent.store
                    ave = sum /2
                    self.store = ave
                    agent.store = ave
                    #print(self, "sharing with", agent, 
                    #   "as we are", str(dist), "apart")
            else:
               pass  

      
    def distance_between(self, agent):
        '''
        Use pythag math to calculate distance between self and another agent.
        
        Positional argument:
            agent - an agent from a list.
            
        Returns:
            A float distance between the two agents.
        '''
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
