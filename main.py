from src.maze import Maze
from src.policy import Policy
from src.random_agent import Agent

def run_simulation(max_steps=100):
    """
    Run a simulation of the agent in the maze.
    
    Args:
        max_steps: Maximum number of steps to run the simulation
    
    Returns:
        total_reward: Total reward accumulated during the simulation
        steps: Number of steps taken
    """
    maze = Maze()
    policy = Policy(maze.actions)
    agent = Agent(maze, policy)
    
    current_state = (0, 0)  # Start position
    total_reward = 0
    steps = 0
    
    print("Starting simulation...")
    print(f"Initial state: {current_state}")
    
    while steps < max_steps:
        action, next_state, reward, is_terminal = agent.act(current_state)
        
        total_reward += reward
        steps += 1
        
        print(f"Step {steps}: Action={action}, New state={next_state}, Reward={reward}")
        
        current_state = next_state
        
        if is_terminal:
            print(f"Reached terminal state after {steps} steps!")
            break
    
    print(f"Simulation ended. Total reward: {total_reward}, Steps taken: {steps}")
    return total_reward, steps

# Run the simulation if this script is executed directly
if __name__ == "__main__":
    run_simulation()