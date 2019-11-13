#hw-sqlb.py

import sqlite3

with sqlite3.connect("cars.db") as conn:
	c = conn.cursor()

	cars = [
			('Ford','Mustang',25),
			('Ford','F-150',15),
			('Ford','Fusion',35),
			('Honda','Pilot',20),
			('Honda', 'C-RV',17)
			]

	try:
		# first I inserted the above rows
		#c.executemany('INSERT INTO inventory VALUES (?,?,?)', cars)

		#then I updated quantity on two of them
		#c.execute("UPDATE inventory SET quantity = 30 WHERE model='Mustang'")
		#c.execute("UPDATE inventory SET quantity = 25 WHERE model='C-RV'")

		#lastly, I will output the values
		c.execute("SELECT make, model, quantity FROM inventory WHERE make='Ford'")
		rows = c.fetchall()

		for r in rows:
			print "{} {} \tQuantity: {}".format(r[0], r[1], r[2])

	except sqlite3.OperationalError:
		print "Something went wrong, fix and try again"