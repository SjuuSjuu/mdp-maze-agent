import yaml
from random_agent import Agent

yaml_path="utils/setup.yaml"

class Maze:

    def __init__(self):
        self.yaml_path = yaml_path
        self.grid = self.grid_init()
    
    # Gebruikt yaml file voor initialisatie van de maze
    def grid_init(self):
        with open(self.yaml_path, 'r') as f:
            data = yaml.safe_load(f)

        raw_maze = data['maze']
        custom_states = data.get('custom_states', [])

        # Initialize grid with default values
        grid = [[{"value": cell, "terminal": False} for cell in row] for row in raw_maze]

        # Apply custom states
        for state in custom_states:
            x, y = state["x"], state["y"]
            grid[y][x].update({
                "value": state.get("value", grid[y][x]["value"]),
                "terminal": state.get("terminal", True)
            })

        return grid

    # Move: direction 1=up, 2=right, 3=down, 4=left
    def action(self, direction):
        moves = {
            1: (0, -1),  # up
            2: (1, 0),   # right
            3: (0, 1),   # down
            4: (-1, 0)   # left
        }

        if direction not in moves:
            print("Invalid direction")
            return self.agent_pos

        dx, dy = moves[direction]
        new_x = self.agent_pos[0] + dx
        new_y = self.agent_pos[1] + dy

        if 0 <= new_x < len(self.grid[0]) and 0 <= new_y < len(self.grid):
            self.agent_pos = [new_x, new_y]

        return self.agent_pos


    def access_position(self, x,y):
        return self.grid[x][y]
         
    def display(self):
        for i in self.grid:
                print(i)

    def step():
        return


        

maze = Maze()
maze.display()
