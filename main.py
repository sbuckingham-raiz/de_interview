from src.Postgres import Postgres

TABLE_DDL = "CREATE TABLE IF NOT EXISTS data (acctnbr NUMERIC, memberagreenbr NUMERIC, rtxnnbr NUMERIC, tranamt NUMERIC, rtxntypcd TEXT, postdate DATE)"


postgres = Postgres()
connection = postgres.connect()




connection.close()