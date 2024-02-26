import os
import re
import json
import db

CONFIG_FILE = "config.json"

# Czy nie rozbić tego na dwie funkcje?
def read_and_archive_teams_json():
    with open(CONFIG_FILE, "r") as f:
        config_data = json.load(f)

    leagues = config_data["leagues"]
    files_path = config_data["files_path"]
    pattern = re.compile(r"^(" + '|'.join(leagues) + r")Teams.json$")

    for file in os.listdir(files_path):
        if pattern.match(file):
                teams = pd.read_json(f"{files_path}/{file}")
                print(teams.transpose())
                os.rename(f"{files_path}/{file}", f"Archive/{file}")


def read_data_from_json(file_path):
    result = []
    with open(file_path, "r") as f:
        data = json.load(f)
    for v in data.values():
        result.append(v)
    return result

def add_read_data_to_db():
    data_from_file = read_data_from_json("test1.json")
    for data in data_from_file:
            # db.add_event(event["event_name"], event["event_description"], event["player"], event["team"], event["match_time"])
        # print(data["event_name"], data["event_description"], data["player"], data["team"], data["match_time"])
        # print(data["events"])
        for event in data["events"]:
            db.add_event(event["event_name"], event["event_description"], event["player"], event["team"], event["match_time"], event["league"])


def add_leagues_from_file():
    with open(CONFIG_FILE, "r") as f:
        config_data = json.load(f)

    leagues_to_add = config_data["leagues_to_add"]
    current_leagues = config_data["leagues"]

    for league in leagues_to_add:
        db.add_leagues(league)

    current_leagues.extend(leagues_to_add)

    config_data["leagues_to_add"] = []
    config_data["leagues"] = current_leagues

    with open(CONFIG_FILE, "w") as f:
        json.dump(config_data, f)

def add_teams_from_file(files_path):
    with open(CONFIG_FILE, "r") as f:
        config_data = json.load(f)

    leagues = config_data["leagues"]

    for file in os.listdir(files_path):
        filename = os.fsdecode(file)
        if filename.replace("Teams.json", "") in leagues and filename.endswith("Teams.json"):
            full_file_path = f"{files_path}/{filename}"
            teams = read_data_from_json(full_file_path)

add_teams_from_file("Teams")

# add_leagues_from_file()
# add_leagues_from_file()

# db.add_leagues(['Premier League', 'Bundesliga'])

# d = read_data_from_json("test1.json")
# for i in d:
#     print(i["events"])

# def get_config_data():
#     result = {}

#     with open(CONFIG_FILE, "r") as f:
#         result = json.load(f)
#     return result

# def change_files_path():
#     path = input("Files path: ")

#     with open(CONFIG_FILE, "w") as f:
#         try:
#             get_config_data()
#         except FileNotFound:
            
#         f.write(path)


# def get_files_path():
#     with open(CONFIG_FILE, "r") as f:
#         files_path = f.read()


