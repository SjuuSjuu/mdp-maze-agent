def value_iteration(maze, gamma=1.0, delta_threshold=0.1):
    """
    Value Iteration algoritme voor het vinden van optimaal beleid in gegeven MDP.
    
    Parameters:
   
    maze : Maze object
        Het doolhof waarin we de optimale policy zoeken
    gamma : float
        Discount factor (tussen 0 en 1)
    delta_threshold : float
        Convergentie waarde (moet kleiner zijn dan deze om te stoppen, betekend zo goed als geen verandering meer in de value functie)
    
    Returns:
   
    value_function : dict
      
    policy : dict
        
    """
    # Set van alle mogelijke acties A (deze staat in de maze class maar zijn: 0=omhoog, 1=omlaag, 2=links, 3=rechts)
    actions = list(maze.actions.keys())
    
    # Initialisatie van state-value functie voor alle states
    value_function = {state: 0 for state in maze.states}
    
    # Policy die wordt bepaald
    policy = {}
    
    # Value Iteration algoritme
    while True:
        delta = 0
        
        # Maak een kopie van de huidige value functie voor updates
        new_value_function = value_function.copy()
        
        # Voor elke toestand s in de state space S
        for state in maze.states:
            reward, is_terminal = maze.states[state]
            
            # Terminal states hebben een vaste waarde, dus skippen deze
            if is_terminal:
                continue

            max_value = float('-inf')
            for action in actions:
                # transitie naar volgende state s' na actie a in state s
                next_state, next_reward, _ = maze.step(state, action)
                
                # Bereken Q(s,a) = R(s,a) + γ * V(s')
                action_value = next_reward + gamma * value_function[next_state]
                
                # Bepaal de maximale waarde over alle acties
                max_value = max(max_value, action_value)
            
            # Update de value functie
            new_value_function[state] = max_value
            
            # Update delta voor convergentie check
            delta = max(delta, abs(new_value_function[state] - value_function[state]))
        
        value_function = new_value_function

        if delta < delta_threshold:
            break
    
    # Bepaal optimale policy
    for state in maze.states:
        reward, is_terminal = maze.states[state]
        
        # Terminal states hebben geen beleid nodig
        if is_terminal:
            policy[state] = None
            continue
            
        # Bereken argmax_a [ R(s,a) + γ * V(s') ]
        best_action = None
        best_value = float('-inf')
        
        for action in actions:
            #transitie naar volgende state s' na actie a in state s
            next_state, next_reward, _ = maze.step(state, action)
            
            # Bereken Q(s,a) = R(s,a) + γ * V(s')
            action_value = next_reward + gamma * value_function[next_state]
            
            # Vind de actie met de hoogste waarde
            if action_value > best_value:
                best_value = action_value
                best_action = action
                
        # De optimale policy selecteert de actie met de hoogste Q-waarde
        policy[state] = best_action
    
    return value_function, policy