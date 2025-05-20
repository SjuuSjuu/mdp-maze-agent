class Agent:
    def __init__(self, maze, policy):
        """
        Initialiseer een agent met een instantie van maze en policy class.
        
        Args:
            maze: Instantie van de Maze klasse
            policy: Instantie van de Policy klasse
        """
        self.maze = maze
        self.policy = policy
        self.value_function = {}  # Dictionary om de verwachte returns van elke state op te slaan
        
        # De waarde initialiseren voor alle states met nullen
        for state in self.maze.states.keys():
            self.value_function[state] = 0.0
    
    def act(self, state):
        """
        Actie uitvoeren gebaseerd op huidige state en geinitialiseerde policy.
        
        Args:
            state: The current state (positie) in de maze (deze kun je terugmappen naar de rewards en terminal states (deze staan hardcoded in de maze class))
            
        Returns:
            action: Gekozen actie
            next_state: Resulterende state na het nemen van de actie
            reward: Ontvangen reward na de actie
            is_terminal: Geeft aan of de resulterende state terminal is
        """
        # Use policy to select an action
        action = self.policy.select_action(state, self.value_function)
        
        # Execute the action in the environment
        next_state, reward, is_terminal = self.maze.step(state, action)
        
        return action, next_state, reward, is_terminal
    
    def update_value_function(self, state, value):
        """
        Update de value function voor een gegeven state.
        
        Args:
            state: De state die moet worden geupdate
            value: Nieuwe waarde die moet worden toegewezen aan de state
        """
        self.value_function[state] = value