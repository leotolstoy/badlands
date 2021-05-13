import numpy as np 


from demographics import DemographicsModel
from city import CityModel
from logisticBayesianModel import LogisticBayesianModel
from constantModel import ConstantModel
from constantRateModel import ConstantRateModel




class Importer():
	def __init__(self,p1,p2,p3):

		self.populationModel = ConstantRateModel(p1)
		self.turnoutModel = ConstantModel(p2)
		self.voteMarginModel = ConstantModel(p3)

		self.demographics = dict([\
			('college_ed',DemographicsModel(self.populationModel, self.turnoutModel, self.voteMarginModel)),\
			])  

		self.resetTimeDemographics('college_ed')

		
	def resampleDemographicsModel(self,key):
		self.demographics[key].sampleModel()

	def evaluateDemoModelAtTime(self, time, key):

		self.totalPopulation = self.demographics[key].populationModel.evalModelAtTime(time)
		self.turnout = self.demographics[key].turnoutModel.evalModelAtTime(time)
		self.voteMargin = self.demographics[key].voteMarginModel.evalModelAtTime(time)

		self.totalVotes = self.turnout * self.totalPopulation
		self.frac_dem = 0.5 + self.voteMargin/2
		self.frac_rep = 0.5 - self.voteMargin/2

		self.dem_votes = self.frac_dem * self.totalVotes
		self.rep_votes = self.frac_rep * self.totalVotes

		self.raw_margin = self.dem_votes - self.rep_votes

	def resetTimeDemographics(self,key):

		self.resampleDemographicsModels('college_ed')
		self.evaluateDemoModelAtTime(0, 'college_ed')

		


