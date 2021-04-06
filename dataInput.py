import configManager
input_data = []

def dataInputHelper():
	global input_data
	input_data.clear()
	info = configManager.readConfig()
	for i in info:
		a = info[i]
		arr = [x for x in a.split("subscriber_id: ")]
		b = arr[1]
		b = b.replace('"','')
		input_data.append(b)
	return input_data