from martypy import Marty
import tkinter as tk
marty = Marty('exp', '/dev/ttyAMA0')
marty.get_ready()
tk.bind_all('<Key>', key_input)

def key_input(event):
    key_press = event.keysym.lower()
    do while key_press != 'l'  
    if key_press == 'w':
        print('Marty walks two steps forward')
        marty.walk()
    elif key_press == 'a':
        print('Marty walks two steps left')
        marty.sidestep('left')
    elif key_press == 's':
        print('Marty walks two steps backward')
        marty.walk(2, 'auto', 0, -25)
    elif key_press == 'd':
        print('Marty walks two steps right')
        marty.sidestep('right')
    elif key_press == 'q':
        print('Marty turns 15 degrees left') 
        marty.walk(2, 'auto', 15)
    elif key_press == 'e':
        print('Marty turns 115 degrees right')
        marty.walk(2, 'auto', -15)
    elif key_press == 'z':
        print('Marty stands straight')
        marty.stand_straight()
    elif key_press == 'c':
        print('Marty dances')
        marty.dance()
    elif key_press == 'x':
        print('Marty plays excited sound')
        marty.play_sound('excited')
    marty.stop('pause')



