from position import Position

class Maze:
    def __init__(self, gridsize, num_terminal_states):
        self.gridsize = gridsize
        self.num_terminal_states = num_terminal_states
        self.grid = self.create_maze()
                
    # class functions
    def create_maze(self):
        return [[Position] for _ in range(self.gridsize)]
    

#test
maze = Maze(3)
print(maze.grid)