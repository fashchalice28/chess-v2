# Chess.com-Cheat
Simple chess cheat for Chess.com based on opencv.
#
![Showcase](https://raw.githubusercontent.com/ofeksadlo/Chess.com-cheat/master/showcase(2).gif)

# What it does
Highlight above the board the best next move for you.

# How it works?
The program will wait for the opponent turn depend on the clients chosen color.</br>
Then it will loop through every cell to detect the last moveset and feed the stockfish engine.</br>
Which will predict the best next move for the client.</br>
The clients moves are gathered by detecting the</br>
position where the client clicked on the board. And then translated to a moveset.</br>
In the old method we captured every 501 milliseconds the board to detect the last moveset.</br>
That brought up a big problem because if the opponent moved too fast we would miss</br>
the clients move. Using this method you can even play bullet mode. 

# Requirements
Use pip install -r requirements.txt to install all dependencies. 

# How to make it work
1) Download the main.py and the data folder
2) Download stockfish from here: https://stockfishchess.org/download/ I'v used "64-bit: Maximally compatible but slow."</br>
   **Keep in mind the exe file needs to be at same drive as the scripts running on.**</br>
   **Also you might need to change the file name in code! Not just the path.**
3) You need to extract the exe file you downloaded and in main.py code, change the path to your stockfish engine exe file.
4) About the stockfish.set_depth(16) you can put higher values. The higher the value the more accurate the prediction
   But it's also slower. Using set depth 16 I tied against stockfish level 8 so it's preety strong as it is.
5) 1) Open up a game while logged in to Chess.com (Playing as anonymous will change the board size and mess everything</br>
    Also it's only tested on chrome and on 100% zoom while logged in).</br>
   2) During the freeze time open up the program choose your starting color. And alt+tab back to the browser (Don't use your mouse).</br>
    Keep in mind that your mouse clicks from that moment matters.</br>
    So play like that: 1 click represent the from cell and 1 click represent the to cell when it's your turn.</br>
    No dragging pieces.</br>
    No checking youtube for a second</br>
    It will mess everything and the program will crash</br>

***Keep in mind Chess.com would most definetly ban you for playing against other players.</br>
Play only against bots!***
   

# Compatibility Issues
* The program only tested with Chrome on resolution 1920x1080 and the zoom needs to be 100%
* Technically you can make the program to work with any kind of browser on any kind of zoom.
  As long as you fix the cordinates of the board screenshot and the cell size.
* The program is more stable now but need to get a better check on mouse clicks.</br>
  In order to avoid missread client moves. 3 conditions needs to be checked to make it perfect:
  1) Check if board is visible.
  2) Check if mouse clicked within board rectangle.
  3) Check if move is legal as in between a1 - h8.

# Future plans
- [x] Adding support for black pieces
- [x] Saving games played
- [x] Auto Play (Added check it out through the config. Only works for white player and still have some bugs.)
- [ ] Loading game movesets from File.
- [x] Drawing live on the board to highlight best next move.
- [ ] More stable clients moves read.
- [ ] Currently the program reads last move using pixel matching.</br>
      It works but if we miss one move the predictions are wothless.</br>
      I'm going to develop an improved version of this cheat. That will detect</br>
      pieces live from the screen. Then translate the board to Forsyth–Edwards</br>
      Notation to get prediction from current board position. This will allow to solve</br>
      puzzels and start the cheat mid-game.
# Disclaimer 
**This entire project done for the purpose of challenge and education.**<br>
**Not for the purpose of cheating**

**Developed on [Python 3.7.7](https://www.python.org/ftp/python/3.7.7/python-3.7.7-amd64.exe)**

gxzfw