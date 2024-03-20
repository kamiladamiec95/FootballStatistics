from mcr.microsoft.com/mssql/server:2019-latest

env SA_PASSWORD: YourStrongPassw0rd\
    ACCEPT_EULA: Y

expose 1433

copy ./Create_db.sql .
copy ./entrypoint.sh .
user root
run chmod +x ./entrypoint.sh
user mssql
entrypoint ["./entrypoint.sh"]
