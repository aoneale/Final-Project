"""
The strategist's job is to formulate the strategy of the player. More specifically, you decide the player's next move given 
the game state at any particular time. Therefore, it's essential for you to have a good understanding of the game state, layout etc. 

Power skill: The team depends on your intelligence and strategy to win! You can get as creative as you want in making your 
strategising algorithm as complex/smart as you want! Bring in all the AI/RL/DL you've got! ;)

"""
import random

# Change the class name below to Strategist<Color> 
# For example, if your team color is lavender, change the class name below to StrategistLavender
# This is to prevent conflict when we integrate all strategists for the final competition

class Strategist():
    
    def __init__(self, layout, label):
        self.neighbors = self.get_neighbors(layout)
        self.label = label #DO NOT CHANGE
        # This is important as it will be be used as a handle to identify your team throughout the game

        
    # This function is the brain of the player and will be called by the manager whenever necessary. 
    # It looks at the current game state to return the next best move
    # DO NOT CHANGE THE FUNCTION DEFINITION
    def next_move(self, game_state):
        return random.choice([1,2])
    
    
    # Find neighbors of each panel
    # This method will be handy to plan your next move
    # This is a helper function, you are free to change/delete/modify it as per your needs
    def get_neighbors(self, layout):
        neighbor_dict = {}
        return neighbor_dict
    