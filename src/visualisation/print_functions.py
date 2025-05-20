# print_functions.py
action_symbols = {
        0: '↑',
        1: '↓',
        2: '←',
        3: '→',
        None: 'T'
    }

def print_utilities(value_function, maze):
    print("Utilities:")
    for i in range(maze.height):
        row_cells = []
        for j in range(maze.width):
            v = value_function[(i, j)]
            cell_str = f"{v:.1f}".rjust(6)
            row_cells.append(cell_str)
        print(" ".join(row_cells))


def print_optimal_policy(action_symbols, optimal_policy, maze):
    print("\nOptimal Policy:")
    for i in range(maze.height):
        row = ""
        for j in range(maze.width):
            a = optimal_policy[(i, j)]
            row += f"  {action_symbols[a]}  "
        print(row)


def print_agent_navigation(action_symbols, agent, policy, start_state):
  

    print(f"\nNavigating the maze from position {start_state}:")
    current_state = start_state
    while True:
        action = policy.select_action(current_state, agent.value_function)
        next_state, reward, is_terminal = agent.maze.step(current_state, action)
        print(f"From state {current_state}  action {action_symbols[action]} to {next_state}, reward: {reward}, terminal: {is_terminal}")
        if is_terminal:
            break
        current_state = next_state
    print("Reached terminal state.")
