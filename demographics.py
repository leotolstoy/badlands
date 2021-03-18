from timeModel import timeModel
from bayesianModel import BayesianModel



class DemographicsModel():

	def __init__(self,populationModel, turnoutModel, regVoterModel, voteMarginModel):
		self.populationModel = populationModel
		self.turnoutModel = turnoutModel
		self.regVoterModel = regVoterModel
		self.voteMarginModel = voteMarginModel

		self.sampleModel()


	def sampleModel(self,):

		self.populationTimeModel = timeModel(self.populationModel.sample())
		self.turnoutTimeModel = timeModel(self.turnoutModel.sample())
		self.regVoterTimeModel = timeModel(self.regVoterModel.sample())
		self.voteMarginTimeModel = timeModel(self.voteMarginModel.sample())
