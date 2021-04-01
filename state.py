import numpy as np 


from demographics import DemographicsModel
from city import CityModel
from logisticBayesianModel import LogisticBayesianModel





class State():
	def __init__(self,p1,p2,p3,p4):

		# TODO: make turnout model it's own bi-mean thing
		# TODO: make reg voter model, vote margin model, and population model polynomial/logistic/1st order, have them inherit from BayesianModel

		self.overallPopulationModel = LogisticBayesianModel(p1)
		self.overallTurnoutModel = LogisticBayesianModel(p2)
		self.overallRegVoterModel = LogisticBayesianModel(p3)
		self.overallVoteMarginModel = LogisticBayesianModel(p4)

		# self.major_cities = [CityModel()]
		self.demographics = dict([\
			('college_ed',DemographicsModel(self.overallPopulationModel, self.overallTurnoutModel, self.overallRegVoterModel, self.overallVoteMarginModel)),\
			('overall',DemographicsModel(self.overallPopulationModel, self.overallTurnoutModel, self.overallRegVoterModel, self.overallVoteMarginModel)),\
			])  

		self.totalPopulation = self.demographics['overall'].evalModelAtTime(0)
		self.overallVoteMargin = self.demographics['overall'].evalModelAtTime(0)
		self.overallRegVoter = self.demographics['overall'].evalModelAtTime(0)
		self.overallTurnout = self.demographics['overall'].evalModelAtTime(0)

		self.totalVotes = self.overallTurnout * self.overallRegVoter
		self.frac_overall_dem = 0.5 + self.overallVoteMargin/2
		self.frac_overall_rep = 0.5 - self.overallVoteMargin/2

		self.overall_dem_votes = self.frac_overall_dem * self.totalVotes
		self.overall_rep_votes = self.frac_overall_rep * self.totalVotes

		self.yearToFlip = []


		def resampleDemographicsModel(key):
			self.demographics[key].sampleModel()




