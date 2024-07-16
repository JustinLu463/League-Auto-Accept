League Auto Accept:
- This repository contains a script that automatically accepts League of Legends games by detecting and clicking the accept button.


Contents:
- league_auto_accept.py: Main script to run the auto accept feature.
- location.py: Helper script to determine the location of the accept button on the screen.
- league_accept_button.png: Image of the accept button used for detection.

Prerequisites to run this script, you'll need the following:
- Python 3.x
- opencv-python library
- pyautogui library

You can install the required libraries using pip:
- pip install opencv-python pyautogui


How It Works:
- The script performs the following steps:
- Continuously captures the screen and looks for the accept button using the provided league_accept_button.png image.
- If the accept button is found, it moves the mouse to the button's location and clicks it.

Important Notes:
- Make sure your game is running in windowed mode for better performance.
- The script uses image recognition to detect the accept button, so it may not work if the button's appearance changes.

Customization:
- If the location of the accept button on your screen is different, you can update the location.py script to return the correct coordinates.
