from maze import Maze

yaml_path = "utils/setup.yaml"

class Agent:
    def __init__(self, yaml_path):
        self.environment = Maze.grid_init
        self.position = yaml_
