import menu
import operations

class Manager:
    def __init__(self):
        self.is_running = True
        self.choices = {
            "2": operations.change_file_path,
            "3": self.quit
        }
        self.start()

    def start(self):
        while self.is_running:
            menu.show_menu()
            user_choice = menu.get_choice()
            self.choices.get(user_choice)()

    def quit(self):
        self.is_running = False


Manager()
