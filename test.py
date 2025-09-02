import pyautogui, time, random, keyboard, ctypes, shutil, os
# from screeninfo import get_monitors
from collections import deque

#do position as grid squares

# size of file step
XSTEP = 76
YSTEP = 100
# user screen infos
RES = (1920, 1080)
GRID_BOUNDS = (24,10)

MORE_MON = False

# global game data
TICK = 0.2
snake = deque([(0,2),(0,1),(0,0)])
occupied = set(snake)
apple = (2,0)
hx, hy = snake[0] #head cords

# Game logic
def play():
    round_setup()
    next_move = (0,1)
    next_tick = time.monotonic() + TICK
    while True:
        global hx, hy
        hx, hy = snake[0]
        if keyboard.is_pressed("q"): break
        if keyboard.is_pressed("w") and next_move != (0,1): next_move = (0, -1)
        elif keyboard.is_pressed("a") and next_move != (1,0): next_move = (-1, 0)
        elif keyboard.is_pressed("s") and next_move != (0,-1): next_move = (0, 1)
        elif keyboard.is_pressed("d") and next_move != (-1,0): next_move = (1, 0)
       
        now = time.monotonic()
        if now >= next_tick:
            if step(next_move): break
            next_tick += TICK
        
        time.sleep(0.001)
            
    clean_up()

def step(dir):
    global hx, hy
    nx = hx + dir[0]
    ny = hy + dir[1]

    #bounds    
    if nx > GRID_BOUNDS[0] or ny > GRID_BOUNDS[1] or nx < 0 or ny < 0:
        print(hx, hy)
        return True
    if nx != apple[0] or ny != apple[1]:
        tail = snake.pop()    
    snake.appendleft((nx, ny))
    hx, hy = nx, ny
    print(snake)
    move(tail,(hx,hy))
    
    return False
    
def round_setup():
    # make target
    global apple
    rx = random.randint(2,GRID_BOUNDS[0])
    ry = random.randint(1,GRID_BOUNDS[1])
    move(apple,(rx,ry) )

    apple = rx, ry

# File logic
# def set_up():
#     desktop = os.path
#     # display files on the desktop
#     # switch folder? 
#     # switch back?
#     for m in get_monitors(): 
#         print()

def clean_up():
    print("peace")

# def reset(dead_snake):
#     if len(dead_snake) != 0:
#         home = dead_snake.pop()
        

def move(origin, dest):
    pyautogui.moveTo(origin[0]*XSTEP+10,origin[1]*YSTEP+10)
    pyautogui.mouseDown()
    pyautogui.moveTo(dest[0]*XSTEP+10, dest[1]*YSTEP+10)
    pyautogui.mouseUp()

play()  