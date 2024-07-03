from pythonclimenu import menu

OPTIONS = ["Option 1", "Option 2", "Option 3", "Quit"]

# Creates a simple console menu with blue cursor
menu1 = menu(title="Amazing Console Menu", options=OPTIONS, cursor_color="blue")

menu2 = menu(
    title = ["Amazing Console", "Menu"], # displays title on multiple lines
    options = OPTIONS,
    cursor_color = (255, 95, 46), # sets the cursor color using RGB values
    title_color = [
        "blue", # colors "Amazing Console"
        "light_red" # colors "Menu"
    ],
    initial_cursor_position = -1 # sets cursor default position to 'Quit'
)

menu3 = menu(
    title = ["Amazing Console", "Menu"], # displays title on multiple lines
    options = OPTIONS,
    cursor_color = "yellow",
    title_color = "light_green", # colors all lines of title
    options_color = [
        "magenta", # colors options[0]
        "light_cyan", # colors options[1]
        (192, 11, 168) # colors options[2]
        # option[3] color is not specifed so it will be considered as None
    ],
    initial_cursor_position = OPTIONS[1] # sets cursor default position to 'Option 1'
)