import pyodbc

def connect_to_db():
    conn_str = (
        "Driver={SQL Server};"
        "Server=DESKTOP-DVUVJ0H;"
        "Database=FootballStatistics;"
        "Trusted_Connection=yes;"
    )
    try:
        conn = pyodbc.connect(conn_str)
        print("Connected to database")
        return conn
    except Exception as e:
        print("Can't connect with database, check connection parameters")
        print(f"Error: {e}")
        exit()

def add_event(event, player, home_team, away_team, event_team, match_external_id, league):
    with connect_to_db() as conn:
        sql = f"EXEC {league}.AddRawData ?, ?, ?, ?, ?, ?"
        cursor = conn.cursor()
        cursor.execute(sql, event, player, home_team, away_team, event_team, match_external_id, league)
        conn.commit()

def add_leagues(league):
    with connect_to_db() as conn:
        # for league in leagues:
        # sql = "EXEC dbo.AddLeague ?"
        # data = list( (row,) for row in leagues)
        # print(data)
        cursor = conn.cursor()
        # cursor.executemany(sql, data)
        cursor.execute("EXEC dbo.AddLeague ?", league)
        conn.commit()              

def add_team(short_name, long_name, founding_date, address, league):
    with connect_to_db() as conn:
        sql = f"EXEC {league}.AddTeam ?, ?, ?, ?"
        cursor = conn.cursor()
        cursor.execute(sql, short_name, long_name, founding_date, address, league)
        conn.commit()

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
