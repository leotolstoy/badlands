import numpy as np 


from demographics import DemographicsModel
from city import CityModel






class State():
	def __init__(self):


		self.major_cities = [CityModel()]
		self.population = []
		self.vote_margin = []
		self.demographics = DemographicsModel()


		self.voteMargin = 0
		self.yearToFlip = []
		self.turnout = 0.5





