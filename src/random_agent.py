class Agent:
    def __init__(self, maze, policy):
        """
        Initialize an agent with a maze environment and policy.
        
        Args:
            maze: Instance of the Maze class
            policy: Instance of the Policy class
        """
        self.maze = maze
        self.policy = policy
        self.value_function = {}  # Dictionary to store expected returns for each state
        
        # Initialize value function for all states with zero
        for state in self.maze.states.keys():
            self.value_function[state] = 0.0
    
    def act(self, state):
        """
        Execute an action given the current state based on the agent's policy.
        
        Args:
            state: The current state (position) in the maze
            
        Returns:
            action: The chosen action
            next_state: The resulting state after taking the action
            reward: The reward received
            is_terminal: Whether the resulting state is terminal
        """
        # Use policy to select an action
        action = self.policy.select_action(state, self.value_function)
        
        # Execute the action in the environment
        next_state, reward, is_terminal = self.maze.step(state, action)
        
        return action, next_state, reward, is_terminal
    
    def update_value_function(self, state, value):
        """
        Update the value function for a given state.
        
        Args:
            state: The state to update
            value: The new value to assign
        """
        self.value_function[state] = value