from timeModel import timeModel
from logisticBayesianModel import LogisticBayesianModel



class DemographicsModel():

	def __init__(self,populationModel, turnoutModel, regVoterModel, voteMarginModel):

		# All Bayesian Models
		self.populationModel = populationModel
		self.turnoutModel = turnoutModel
		self.regVoterModel = regVoterModel
		self.voteMarginModel = voteMarginModel

		self.sampleModel()


	def sampleModel(self,):

		self.populationModel.sampleModel()
		self.turnoutTimeModel.sampleModel()
		self.regVoterTimeModel.sampleModel()
		self.voteMarginTimeModel.sampleModel()
