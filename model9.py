# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 17:08:33 2022

@author: clambert

model9 relateds to the "GUI-Webscraping" practical and should be used with 
the agentframework9 and the csvreader9 files.

in.txt is the input data for this file and should be stored in the same directory

Directions:
1. Save model9, agentframework9 and csvreader9 in the same directory location
2. Run model9

Expected outputs:
1. Scatter chart of agents, coloured individually and displayed on environment
background in a seperate window. The animation will show how the agents move
and the eaten "paths" will be displayed. This will also have a GUI button "Run 
Model" from the dropdown at the top left hand corner.
2. print shared neighberhood values between agents (sharing)

Notes
I was unable to complete this practical due to time constraints and the 
following notes apply:
    I was able to build the GUI output but the model runs automaticly and does 
    not run again when the button is pressed.
    I began to work through the web scraping section of the practical but ran 
    out of time to complete. 
    The model runs, but takes some time to process and seems to not reset after 
    completion - I needed to restart the kernel to begin the model again.

"""

#Imported modules
import matplotlib
matplotlib.use('TkAgg') 
import random
import operator
import matplotlib.animation 
import matplotlib.pyplot
import agentframework9
import csvreader9
import tkinter
#import requests
#import bs4

'''
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
#print(td_ys)
#print(td_xs)
'''
# Set the seed for reducability
#random.seed(0) #testing reducability of model - when set, output should be the same each time
#random.seed(1)

#bring enviroment data in from csvreader8
environment = csvreader9.get_data()

#List of Agents created
agents = []

a = agentframework9.Agent(environment, agents)
#a. __init__()
a. move ()
print(a.y, a.x) #test agentframework

num_of_agents = 10 #changable value
num_of_iterations = 100 #changable value
neighbourhood = 25 #changable value

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Make the agents.
for i in range(num_of_agents):
    #y = int(td_ys[i].text)
    #x = int(td_xs[i].text)
    agents.append(agentframework9.Agent(environment, agents))

#print (agents) #test

carry_on = True	
        
# Move the agents.
def update(frame_number):
    """
    Parameters
    ----------
    moves agents by frame during the animation 

    Returns
    -------
    None.

    """
    fig.clear() # clears previous frame in amnimation (?)
    global carry_on
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move() #moving the agents
            agents[i].eat() #eating into the environment
            agents[i].share_with_neighbours(neighbourhood) #sharing locations between agents

    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
   
#returns graphical results
    matplotlib.pyplot.xlim(0, 99) #x axis
    matplotlib.pyplot.ylim(0, 99) #y axis
    matplotlib.pyplot.imshow(environment) #plots enviroment data from csvreader8
    for i in range(num_of_agents): #created and moved agents based on number of agents
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y) #plot scatter of agents
        print(agents[i].x,agents[i].y) #print list of agents
      
def gen_function(b = [0]):
    """
    Parameters
    ----------
    Frames start at 0 and count through until stopping condition is met

    Yields
    ------
    Returns control and waits next call.

    """
    a = 0
    global carry_on
    while (a < 10) & (carry_on) :
        yield a			# 
        a = a + 1

#animation lines and run function
def run():
    """
    runs the animation in a seperate window and applies GUI features, such as a
    "Run" button

    """
    pass
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    
root = tkinter.Tk() # Main window.
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

canvas.draw() 

tkinter.mainloop() # Wait for interactions. 

# done marker
#print ("finished")
