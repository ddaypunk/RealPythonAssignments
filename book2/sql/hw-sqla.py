#hw-sqla.py

import sqlite3

with sqlite3.connect("cars.db") as conn:
	c = conn.cursor()

	try:
		c.execute("""CREATE TABLE inventory
	(make TEXT, model TEXT, quantity INT)
				""")

	except sqlite3.OperationalError:
		print "Table already exists."