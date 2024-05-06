import pygetwindow as gw

def set_resolution(width, height):
    # Get the primary display
    screen = gw.getWindowsWithTitle('Program Manager')[0]
    screen.moveTo(0, 0)
    screen.resizeTo(width, height)

# Example usage
set_resolution(1920, 1080)
