


### SETTINGS
# classe che si occupa di leggere e scrivere la configurazione



class Settings:
	def readParam(self, param):
		if param == "Logic":
			return "first_one_wins"