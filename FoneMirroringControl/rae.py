import time
import threading
from pynput.keyboard import Listener, KeyCode, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

delay = 0.03
move_duration = 0.01  # Duration for the smooth move

start_stop_key = KeyCode(char='z')
mouse = MouseController()

class ClickMouse(threading.Thread):
    def __init__(self, delay, move_duration):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.move_duration = move_duration
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                # Get the original position
                start_x, start_y = mouse.position
                
                # Press and hold the left mouse button
                mouse.press(Button.left)
                
                end_y = start_y - 50
                steps = 50
                step_delay = self.move_duration / steps
                
                for i in range(steps):
                    # Calculate intermediate positions
                    y = start_y - ((start_y - end_y) * (i + 1) / steps)
                    mouse.move(0, y - mouse.position[1])  # Move relatively
                    time.sleep(step_delay)
                
                # Release the left mouse button
                mouse.release(Button.left)
                
                # Teleport cursor back to original position
                mouse.position = (start_x, start_y)
                
                time.sleep(self.delay)

kb = KeyboardController()
click_thread = ClickMouse(delay, move_duration)
click_thread.start()

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()

with Listener(on_press=on_press) as listener:
    listener.join()