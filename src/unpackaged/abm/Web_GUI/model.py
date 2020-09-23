# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:12:12 2020

@author: Student 201386558
Univeristy of Leeds

Model should run from a GUI menu.
It takes in 3 arguments.
Model will animate in a popup window.

- Gets model arguments from the user.
- Creates a GUI window.
- Reads in data to create an environment.
- Reads in data from a web scrape for agents startin positions.
- Creates a set number of agents based on user input.
- Moves agents randomly a number of iterations based on user input.
- Agents collect parts of environment as they move around.
- Agents check surroundings for nearby agents and share stores.
- Plots the positions of the agents as they move.
- Environments changes are plotted as they agents 'nibble' it away.
- Programme stops when number first agent stores 100 pieces of environment
or number of agents moves input by user are complete.

"""
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot, agentsFramework, csv, sys
import random, matplotlib.animation, tkinter, requests, bs4


'''
Function to call agents methods to animate agents and iteract with surrounding.
''' 
def update(frame_number):
    fig.clear()
    global carry_on
    if carry_on == True:
        
        # Randomly shuffle agent list so no agent has advantage if store collection
        random.shuffle(agents)
        
        # Call agents methods to interact with environment and each other
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neigbourhood)
           
        # Stop when first agents get 100 in their store
        for i in range(num_of_agents):
            if (agents[i].store > 100):
                carry_on = False
                print(agents[i], "They win, Stopping Now!")
                
        # Plot the environment and 
        # in turn plot all agents for each iteration of moves
        matplotlib.pyplot.ylim(0, 99)
        matplotlib.pyplot.xlim(0, 99)
        matplotlib.pyplot.imshow(environment)   
        for i in range(num_of_agents):
            matplotlib.pyplot.scatter(agents[i].x, agents[i].y)


'''
Function to stop the animation once criteria is met.
''' 
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < num_of_iterations) & (carry_on) :
        yield a	# Returns control and waits next call.
        a = a + 1    


'''
Function called when user interacts with the GUI to run the model.
Function calls other update function and animates the outputs.
'''
def run():
    animation = matplotlib.animation.FuncAnimation(fig,
                                update, frames=gen_function, repeat=False)
    canvas.draw() 

    
''' 
Get input variables from the user as 3 int arguments.
'''
num_of_agents = int(sys.argv[1])
num_of_iterations = int(sys.argv[2])
neigbourhood = int(sys.argv[3])


'''
Initialise and style the GUI window.
'''
root = tkinter.Tk()
root.wm_title("ABM Model")
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model Menu", menu=model_menu)
model_menu.add_command(label="Run model", command=run)


'''
Open lcoal file, read data, add to values to environment list.
Agents will interact with the environemnt in output animation.
'''
environment = []
fOpen = open("in.txt") # File saved with script
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


'''
Request HTML and parse into table into x & Y list.
''' 
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})


''' Initialise the Agent object to add each agents
position in the empty list
''' 
agents = []
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    # Object is passed environment, agent list and their x & y positions
    agents.append(agentsFramework.Agent(environment, agents, y, x))


''' 
Plot the agents positions on the 'nibbled' environment in the GUI 
'''
# Stopping condition initial variable
carry_on = True
# Output GUI sizes and axes, believe this window is unused in programme
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])  
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

tkinter.mainloop()  # Hold until GUI is activated by the user