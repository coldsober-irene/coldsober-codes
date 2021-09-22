
import sqlite3 as sq

# create database
class db:
	def __init__(self, db_name, conn):
		self.my_db = db_name
		self.conn = conn
		self.dict_database = []

	def create_db(self):
		i = 0
		for conns in self.conn:
			conns = sq.connect(self.my_db[i])
			self.dict_database.append(conns)
			print(f"database {self.my_db} created successfully")
			i += 1

	def create_tables(self,c,table_name):
		# create cursor
		#c = None
		i = 0
		j = 0
		for co in self.dict_database:
		
			c[i] = co.cursor()
			i += 1
		
		dict_tableName = dict(table_name)
		for tab in dict_tableName.keys():
			c[j].execute(f"""CREATE TABLE IF NOT EXISTS {tab}({dict_tableName[tab]})""")
			print(f"successfully created table {tab}")
			j += 1

tables = {"table20":["name text", "class integer", "decision text"], 
			"table21":["age integer", "religion text"],
			"table22":["wall text", "class integer", "decision text"], 
			"table23":["rate integer","belief real", "religion text"],
			"table24":["greate text", "class integer", "decision text"]
			}

cursors = ["c1", "c2", "c3", "c4", "c5"]
db1 = db(["cold.db", "irene.db", "serevision.db", "fud.db", "kaduhisger.db"], ["cold_conn", "i_conn", "s_conn", "f_conn","k_conn"])
db1.create_db()

db1.create_tables(cursors, tables)