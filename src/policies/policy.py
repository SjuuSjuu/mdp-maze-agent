# Policy class: Deze klasse is verantwoordelijk voor de policy van de agent. Je kunt kiezen tussen
    # random en greedy policy. De random policy kiest willekeurig een actie uit de beschikbare acties, 
    # terwijl de greedy policy de actie kiest die de hoogste waarde oplevert volgens de waarde functie van de agent. 
    # De klasse heeft ook een methode om de huidige policy in te stellen en om de maze in te stellen. Dit moet je handmatig doen in de main.py.


import random

class Policy:
    def __init__(self, actions):
        self.actions = list(actions.keys())
        self.current_policy = "random"  # default
        self.maze = None  # Wordt nog ingesteld in main

    def set_policy(self, name):
        if name in ["random", "greedy"]:
            self.current_policy = name
        else:
            raise ValueError(f"Policy '{name}' is not supported. Use 'random' or 'greedy'.")

    def set_maze(self, maze):
        self.maze = maze

    def select_action(self, state, value_function=None):
        if self.current_policy == "random":
            return self.random_policy()
        elif self.current_policy == "greedy":
            return self.greedy_policy(state, value_function)

    def random_policy(self):
        return random.choice(self.actions)

    def greedy_policy(self, state, value_function):
        # Selecteerd de actie met de hoogste value volgens value functie
        best_action = None
        best_value = float("-inf")
        for action in self.actions:
            next_state, reward, _ = self.maze.step(state, action)
            value = reward + value_function.get(next_state, 0.0)
            if value > best_value:
                best_value = value
                best_action = action
        return best_action