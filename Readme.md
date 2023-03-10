# Warship Game

This is a two-player game built on Django. Each player has three ships with random attack and HP values. The front ship of each player is used for attack and defense. In each turn, players have three choices:

1. Attack: Attack the enemy front ship
2. Defend: Defend a front ship (HP instantly increases by ATK)
3. Switch: Front ship

The game ends when all ships of one player have HP = 0. 

## Prerequisites

To run this game, you will need:

- Django
- Python

## How to Run

To run this game, follow these steps:

1. Clone this repository to your local machine.
2. Open a terminal window and navigate to the project directory.
3. Run the following command to start the server:
    `python Server_Warship/manage.py runserver`
4. Open another terminal window and navigate to the project directory.
5. Run the following command to start the client:
    `python Cilent/client.py runserver`
6. Enter your name and choose one of the following options:
    - Create a new board: Generates a new board and gives a code
    - Join a board: Requires a board code to join
    - Reconnect to the board: Requires a board code to join (use when an accident happens to client)
