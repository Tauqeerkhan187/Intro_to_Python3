import time
from Intro_to_Python3.KB_poller import KBPoller

running = True

player_x = 10
player_y = 10

x_min = 0
x_max = 100
y_min = 0
y_max = 100

kb = KBPoller()

def scan_keys():
    # Non - blocking input scan, returns set of currently pressend keys.
    pressed = set(kb.pressed)
    
    return pressed.intersection({"a","d","w","s","q"})

def render_state():
    print("player is at:", player_x, player_y)

def update_state(keys):
    # Keys is a set like w, a
    global player_x, player_y, running
    
    if "q" in keys:
        running = False
        return 
    
    # Move (for continuous movement)
    if "a" in keys:
        player_x -= 1
    if "d" in keys:
        player_x += 1
    if "w" in keys:
        player_y -= 1
    if "s" in keys:
        player_y += 1
    
    # for bounds
    
    if player_x < x_min:
        player_x = x_min
    if player_x > x_max:
        player_x = x_max
    if player_y < y_min:
        player_y = y_min
    if player_y > y_max:
        player_y = y_max
        
# frame limiter (10 FPS)
frame_Time = 1.0 / 10.0

while running:
    render_state()
    
    keys = scan_keys()
    
    update_state(keys)

    time.sleep(frame_Time)
    
print ("YOU FAILED -__-")