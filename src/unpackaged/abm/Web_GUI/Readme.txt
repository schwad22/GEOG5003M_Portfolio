Agent Based Modelling Programme


README

A programme to animate the movement of 'n number of agents around a set environment whilst they interact with the environment and each other.

The programme is run by calling model.py and passing in 3 arguments as text (number):
	Number of agents
	Number of agent moves (iterations of move)
	Size of agents search neighbourhood

No installation is necessary providing the user has Python3 already installed.
The programme is run from a GUI that will initiate, and will animate their movement, the programme will run till all iterations have completed,
or a stopping condition is met, when one agent has collected 100 pieces of the environment. 


LIBRARIES

random
matplotlib
tkinter
requests
bs4
csv
sys


ISSUES

Once programme completes the user must close the GUI and kill the programme by pressing crtl+c.
Documentation is only present for the agentsFramework class, as I couldn't get either Pydoc or Sphinx to write the documentation for model.py


USAGE

This programme is open source and permission is granted for wider use.
Licence - Apache License 2.0

