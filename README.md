# CSCE 462: An Interactive Chess Board

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


## Documentation

For further reading about how to use python-chess you can visit the website [here](https://python-chess.readthedocs.io/en/latest/)
