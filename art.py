"""
The artist's job is be as creative as possible in designing/coloring panels that their team occupies
Power skill: You are the face of your team - you are not only responsible for the final output that all other teams can see on the game board but also responsible for packaging and communicating it to the gameboard.
The team depends on your interfacing to score points and win the battle!

"""

import requests 
import socket
from socket_connector import PanelConnector

######################################

## Recommended things to consider as the Artist:

## 1. Think of creative ways of designing the panel. At the very minimum, assign it the color that represents your team
## 2. Some examples of being creative could be understanding the game situation and getting creative when you are, for example, blocked or respwaned
## 3. You are also responsible for packaging and sending data back to the game board. 

####################################

# Change the class name below to Artist<Color> 
# For example, if your team color is lavender, change the class name below to ArtistLavender
# This is to prevent conflict when we integrate all artists for the final competition
class Artist():
    def __init__(self,label, simulator = True):
        ### Do not edit the lines in this block of code
        ### These settings are essential for the game manager to connect 
        ### to the panel simulator
        self.label = label
        
        
    def send_data_to_panels(self, list_of_bytes):
        """Send data to the Nanoleaf simulator or to the Nanoleaf panels.
        list_of_bytes should contain a list of integers, each one between 0
        and 255."""
        PanelConnector().send_data_to_panels(list_of_bytes)
    
    # Using game state and your label color, design all panels for the next move
    # Please respect the color label for other current players in the game, i.e., try to assign a shade of red to team red etc
    # Package panel data and your final design and send it to the gameboard - you might need to refer to the api documentation 
    # to understand expected output format that the gameboard expects
    # DO NOT CHANGE THE FUNCTION DEFINITION
    def communicate_with_style(self, game_state, panel_id_list):
        print('Artist in action :)')