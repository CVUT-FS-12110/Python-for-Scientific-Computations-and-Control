# Rock, paper, scissors

You are supposed to create solver for the simulation of tournament in the game called "[Rock, paper, scissors](https://en.wikipedia.org/wiki/Rock_paper_scissors)". The solver will consists of function **rock_paper_scissors** and two classes **Game** and **Player**. They are already defined in prepared file **rock_paper_scissors.py** (use this file for your implementation). Your task is to fill in their implementations. Read carefully following specification of given functional parts:


### Function rock_paper_scissors

The function will be given three variables for every tournament that should be simulated.
* number_of_rounds - specifies for how many times should be the game run
* player_a - dictionary of player A action probabilites
* player_b - dictionary of player B action probabilites

Function will guide the flow of the program according to following workflow. At the end it will return results of the game.

#### Workflow of function
* Obtain passed arguments
* Crate two instances of class **Player** (one for each player given). 
* Create instance of class Game
* Run the game object method **run_game**
* Get results of the game with game object method **get_results** 
* Return results in required format from the function


### Class Player

This class will represent a player in the tournament. It will have following properties:
* atribute/s to hold player action probabilites
* constructor method - player action probabilites must be passed with it
* validity_check method - this method will check if player has valid action probabilites
    * sum of all probabilities must be exactly 1
    * no single probability may exceed 1
    * no single probability may be lower than 0
    * in case probabilities are OK return **True**, otherwise **False**
* __repr__ magic method - returns any reasonable description of the object


### Class Game

This class will represent the tournament. It will have following properties:
* atribute/s to hold both players signed to the tournament
* constructor method - both players and number_of_rounds will be passed with it
* validity_check method - this method will check if the game is in valid state
    * both players must have **True** validity_checks
    * number_of_games must be higher than 0
    * in case all is **True** return **True**, otherwise **False**
* run_game method - this method will run the simulation of the tournament if the game is in valid state. Workflow of method:
    * check if game is valid with game validity_check method
        * if the result is **False** abort the game
        * if the result is **True** proceed
    * game will run number of rounds specified in given parametr
        * in each round the both players will chose their strategy according to their action probabilities (see hint in the bottom)
        * the result of each round is counted to the results of the entire game so it can be returned later
* get_results method - returns the result of the game
    * if the game was aborted return **False**
    * if the game run return it's result, see **Output data format**
* __repr__ magic method - returns any reasonable description of the object


### Input data format

Function rock_paper_scissors will be given input data in this format
```Python
number_of_rounds = 1000

player_a = {
    "paper": 0.8,
    "scissors": 0.1,
    "rock": 0.1,
}

player_b = {
    "paper": 0.1,
    "scissors": 0.8,
    "rock": 0.1,
}
```


### Output data format

Function rock_paper_scissors will return results in tho following formats:
* aborted game -> return **False**
* completed game -> return dictionary in this format
```Python
{
    'player_a': number_of_wins_of_player_A,
    'player_b': number_of_wins_of_player_B,
    'tie': number_of_ties,
}
```

Function has to return correct output for any valid combination of inputs.

### Hint - decide rolls for probabilities

Use Python random library to generate the rolls. For example:

```Python
import random

prob = random.uniform(0, 1) # return float 0-1

# or

case = random.randint(1, 3) # return: 1, 2, 3
```
