from maze import Maze
import yaml
import random
yaml_path = "utils/setup.yaml"

class Agent:
    def __init__(self, yaml_path):
        self.environment = Maze.grid_init
        self.position = (0,0)
        self.yaml_path = yaml_path


    def set_spawn(self, yaml_path):
        with open(self.yaml_path, 'r') as f:
            data = yaml.safe_load(f)
            return data.get('custom_states', [])

    def act(self):
        return random.randint(1, 4)