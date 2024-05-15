import subprocess
import pyautogui
import time,PIL
from PIL import Image
scale_factor = 2
def get_window_bounds(app_name):
    """
    Uses AppleScript to get the bounds of the first window of the specified application.
    Returns the bounds as a tuple (x, y, width, height).
    """
    script = f'''
    tell application "System Events"
        tell process "{app_name}"
            if exists window 1 then
                set windowPos to position of window 1
                set windowSize to size of window 1
                return (item 1 of windowPos as text) & ", " & (item 2 of windowPos as text) & ", " & (item 1 of windowSize as text) & ", " & (item 2 of windowSize as text)
            else
                return ""
            end if
        end tell
    end tell
    '''
    p = subprocess.Popen(['osascript', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = p.communicate(script)
    
    if stderr or stdout.strip() == "":
        print(f"Error or no output: {stderr}")
        return None

    # Parse output
    results = stdout.strip().split(", ")
    x, y, width, height = map(int, results)
    
    return x, y, width, height

bounds = get_window_bounds("Bezel")
if bounds:
    x, y, width, height = bounds
    print(f"Window found at ({x}, {y}) with size {width}x{height}")

    # Activate the window with the provided name
    subprocess.run(['/usr/bin/osascript', '-e', f'tell app "Bezel" to activate'])

    time.sleep(1)  # Give it a second to focus on the window

    # Take a screenshot of the specific region
    screenshot = pyautogui.screenshot(region=(x*scale_factor, y*scale_factor, width*scale_factor, height*scale_factor))
    screenshot.save('screenshot.png')
    print("Screenshot saved.")


else:
    print("Window not found.")

