menu = (
    "1. Import events files\n"
    "2. Import teams files\n"
    "3. Change files' folder path\n"
    "4. Add leagues\n"
    "5. Quit\n"
)


def show_menu():
    print(menu)


def get_choice():
    return input("Enter choice: ")
