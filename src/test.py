import pandas as pd
import json
import os
import re
import db

# regex na kolejki
# ^(Bundesliga|PremierLeague)\d+.json$

CONFIG_FILE = "config.json"
with open(CONFIG_FILE, "r") as f:
        config_data = json.load(f)

leagues = config_data["leagues"]
files_path = config_data["files_path"]
pattern = re.compile(r"^(" + '|'.join(leagues) + r")Teams.json$")

for file in os.listdir(files_path):
        if pattern.match(file):
                teams = pd.read_json(f"{files_path}/{file}").transpose()
                league = file.replace("Teams.json", "")
                db.add_team(teams, league)
                # params = (teams["short_name"], teams["long_name"], teams["founding_date"], teams["addres"], league) # czy tak bedzie ok?
                # print(params, league)
                # db.add_team(*params)
                # os.rename(f"{files_path}/{file}", f"Archive/{file}")

#         pattern = re.compile(r"")

#         if file
        # if filename.replace("Teams.json", "") in leagues and filename.endswith("Teams.json"):
        #     full_file_path = f"{files_path}/{filename}"
        #     teams = read_data_from_json(full_file_path)

# normalizacja

# with open('test1.json') as data_file:
#     data = json.load(data_file)
# print(data)
# df = pd.json_normalize(data, 'events', ['home_team', 'away_team', 'league'],
#                     record_prefix='events_')
# print (df)

# import pandas as pd


# threshold = pd.read_json("test1.json")
# threshold['testcolumn'] = pd.DataFrame.from_records(threshold['events'])['testcolumn']
# print(threshold)
# df = pd.DataFrame(pd.read_json("test1.json"))
# df_events = df["events"]
# df_test = pd.DataFrame()
# print(df)






# test = {"event": [], "player": [], "event_team": []}
# for i in df_events:
#     for j in i:
#         test["event"].append(j["event"])
#         test["player"].append(j["player"])
#         test["event_team"].append(j["event_team"])
#         # if test:
#         #     test = test | j
#         # else:
#         #     test = j
# df_2 = pd.DataFrame(test)
# # print(df_2)
# df_conc = pd.concat([df,df_2], axis=1)
# print(df_conc[["home_team", "away_team", "league", "event", "player", "event_team"]])
         
         
# for i in df["events"]:
#     df2 = pd.DataFrame(i)
#     print(df2)
        # df2 = pd.DataFrame([j])
        # print(df2)

# import os
# import re

# #DEFINED_FILE_NAMES = ['aaa', 'bbb', 'ccc']
# # files = ['aaa123.csv', 'aaa2.csv', 'aaa3.csv', 'ddd3.csv', 'ccc2.csv']

# #wczytac z configa tabele tez
# # dodac log bledow

# #zrobic dynamicznie budowany slownik

# # tutaj chyba bardziej procedury
# PATTERNS = {
#     'history': re.compile(r'^history\d*(.csv|.txt|.json)$'),
#     'document': re.compile(r'^document\d*(.csv|.txt|.json)$'),
#     'general': re.compile(r'^(document|history)\d*(.csv|.txt|.json)$'),
# }

# FILES_PATH = 'data'

# # a ten pattern chyba bedzie ok
# #PATTERN = re.compile(r'^(aaa|bbb|ccc)\d*(.csv|.txt|.json)$')


# file_names = os.listdir('data')

# #PATTERN = PATTERNS['general']

# filtered_file_names = list(filter(PATTERNS['general'].match, file_names))


# for filtered_file_name in filtered_file_names:
#     file = re.sub(r'\d*','', filtered_file_name).split('.')[0]

#     if file = history:
#         pass
#     # if re.search(, filtered_file_name)
#     # print(filtered_file_name)
#     # regex sprobowac

#     # if file_name.split('.')[0] in DEFINED_FILE_NAMES:
#     #     with open(f'data/{file_name}', 'r') as f:
#     #         print(f.read())


# #568
# # print(re.match('add*', 'asd1'))

# # pattern = re.compile(r'(aaa|bbb|ccc).')
# #
# # a = list(filter(pattern.match, files))
# # print(a)



# import re
#
# mylist = ["dog", "cat", "wildcat", "thundercat", "cow", "hooo"]
# r = re.compile(".*cat")
# newlist = list(filter(r.match, mylist)) # Read Note below
# print(newlist)