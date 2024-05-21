import pyautogui
from PIL import ImageGrab
import time

# Define the RGB color of the pixel you want to click
target_color = (149,195,232)  # Red color in RGB format

# Define the region of your screen where you want to search for the pixel
# (left, top, right, bottom)
search_region = (586, 352, 1970, 949)
count=0

# Function to search for the target color pixel and click on it
def find_and_click_pixel(target_color, search_region):
    while True:
        # Capture the screen image within the defined search region
        screen = ImageGrab.grab(bbox=search_region)
        
        # Search for the target color pixel
        for x in range(screen.width):
            for y in range(screen.height):
                pixel_color = screen.getpixel((x, y))
                if pixel_color == target_color:
                    # Calculate the global coordinates of the pixel
                    global_x = 50 + x + search_region[0] # Added small offset to avoid misclicks
                    global_y = y + search_region[1]
                    
                    # Click on the pixel
                    pyautogui.click(global_x, global_y)
                    return 1
        return 0

# Call the function to start searching for the pixel and click on it
time.sleep(3)
while count<31:
    count += find_and_click_pixel(target_color, search_region)
