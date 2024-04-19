import cv2
import numpy as np
import time
import pyautogui
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# user gmail and app password
gmail_user = 'enter your email here'
gmail_password = 'your gmail app password here' 

# what address should receive email
recipient_email = 'enter your email here'

# what is going to be sent and the message
subject = "League Time!"
body = "You're in a game, hurry back!"

def send_email():
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(gmail_user, gmail_password)
        text = msg.as_string()
        server.sendmail(gmail_user, recipient_email, text)
        server.quit()
        print("Notification sent via email.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def screen_capture():
    # this part takes a screenshot of your screen using pyautogui
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    return screenshot

def find_accept_button(screenshot, template):
    # this converts screenshot to gray scale for processing
    gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    # read the template in gray scale
    template = cv2.imread(template, 0)
    w, h = template.shape[::-1]

    # match the template using cv2.matchTemplate
    res = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):  # if the template is found in the screenshot
        return True
    return False

# reference for the picture you're using as reference
template_path = 'insert image path here'

while True:
    current_screen = screen_capture()
    if find_accept_button(current_screen, template_path):
        # this part is where the mouse location will be set to
        pyautogui.click(x=961, y=697)
        pyautogui.click(button='left')
        send_email()
        break  
    time.sleep(2)  # check every 2 seconds