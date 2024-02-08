def change_file_path():
    path = input("Files path: ")

    with open("config.csv", "w") as f:
        f.write(path)
