# CSCE 462: An Interactive Chess Board

## Team

This project was developed by Anders Wallace and Zach Hein

## Overview

The system for this chess board is relatively simple. The whole system consists of a Raspberry Pi with the Stockfish engine on it, an Arduino which controls the LED array, and an XY system of buttons along the sides of the board feeding into the Arudino. 

The engine sends the move of the computer to the Arduino, which is parsed and then lights up the corresponding LED spaces to move to and from. The user then moves the computer piece, and then his own piece, pressing the X and Y buttons to tell the Arduino the human player move. This move is processed and the LEDs are light up to show feedback for where the human player is moving. This move is sent from the Arduino to the Raspberry Pi so the engine can see the other players' move, which restarts the cycle until a player has lost.

## Dependencies

This project depends on the python-chess library, to install for Python 3.5+, run the command:

`pip3 install python-chess`

The python program calls on the Stockfish engine to recreate the chess logic. Download the appropriate engine for your system [here](https://stockfishchess.org/download/)

Additionally the Arduino uses `FastLED` library to control the LED strips. This can be downloaded by clicking [here](https://github.com/FastLED/FastLED/archive/master.zip)

## Using the Program

* To play the game, set the program to run on startup, or run the program:

`python3 chess_main.py`

Note: The program calls the Stockfish engine from the user directory in order for the game to run. Make sure to replace this function argument with your own file directory so the engine can be successfully called on startup.

* After the computer makes its move (it is white so it always goes first), the user will click the buttons representing the piece its moving from, and then the buttons representing the space its moving to, i.e. `a7a6`

* Once the game is over (i.e. the computer or user is in checkmate), the LEDs will flash and then turn off, ending the program

## Demonstration
[Here](https://youtu.be/W13wSfIYjTs) is a demonstration of the chess board functionality. 

## Documentation

For further reading about how to use python-chess you can visit the website [here](https://python-chess.readthedocs.io/en/latest/)
