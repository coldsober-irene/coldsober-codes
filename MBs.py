
# turn kilobites into megabites and gigabites
def turn_mbs(var):
	output = 0
	unit = ""
	try:
		int(var)
		if int(var) < 1000:
			output += round(float(var), 1)
			unit += "KB"
		elif int(var) >= 1000 and int(var) < 1000000:
			output += round((int(var)/1000), 1)
			unit += "MB"
		elif int(var) >= 1000000 and int(var) < 1000000000:
			output += round((int(var) / 1000000), 1)
			unit += "GB"
		else:
			output += round((int(var) / 1000000000), 1)
			unit += "TB"
		return str(output) + unit
	except Exception:
		pass

print(turn_mbs(170.7889))






