import os
import re
import json
import db
# import pandas as pd

CONFIG_FILE = "config.json"

def read_and_archive_teams_json():
    with open(CONFIG_FILE, "r") as f:
        config_data = json.load(f)

    leagues = config_data["leagues"]
    files_path = config_data["team_files_path"]
    pattern = re.compile(r"^(" + '|'.join(leagues) + r")Teams.json$")

    for file in os.listdir(files_path):
        if pattern.match(file):
                teams = pd.read_json(f"{files_path}/{file}").transpose()
                os.rename(f"{files_path}/{file}", f"Archive/{file}")
                league = file.replace("Teams.json", "")
                db.add_team(teams, league)


def read_and_archive_raw_data_json():
    with open(CONFIG_FILE, "r") as f:
        config_data = json.load(f)

    leagues = config_data["leagues"]
    files_path = config_data["event_files_path"]
    pattern = re.compile(r"^(" + '|'.join(leagues) + r")\d+.json$")

    for file in os.listdir(files_path):
        if pattern.match(file):
                with open(f"{files_path}/{file}", encoding="utf-8") as data_file:
                    events = json.load(data_file)
                df = pd.json_normalize(events, "events", ["home_team", "away_team", "league", "external_match_id"],
                            record_prefix="events_")
                df_matches = pd.DataFrame(df.where(df["events_event"] == "match_start"))
                df_matches = df_matches.dropna(how='all')
                df_matches["is_finished"] = 0 
                league = re.sub(r"(\d|.json)", "", file)
                db.add_match(df_matches, league)
                db.add_event(df, league)
                os.rename(f"{files_path}/{file}", f"Archive/{file}")

def change_event_files_path(new_path):
    # try:
    with open(CONFIG_FILE, "r") as f:
        config_data = json.load(f)
    # except Exception:
        # print("Config file not found")
    # except ValueError:
        # raise ValueError("Can't open JSON file")
    config_data["event_files_path"] = new_path
    with open(CONFIG_FILE, "w") as f:
        json.dump(config_data, f)

def change_team_files_path(new_path):
    with open(CONFIG_FILE, "r") as f:
        config_data = json.load(f)
    config_data["team_files_path"] = new_path
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config_data, f)


def clear_console(func):
    os.system("cls")


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


def sub_menu_show_files_path():
    with open(CONFIG_FILE, "r") as f:
        config_data = json.load(f)
    for x, y in config_data.items():
        print(x + ":", y)

