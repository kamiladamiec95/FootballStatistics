import pyodbc
import sqlalchemy
import pandas as pd

def connect_to_db():
    engine = sqlalchemy.create_engine('mssql+pyodbc://@DESKTOP-DVUVJ0H/FootballStatistics?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server')
    return engine

def add_event(events, league):
    with connect_to_db().begin() as conn:
        events = events.rename(columns={"events_event": "Event", "events_player": "Player", "events_event_team": "Team", "external_match_id": "MatchExternalId"})
        events = events.drop(columns=["league", "away_team", "home_team"])
        events.to_sql(name="RawData", if_exists='append', con=conn, index=False, schema=f"{league}")

def add_match(events, league):
    print(events)
    for index, row in events.iterrows():
        home_team = row["home_team"]
        away_team = row["away_team"]
        is_finished = row["is_finished"]
        external_match_id = row["external_match_id"]
        query = f"EXEC {league}.AddMatch @HomeTeamName='%s', @AwayTeamName='%s', @MatchExternalId='%s', @IsFinished='%s'" % (home_team, away_team, external_match_id, is_finished)
        with connect_to_db().begin() as conn:
            conn.execute(sqlalchemy.text(query))

def read_matches(league):
    query = f"SELECT * FROM {league}.Matches"
    with connect_to_db().begin() as conn:
        df = pd.read_sql(query, conn)
      
def add_leagues(league):
    with connect_to_db().begin() as conn:
        cursor = conn.cursor()
        cursor.execute("EXEC dbo.AddLeague ?", league)
        conn.commit()              

def add_team(teams, league):
    with connect_to_db().begin() as conn:
        teams = teams.rename(columns={"short_name": "ShortName", "long_name": "LongName", "founding_date": "FoundingDate", "addres": "Address"})
        teams.to_sql(name="Teams", if_exists='append', con=conn, index=False, schema=f"{league}")

def create_db():
    conn_str = (
        "Driver={SQL Server};"
        "Server=DESKTOP-DVUVJ0H;"
        "Database=master;"
        "Trusted_Connection=yes;"
    ) 

    cnxn = pyodbc.connect(conn_str, autocommit=True)

    cursor = cnxn.cursor()
    create_db_query = """IF DB_ID('FootballStatistics') IS NULL
                            CREATE DATABASE FootballStatistics"""
    
    cursor.execute(create_db_query)
    # cnxn.commit()

#     create_procedure_AddLeague = """
#     USE FootballStatistics
#     GO
#     CREATE PROCEDURE [dbo].[AddLeague]
# (
# 	@LeagueName nvarchar(255)
# )
# AS
# BEGIN

# declare @sql varchar(max)

# set @sql = 'CREATE SCHEMA ' + @LeagueName

# EXEC(@sql)

# set @sql = 'CREATE TABLE [' + @LeagueName + '].[Matches](
# 	[Id] [int] IDENTITY(1,1) NOT NULL,
# 	[HomeTeamId] [int] NOT NULL,
# 	[HomeTeamScore] [int] NULL,
# 	[AwayTeamId] [int] NULL,
# 	[AwayTeamScore] [int] NULL,
# 	[MatchExternalId] [bigint] NULL
#  CONSTRAINT [PK_' + @LeagueName +'Matches] PRIMARY KEY CLUSTERED 
# (
# 	[Id] ASC
# )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
# ) ON [PRIMARY]'

# EXEC(@sql)


# set @sql = 
# 'CREATE TABLE [' + @LeagueName + '].[RawData](
# 	[Id] [int] IDENTITY(1,1) NOT NULL,
# 	[Event] [varchar](255) NULL,
# 	[Player] [nvarchar](100) NULL,
# 	[Team] [nvarchar](80) NULL,
# 	[MatchExternalId] bigint NULL
#  CONSTRAINT [PK_' + @LeagueName + 'RawData] PRIMARY KEY CLUSTERED 
# (
# 	[Id] ASC
# )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
# ) ON [PRIMARY]'

# EXEC(@sql)


# set @sql = 
# 'CREATE TABLE [' + @LeagueName + '].[Teams](
# 	[Id] [int] IDENTITY(1,1) NOT NULL,
# 	[ShortName] [nvarchar](80) NULL,
# 	[LongName] [nvarchar](255) NULL,
# 	[FoundingDate] [date] NULL,
# 	[Address] [nvarchar](300) NULL
#  CONSTRAINT [PK_' + @LeagueName + 'Teams] PRIMARY KEY CLUSTERED 
# (
# 	[Id] ASC
# )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
# ) ON [PRIMARY]'

# EXEC(@sql)

# SET @sql = 
# 'CREATE PROCEDURE [' + @LeagueName + '].[AddTeams]
# (
# 	@ShortName varchar(80),
# 	@LongName varchar(255),
# 	@FoundingDate date,
# 	@Address nvarchar(30)
# )
# AS
# BEGIN

# 	INSERT INTO ' + @LeagueName + '.Teams ([ShortName], [LongName], [FoundingDate], [Address])
# 	SELECT @ShortName, @LongName, @FoundingDate, @Address

# END'


# END"""

#     cursor.execute(create_procedure_AddLeague)
#     cnxn.commit()
