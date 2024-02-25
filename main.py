import menu
import operations
import pyodbc
import db

# cnxn = pyodbc.connect("Driver={SQL Server};"
#                       "Server=DESKTOP-DVUVJ0H;"
#                       "Database=test;"
#                       "Trusted_Connection=yes;")

# cursor = cnxn.cursor()
# cursor.execute('SELECT getdate()')
# print(cursor)

# query = 'SELECT 234'

# cursor.execute('select 123')
# print(cursor.fetchall())
# cnxn.close()
class Manager:

    def __init__(self):
        self.is_running = True
        self.choices = {
            #"2": operations.change_file_path,
            "3": operations.add_leagues_from_file,
            "4": self.quit
        }
        self.start()

    def start(self):
        while self.is_running:
            # db.add_event()
            
            menu.show_menu()
            user_choice = menu.get_choice()
            self.choices.get(user_choice)()
            

    def quit(self):
        self.is_running = False

db.create_db()
Manager()
