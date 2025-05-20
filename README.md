# mdp-maze-agent
Dit project implementeert een eenvoudige omgeving waarin een agent een doolhof (maze) doorloopt met behulp van het **Value Iteration** algoritme om een optimaal policy te leren.

---

## Inhoud

- `Maze` - Een class die de maze omgeving definieert met posities, rewards en terminal states.
- `Agent` - De agent class die acties uitvoert in de maze volgens een policy en een value function onderhoudt.
- `Policy` - Een class verantwoordelijk voor het selecteren van acties; ondersteunt zowel random als greedy policies gebaseerd op de value function.
- `value_iteration` - Implementatie van het Value Iteration algoritme om optimale state values en policy te berekenen.
- `print_functions` - Helper functies om utilities en het optimale policy overzichtelijk te tonen.
- `main.py` - Het entry point waar de maze, policy en agent worden opgezet en de maze navigatie wordt uitgevoerd.

---

## Class beschrijvingen

### Maze
Stelt het environment grid voor waar de agent in beweegt. Definieert:
- De grootte van de maze (4x4 grid).
- Rewards die gekoppeld zijn aan elke positie.
- Welke states terminal zijn.
- Geldige acties (up, down, left, right).
- De `step` functie die de huidige state en actie neemt en de volgende state, reward en terminal status teruggeeft.

### Agent
Een entiteit die interactie heeft met de maze door:
- Een referentie te houden naar de maze en een policy.
- Een value function bij te houden die de verwachte returns voor elke state schat.
- De policy te gebruiken om acties te selecteren.
- Acties uit te voeren en de value function te updaten op basis van feedback uit de omgeving.

### Policy
Verantwoordelijk voor het bepalen van de actie die de agent neemt. Ondersteunt:
- **Random policy**: kiest willekeurig een actie.
- **Greedy policy**: kiest de actie met de hoogste verwachte waarde volgens de huidige value function.
Bevat methodes om het policy type in te stellen en om een maze instantie te koppelen voor geldige acties en state transities.

### value_iteration
Een function die het Value Iteration algoritme implementeert en:
- Iteratief de value function update gebaseerd op verwachte returns.
- Een discount factor en een convergentiedrempel gebruikt.
- Zowel de geconvergeerde value function als het optimale policy teruggeeft (mapping van states naar acties).

---

## Hoe te gebruiken

1. **Installeer Python 3.7+** (indien nog niet geïnstalleerd).

2. **Clone of download deze repository.**

3. **Run het programma:**

```bash
python main.py
