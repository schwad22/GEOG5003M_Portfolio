# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:32:48 2020

@author: Student 201386558
Univeristy of Leeds

Class containing:
    A method to initialise the agents initial position
    A Move method, to randomly move the agent 1 postion
    An Eat method to subtract from an input dataset and store the values 

    A function to return the string representation of the agents postiton object
    
    Properties to protect the self.x & self.y variables with get and set methods
"""

# Import the required modules for this class
import random

# Create the class
class Agent():
    
    ''' Initialise the Agent object '''
    def __init__(self, environment):
        self._x = random.randint(0,99)
        self._y = random.randint(0,99)
        self.environment = environment
        self.store = 0
     
        
    ''' Convert self x and y object to a string '''
    def __str__(self):
        return "x=" + str(self._x) + " y=" + str(self._y) + " store has " + str(self.store)
     
        
    ''' Create a property to protect the self.x variable '''   
    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    def getx(self):
        return self._x
    
    def setx(self, value):
        self._x = value
        
        
    ''' Create a property to protect the self.y variable '''  
    @property
    def y(self):
        """I'm the 'y' property."""
        return self._y

    def gety(self):
        return self._y
    
    def sety(self, value):
        self._y = value
   
    
    ''' Method to move the input agents posistion one space randomly '''  
    def move(self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100
            
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100
            
            
    ''' Method to eat the environment at agents location '''        
    def eat(self):
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
        else:
            # Only needed when more than 2000 moves
            self.store += self.environment[self._y][self._x]
            self.environment[self._y][self._x] = 0