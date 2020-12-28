# TheGameOfLife
In this project, my objective is to develope Conway's Game of Life while increasing my knowledge of Python and the PyGame engine.

# What is The Game of Life?
"The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves."
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

# Rules
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

# Run
python life.py

# What's Next
* Add suport for users to design their own start patterns
* Increase runtime speed by using bit operations
* Write application in C that will allow the game to run on an Arduino light board
