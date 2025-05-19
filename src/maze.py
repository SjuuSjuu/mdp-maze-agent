# Maak een klasse Maze met minimaal:

#     16 posities;
#     rewards, één bij elke positie;
#     een verzameling van states: een combinatie van een positie, een reward en een boolean die aangeeft of de state terminal is;
#     vier acties, bijvoorbeeld 0 voor links, 1 voor rechts, et cetera;
#     een methode step() die een stap in de omgeving uitvoert: de methode geeft op basis van een state en een actie de volgende state.

class Maze:
    def __init__(self):
        self.width = 4
        self.height = 4
        # Elke positie: (reward, is_terminal)
        self.states = {
            (0, 0): (-1, False), (0, 1): (-1, False), (0, 2): (-1, False), (0, 3): (40, True),
            (1, 0): (-1, False), (1, 1): (-1, False), (1, 2): (-1, False), (1, 3): (-10, True),
            (2, 0): (-1, False), (2, 1): (-10, False), (2, 2): (-1, False), (2, 3): (-1, False),
            (3, 0): (-1, True), (3, 1): (-10, False), (3, 2): (-1, False), (3, 3): (-1, False)
        }
        self.actions = {
            0: (-1, 0),  # omhoog
            1: (1, 0),   # omlaag
            2: (0, -1),  # links
            3: (0, 1)    # rechts
        }
    
    def is_valid_position(self, x, y):
        within_width = 0 <= x < self.height
        within_height = 0 <= y < self.width
        return within_width and within_height
    
    def step(self, state, action):
        x, y = state
        dx, dy = self.actions[action]
        new_x, new_y = x + dx, y + dy
        if self.is_valid_position(new_x, new_y):
            next_state = (new_x, new_y)
        else:
            next_state = (x, y)  # Buiten de grenzen: zelfde positie
        reward, is_terminal = self.states[next_state]
        return next_state, reward, is_terminal