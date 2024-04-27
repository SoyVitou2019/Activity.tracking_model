import tkinter as tk
import mss
import mss.tools
from datetime import datetime

def capture_screen(screen_number):
    root.attributes("-alpha", 0)  # Set tkinter window to be transparent
    root.attributes("-fullscreen", True)  # Set tkinter window to be fullscreen
    root.overrideredirect(True)  # Remove window decorations
    with mss.mss() as sct:
        # Get information of the selected monitor
        mon = sct.monitors[screen_number]

        # The screen part to capture
        monitor = {
            "top": mon["top"],
            "left": mon["left"],
            "width": mon["width"],
            "height": mon["height"],
            "mon": screen_number,
        }
        # Generate image name based on current time
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output = f"./dataset/enjoying/sct-mon{screen_number}_{current_time}.png"

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        print(f"Screenshot saved as {output}")
    root.attributes("-alpha", 1)  # Restore transparency of tkinter window
    root.attributes("-fullscreen", False)  # Restore tkinter window to normal size
    root.overrideredirect(False)  # Restore window decorations

def capture_screen1():
    capture_screen(1)

def capture_screen2():
    capture_screen(2)

# Create main tkinter window
root = tk.Tk()
root.title("Screen Capture")
root.attributes("-topmost", True)  # Set window to always stay on top

# Create buttons for each screen
btn_screen1 = tk.Button(root, text="Capture Screen 1", command=capture_screen1)
btn_screen1.pack(padx=80, pady=30)

btn_screen2 = tk.Button(root, text="Capture Screen 2", command=capture_screen2)
btn_screen2.pack(padx=80, pady=30)

# Run the tkinter event loop
root.mainloop()
