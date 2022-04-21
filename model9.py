# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 17:08:33 2022

@author: clambert
"""

import random
import operator
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.animation 
import matplotlib.pyplot
import agentframework9
import csvreader1
import tkinter
import requests
import bs4

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs) 

# Set the seed for reproducinility
#random.seed(0)
#random.seed(1)

environment = csvreader1.get_data()
#List of Agents created
agents = []


a = agentframework9.Agent(environment, agents, td_ys, td_xs)
#a. __init__()
a. move ()

num_of_agents = 10
num_of_iterations = 50
neighbourhood = 25

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Make the agents.
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework9.Agent(environment, agents, td_ys, td_xs))

carry_on = True	
        
# Move the agents.
def update(frame_number):
    fig.clear()
    global carry_on
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood) 

    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
 
# Plot the result
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
        print(agents[i].x,agents[i].y)
        
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

def run():
    pass

animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

root = tkinter.Tk() # Main window.
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    
#c.create_rectangle(0, 0, 200, 200, fill="blue")

canvas.draw()

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

tkinter.mainloop() # Wait for interactions. 



