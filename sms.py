import mysql.connector
import getpass
import os
from rich.console import Console
from rich.theme import Theme

#color of the system
color_theme = Theme({
    'tb':"#7fffd4", #topbar color
    'f':"#FF847C",# frame color
    't':"#FECEAB", #text color
    'n':"#FF847C" #notification color
})
rc= Console(theme = color_theme)

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sms"
)

cursor = db.cursor()

clear = lambda: os.system('cls')


def create_table():
    # SQL query to create students table
    create_table_query = """
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            student_id INT NOT NULL,
            password VARCHAR(255) NOT NULL
        )
    """
    cursor.execute(create_table_query)
    print("Table 'students' created successfully.")

def login():
    clear()
    rc.print("""

          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••___•••••[/tb]
          [tb]|                       [t]Student Management System [/t]             [f]-[/f]  [f]|_|[/f]  [f]X[/f] |[/tb]
          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••[/tb]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [tb]•                          [t]█░░ █▀█ █▀▀ █ █▄░█[/t]                            •[/tb]
          [tb]•                          [t]█▄▄ █▄█ █▄█ █ █░▀█[/t]                            •[/tb]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [tb]••••••••••[f]••••••••••[/f]•••••••••[tb]••••••••••[/tb]••••••••••[f]••••••••••[/f]••••••••[tb]•••••••[/tb]

""")
    student_id = str(rc.input("\t  [t]Enter student ID[/t] [n]:[/n] "))
    password = getpass.getpass("\t  Enter password: ")

    query = "SELECT * FROM students WHERE student_id = %s AND password = %s"
    cursor.execute(query, (student_id, password))
    user = cursor.fetchone()

    if user:
        return student_id
    else:
        print("Invalid student ID or password.")
        return None

def homepage(student_id):
    clear()
    rc.print(f"""

          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••___•••••[/tb]
          [tb]|                       [t]Student Management System [/t]             [f]-[/f]  [f]|_|[/f]  [f]X[/f] |[/tb]
          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••[/tb]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [tb]•         [t]█▀ ▀█▀ █░█ █▀▄ █▀▀ █▄░█ ▀█▀ ▀ █▀   █▀▄▀█ █▀▀ █▄░█ █░█[/t]          •[/tb]
          [tb]•         [t]▄█ ░█░ █▄█ █▄▀ ██▄ █░▀█ ░█░ ░ ▄█   █░▀░█ ██▄ █░▀█ █▄█[/t]          •[/tb]
          [f]•                                                                        •[/f]
          [f]•                     Welcome, Student ID: {student_id}!                    •[/f]
          [f]•                                                                        •[/f]
          [tb]•                    [t][[n]1[/n]][t]. View your information[/t]                          •[/tb]
          [tb]•                    [t][[n]2[/n]][t]. Update your information[/t]                        •[/tb]
          [tb]•                    [t][[n]3[/n]][t]. Logout[/t]                                         •[/tb]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [tb]••••••••••[f]••••••••••[/f]•••••••••[tb]••••••••••[/tb]••••••••••[f]••••••••••[/f]••••••••[tb]•••••••[/tb]

""")

def main():
    create_table()

    logged_in = False
    student_id = None

    while True:
        if not logged_in:
            clear()
            rc.print("""

          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••___•••••[/tb]
          [tb]|                       [t]Student Management System [/t]             [f]-[/f]  [f]|_|[/f]  [f]X[/f] |[/tb]
          [tb]••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••[/tb]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [tb]•                             [[n]1[/n]]. [t]Login[/t]                                 •[/tb]
          [tb]•                             [[n]2[/n]]. [t]Exit[/t]                                  •[/tb]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [f]•                                                                        •[/f]
          [tb]••••••••••[f]••••••••••[/f]•••••••••[tb]••••••••••[/tb]••••••••••[f]••••••••••[/f]••••••••[tb]•••••••[/tb]

""")
            choice = str(rc.input("\t  [t]Option[/t] [n]:[/n] "))

            if choice == "1":
                student_id = login()
                if student_id:
                    logged_in = True
            elif choice == "2":
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            homepage(student_id)
            choice = str(rc.input("\t  [t]Option[/t] [n]:[/n] "))

            if choice == "3":
                logged_in = False
                student_id = None
            else:
                print("Invalid choice. Please try again.")
                continue

if __name__ == "__main__":
    main()
