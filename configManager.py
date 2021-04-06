from configparser import ConfigParser

def writeConfig(dict1 ={}):
	#Get the configparser object
	config_object = ConfigParser()

	#Assume we need 2 sections in the config file, let's call them USERINFO and SERVERCONFIG
	config_object["USERINFO"] = dict1

	#Write the above sections to config.ini file
	with open('config.ini', 'w') as conf:
	    config_object.write(conf)


def readConfig():

	#Read config.ini file
	config_object = ConfigParser()
	config_object.read("config.ini")

	#Get the password
	userinfo = config_object["USERINFO"]
	return userinfo