# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 16:36:52 2022

@author: clambert

agentframework9 relateds to the "GUI-Webscraping" practical and should be used with 
the model9 and the csvreader9 files.

in.txt is the input data for the csvreader9 file and should be stored in the same directory

Directions:
1. Save model9, agentframework9, in.txt and csvreader9 in the same directory location
2. Run model9
"""

#Imported modules
import random


#Define "Agent" class
class Agent():

    #generate random x & y values and the environment and agents vaiables
    def __init__(self, environment, agents):
        """
        Parameters
        ----------
        environment :
            __init__ creates random starting values for x & y between 
            0 and 99 and provides the environment and agents attributes

        Returns
        -------
        random starting values

        """
        self.environment = environment #defining environment
        self.agents = agents #defining agents
        self.store = 0
        self.x = random.randint (0,99) #random values for x
        self.y = random.randint (0,99)  #random values for y
    
    #moves the agents 
    def move (self):
        """
        move takes the values generated in __init__ and moves them one step

        Returns
        -------
        Returns new values moved by one step

        """
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:       
            self.y = (self.y - 1) % 100
    
    # eats into enviroment based on values
    def eat(self):
         """
         eats into enviroment if values are > 10
         
         Returns
         -------
         values in environment based on the subtraction assignment

         """
         if self.environment[self.y][self.x] > 10:
             self.environment[self.y][self.x] -= 10
             self.store += 10  

    #shares agents positions with neighbouring agents
    def share_with_neighbours(self, neighbourhood):
         """
         Parameters
         ----------
         neighbourhood : number
             defines distance between agent pairs

         Returns
         -------
         straight line dstance between agent pairs

         """
         for agent in self.agents:
             dist = self.distance_between(agent)
         if dist <= neighbourhood:
             sum = self.store + agent.store
             ave = sum /2
             self.store = ave
             agent.store = ave
             print("sharing " + str(dist) + " " + str(ave))

    #calcualting distance between agents
    def distance_between(self, agent):
        """
        Calculates and returns the 2D coordinate distance between a and b.

        Parameters
        ----------
        a : Agent
            Located in 2D space with an x and y cordinate values.
        b : Agent
            Located in 2D space with an x and y cordinate values.

        Returns
        -------
        Number
            The 2D coordinate distance bertween a and b.

        """
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5  


    pass

