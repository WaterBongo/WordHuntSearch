from pynput import mouse
import pyautogui

points = []

def on_click(x, y, button, pressed):
    if pressed:
        points.append((x, y))
        if len(points) == 2:
            return False

print("Manually position the mouse cursor to the first corner and do a left click.")
print("Then move to the diagonally opposite corner and do a left click.")

# Collect events until released
with mouse.Listener(on_click=on_click) as listener:
    listener.join()

first_point, second_point = points

# Calculate dimensions of the box from the points
left = min(first_point[0], second_point[0])
top = min(first_point[1], second_point[1])
width = abs(first_point[0] - second_point[0])
height = abs(first_point[1] - second_point[1])

# Get screenshot and save it
screenshot = pyautogui.screenshot(region=(left, top, width, height))
screenshot.save('screenshot.png')