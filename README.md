# CSCE 462: An Interactive Chess Board

## Dependencies

This project depends on the python-chess library, to install for Python 3.5+, run the command:

`pip3 install python-chess`

Additionally the arudino uses `FastLED` library to control the LED strips. This can be downloaded by clicking [here](https://github.com/FastLED/FastLED/archive/master.zip)

## Using the Program

* To play the game, run the program:

`python3 chess_main.py`

Note: The program calls the Stockfish engine from the user directory in order for the game to run. Make sure to replace this function argument with your own file directory so the engine can be successfully called on startup.

* When prompted, the user will input a string of the space they are moving from to the space they are moving to; for example if the user is moving from A7 to A5 then the user will input `a7a5`

* To quit the game, enter `q`

* To restart the game, enter `r`

## Documentation

For further reading about how to use python-chess you can visit the website [here](https://python-chess.readthedocs.io/en/latest/)
