import numpy as np 


from demographics import DemographicsModel
from city import CityModel
from bayesianModel import BayesianModel





class State():
	def __init__(self,p1,p2,p3,p4):

		self.populationModel = BayesianModel(p1)
		self.turnoutModel = BayesianModel(p2)
		self.regVoterModel = BayesianModel(p3)
		self.voteMarginModel = BayesianModel(p4)

		# self.major_cities = [CityModel()]
		self.demographics = dict([\
			('college_ed',DemographicsModel()),\
			('overall',DemographicsModel()),\
			])  

		self.totalPopulation = self.demographics['overall'].populationTimeModel.evalModelAtTime(0)
		self.overallVoteMargin = self.demographics['overall'].voteMarginTimeModel.evalModelAtTime(0)
		self.overallRegVoter = self.demographics['overall'].regVoterTimeModel.evalModelAtTime(0)
		self.overallTurnout = self.demographics['overall'].turnoutTimeModel.evalModelAtTime(0)

		self.totalVotes = self.overallTurnout * self.overallRegVoter
		self.frac_overall_dem = 0.5 + self.overallVoteMargin/2
		self.frac_overall_rep = 0.5 - self.overallVoteMargin/2

		self.overall_dem_votes = self.frac_overall_dem * self.totalVotes
		self.overall_rep_votes = self.frac_overall_rep * self.totalVotes

		self.yearToFlip = []





