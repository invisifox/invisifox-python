import requests
import random
from time import sleep

class InvisiFox:
	def __init__(self,apiKey=None,proxyUsername=None,proxyPassword=None,attempts=20,logs=False):
		self.apiString = "https://api.invisifox.com/"
		self.apiKey = apiKey
		self.proxyUsername = proxyUsername
		self.proxyPassword = proxyPassword
		self.attempts = attempts
		self.logs = logs
		self.proxyCountriesList = ['Random', 'UnitedStates', 'Canada', 'Afghanistan', 'Albania', 'Algeria', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Belarus', 'Belgium', 'BosniaandHerzegovina', 'Brazil', 'BritishVirginIslands', 'Brunei', 'Bulgaria', 'Cambodia', 'Cameroon', 'Canada', 'Chile', 'China', 'Colombia', 'CostaRica', 'Croatia', 'Cuba', 'Cyprus', 'Czechia', 'Denmark', 'DominicanRepublic', 'Ecuador', 'Egypt', 'ElSalvador', 'Estonia', 'Ethiopia', 'Finland', 'France', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Guatemala', 'Guyana', 'HashemiteKingdomofJordan', 'HongKong', 'Hungary', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Kazakhstan', 'Kenya', 'Kosovo', 'Kuwait', 'Latvia', 'Liechtenstein', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malaysia', 'Mauritius', 'Mexico', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Nepal', 'Netherlands', 'NewZealand', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palestine', 'Panama', 'PapuaNewGuinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'PuertoRico', 'Qatar', 'RepublicofLithuania', 'RepublicofMoldova', 'Romania', 'Russia', 'SaudiArabia', 'Senegal', 'Serbia', 'Seychelles', 'Singapore', 'Slovakia', 'Slovenia', 'Somalia', 'SouthAfrica', 'SouthKorea', 'Spain', 'SriLanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Thailand', 'TrinidadandTobago', 'Tunisia', 'Turkey', 'Uganda', 'Ukraine', 'UnitedArabEmirates', 'UnitedKingdom', 'UnitedStates', 'Uzbekistan', 'Venezuela', 'Vietnam', 'Zambia']

	def pprint(self,content):
		if self.logs:
			print(content)

	def solveHCaptcha(self,sitekey,pageurl,proxy,rqdata=None,useragent=None,cookies=None,invisible=False):
		if self.apiKey == None:
			raise Exception('No API key set. You can set it on the invisiFox class init or directly onto the class object. If you do not have an invisiFox API key please create an account on invisiFox.com to get one.')
		else:
			payload = {
				"token": self.apiKey,
				"siteKey": sitekey,
				"pageurl": pageurl,
				"proxy": proxy,
				"rqdata": rqdata,
				"useragent": useragent,
				"cookies": cookies,
				"invisible": invisible
			}
			req = requests.get(url=f"{self.apiString}hcaptcha", params=payload)
			if req.status_code == 200:
				req = req.json()
				self.pprint(req)
				if req['status'] == 'OK':
					sleep(15)
					for i in range(self.attempts):
						payload = {"token": self.apiKey,"taskId": req['taskId']}
						sol = requests.get(f"{self.apiString}solution", params=payload).json()
						self.pprint(sol)
						if sol['status'] == 'WAITING':
							sleep(10)
						elif sol['status'] == 'OK':
							return sol['solution']
						elif sol['status'] == 'error':
							raise Exception(f"Error {sol['message']}")
						else:
							raise Exception(f"Error {sol['status']}")
					raise Exception(f"Error could not find solution in time")
				else:
					raise Exception(f"Error {req['status']}")
			else:
				raise Exception(f"Error {req.json()['status']}")


	def makeProxy(self,country="Random",proxyType="random",protocol="http",count=1):
		country = country.replace(' ','')
		if self.proxyUsername == None or self.proxyPassword == None:
			raise Exception('No Proxy Username and / or Proxy Password set. You can set them on the invisiFox class init or directly onto the class object. If you do not have invisiFox proxy credentials please create an account on invisiFox.com to get them.')
		else:
			if protocol not in ['http','https']:
				raise Exception('Unsupported protocol, please use http or https only')
			elif count <= 0:
				raise Exception('Please specific a count >0')
			elif country not in self.proxyCountriesList:
				raise Exception('Country not supported, please check our country list in our API documentation for list of supported geos')
			else:
				countryType = '_country-'+country
				if countryType == '_country-Random':
					countryType = ''

				ansArr = []

				if proxyType == 'random':
					for _ in range(count):
						ansArr.append(f"{protocol}://{self.proxyUsername}:{self.proxyPassword}{countryType}@proxy.invisifox.com:80")
				elif proxyType == 'sticky':
					for _ in range(count):
						ansArr.append(f"{protocol}://{self.proxyUsername}:{self.proxyPassword}{countryType}_session-{''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') for i in range(8))}@proxy.invisifox.com:80")
				else:
					raise Exception('Unsupported proxy type, please use random or sticky only')

				return ansArr

