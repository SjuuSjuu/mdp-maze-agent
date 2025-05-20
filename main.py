# main.py

from src.environment.maze import Maze
from src.policies.policy import Policy
from src.agents.agent import Agent
from src.algorithms.value_iteration import value_iteration
from src.visualisation.print_functions import action_symbols, print_utilities, print_optimal_policy, print_agent_navigation

if __name__ == "__main__":
    maze = Maze()

    value_function, optimal_policy = value_iteration(maze)
    print_utilities(value_function, maze)
    print_optimal_policy(action_symbols, optimal_policy, maze)


    policy = Policy(maze.actions)
    policy.set_policy("greedy") # greedy om de beste actie te kiezen uit de policy, maar kan ook random
    policy.set_maze(maze)

    agent = Agent(maze, policy)
    agent.value_function = value_function

    start_state = (3, 1) #start positie (zie canvas)
    print_agent_navigation(action_symbols, agent, policy, start_state)
