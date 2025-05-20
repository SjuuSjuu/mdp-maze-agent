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
        # Elke positie heeft: (reward, is_terminal)
        self.states = {
            (0, 0): (-1, False), (0, 1): (-1, False), (0, 2): (-1, False), (0, 3): (40, True),
            (1, 0): (-1, False), (1, 1): (-1, False), (1, 2): (-10, False), (1, 3): (-10, False),
            (2, 0): (-1, False), (2, 1): (-1, False), (2, 2): (-1, False), (2, 3): (-1, False),
            (3, 0): (10, True), (3, 1): (-2, False), (3, 2): (-1, False), (3, 3): (-1, False),
            
        }
        self.actions = {
            0: (-1, 0),  # omhoog
            1: (1, 0),   # omlaag
            2: (0, -1),  # links
            3: (0, 1)    # rechts
        }
    
    def is_valid_position(self, x, y):
        if x >= 0 and x < self.height and y >= 0 and y < self.width:
            return True
        else:
            return False

    def step(self, state, action):
        """
        Voert een stap uit in het doolhof vanuit een gegeven toestand en actie.

        Parameters:
            state : tuple
                De huidige positie in het doolhof als (x, y)-coördinaat.
            action : int
                De actie die moet worden uitgevoerd, gedefinieerd als een index in self.actions.

        Returns:
            next_state : tuple
                De nieuwe positie na het uitvoeren van de actie. Als de actie leidt tot een ongeldige positie,
                blijft de agent op dezelfde plek.
            reward : float
                De beloning geassocieerd met de nieuwe positie.
            is_terminal : bool
                Geeft aan of de nieuwe positie een terminale toestand is.


        Opmerking: Ik map nu de state naar de reward van self.states. Ik had ook een state class kunnen maken met: positie, reward en terminal. Maarja, dat is achteraf en niet per se nodig.
        """
        x, y = state
        dx, dy = self.actions[action]
        new_x = x + dx
        new_y = y + dy

        if self.is_valid_position(new_x, new_y):
            next_state = (new_x, new_y)
        else:
            next_state = (x, y)  # Blijf op dezelfde plek als het buiten het veld gaat

        reward, is_terminal = self.states[next_state]
        return next_state, reward, is_terminal