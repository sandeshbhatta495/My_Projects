import pyautogui
import datetime
import os

def take_screenshot(save_dir="screenshots"):
    # Create directory if it doesn't exist
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    # Get current timestamp for unique file name
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"screenshot_{timestamp}.png"
    file_path = os.path.join(save_dir, file_name)

    # Take the screenshot
    screenshot = pyautogui.screenshot()
    screenshot.save(file_path)
    print(f"Screenshot saved to: {file_path}")

# Example usage
take_screenshot()
