import menu
import operations

class Manager:

    def __init__(self):
        self.is_running = True
        self.choices = {
            "1": operations.read_and_archive_raw_data_json,
            "2": operations.read_and_archive_teams_json,
            "3": operations.add_leagues_from_file,
            "5": self.display_sub_menu_settings,
            "6": self.quit
        }
        self.choices_sub_menu_settings = {
            "1": self.sub_menu_change_event_files_path,
            "2": self.sub_menu_change_match_files_path,
            "3": operations.sub_menu_show_files_path,
            "4": self.sub_menu_go_to_main_menu
        }
        self.start()

    def start(self):
        while self.is_running:
            menu.show_menu()
            user_choice = menu.get_choice()
            # try:
            self.choices.get(user_choice)()
            # except FileNotFoundError:
                # print("File doesn't exist")
    
    def display_sub_menu_settings(self):
        menu.show_sub_menu()
        user_choice = menu.get_choice()
        self.choices_sub_menu_settings.get(user_choice)()

    def sub_menu_change_event_files_path(self):
        new_path = input("New path: ")
        operations.change_event_files_path(new_path)

    def sub_menu_change_match_files_path(self):
        new_path = input("New path: ")
        operations.change_team_files_path(new_path)
    
    def sub_menu_go_to_main_menu(self):
        self.start()
            
    def quit(self):
        self.is_running = False

if __name__ == "__main__":
    Manager()
