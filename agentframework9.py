# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 16:36:52 2022

@author: clambert
"""

import random


class Agent():

    def __init__(self, environment, agents, td_ys, td_xs):
        self.environment = environment
        self.agents = agents
        self.store = 0
        self.y = td_ys
        self.x = td_xs
        #self.x = random.randint (0,99)
        #self.y = random.randint (0,99)
                
        if (td_xs == None):
            self._x = random.randint(0,100)
        else:
            self._x = td_xs 
            
        if (td_ys == None):
            self._y = random.randint(0,100)
        else:
            self._y = td_ys 
    
    def move (self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:       
            self.y = (self.y - 1) % 100
    
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10  

    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
        if dist <= neighbourhood:
            sum = self.store + agent.store
            ave = sum /2
            self.store = ave
            agent.store = ave
            print("sharing " + str(dist) + " " + str(ave))

    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5  


    pass

#print (self.x) # test
#print (self.y) # test
