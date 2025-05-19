# B. Random agent

# Maak een klasse Agent met minimaal:

#     een instantie van een Maze;
#     een Policy (zie onder);
#     een value function, die een verwachtte return bij een state geeft;
#     een methode act(), die een actie uitvoert gegeven een state en op basis van de eigen policy.


import random

class Policy:
    def __init__(self, actions):
        self.actions = list(actions.keys())
        self.policies = {
            "random": self.random_policy
            # Later you can add more like:
            # "greedy": self.greedy_policy
        }
        self.current_policy = "random"  # Default policy
    
    def set_policy(self, name):
        if name in self.policies:
            self.current_policy = name
        else:
            raise ValueError(f"Policy '{name}' not found.")
    
    def select_action(self, state, value_function=None):
        return self.policies[self.current_policy](state, value_function)
    
    def random_policy(self, state, value_function=None):
        return random.choice(self.actions)