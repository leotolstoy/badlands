import numpy as np 


from demographics import DemographicsModel
from city import CityModel
from logisticBayesianModel import LogisticBayesianModel





class State():
	def __init__(self,p1,p2,p3):

		# TODO: make turnout model it's own bi-mean thing
		# TODO: make reg voter model, vote margin model, and population model polynomial/logistic/1st order, have them inherit from BayesianModel

		self.projectedPopulationModel = LogisticBayesianModel(p1)
		self.projectedTurnoutModel = LogisticBayesianModel(p2)
		# self.projectedRegVoterFracModel = LogisticBayesianModel(p3)
		self.projectedVoteMarginModel = LogisticBayesianModel(p3)

		# self.major_cities = [CityModel()]

		# We could potentially split up the 'projected' category into 'college_ed' and 'non_college_ed' categories, each with a 
		# separate model. 
		self.demographics = dict([\
			('projected',DemographicsModel(self.projectedPopulationModel, self.projectedTurnoutModel, self.projectedVoteMarginModel)),\
			])  

		self.resetTimeDemographics('projected')

	

	def resampleDemographicsModels(self,key):
		self.demographics[key].sampleModel()

	def evaluateDemoModelAtTime(self, time, key):

		self.totalPopulation = self.demographics[key].populationModel.evalModelAtTime(time)
		self.projectedTurnout = self.demographics[key].turnoutModel.evalModelAtTime(time)
		self.projectedVoteMargin = self.demographics[key].voteMarginModel.evalModelAtTime(time)

		self.totalVotes = self.projectedTurnout * self.totalPopulation
		self.frac_projected_dem = 0.5 + self.projectedVoteMargin/2
		self.frac_projected_rep = 0.5 - self.projectedVoteMargin/2

		self.projected_dem_votes = self.frac_projected_dem * self.totalVotes
		self.projected_rep_votes = self.frac_projected_rep * self.totalVotes

		self.projected_raw_margin = self.projected_dem_votes - self.projected_rep_votes


	def resetTimeDemographics(self,key):

		self.evaluateDemoModelAtTime(0, 'projected')
		

		self.yearToFlip = []















