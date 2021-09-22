import sqlite3 as sq

class do_db:
	def __init__(self, dbs):
		self.dbs = dbs
		self.conns = []
		self.curs = []

	def create_db(self):
		for db in self.dbs:
			conn = sq.connect(f"{db}")
			self.conns.append(conn)
		print("my conections: ",self.conns)

	def create_tb(self, tbls):
		start = 0
		for tb in tbls:
			c = self.conns[start].cursor()
			self.curs.append(c)
			start += 1

		for cur in self.curs:
			cur.execute(f"""CREATE TABLE IF NOT EXISTS {tbls.keys()}({tbls[tbls.keys()]})""")
			print("successfully done!")

	def insert_to(self, database, table, data, *placeholder):
		conn = sq.connect(database)
		c = conn.cursor()
		command = f"INSERT INTO {table} VALUES{placeholder}"
		c.executemany(command, data)

	def readall_to(self, dababase, table):
		conn = sq.connect(database)
		c = conn.cursor()
		command = f"SELECT * FROM {table}"
		fetched_data = c.execute(command)
		return fetched_data

tables = {"stock" :["id integer PRIMARY KEY",
                      "buyer text",
                      "item text",
                      "quantity real",
                      "unit text",
                      "selling_price real",
                      "total real",
                      "date text",
                      "status text",
                      "week integer",
                      "decision text"]}

databases = ["store.db", "pay.db", "exp.db", "cred.db", "telephones.db", "sales.db"]

first_round = do_db(databases)
#first_round.create_tb(tables)