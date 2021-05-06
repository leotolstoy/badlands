from timeModel import timeModel
from logisticBayesianModel import LogisticBayesianModel



class DemographicsModel():

	def __init__(self,populationModel, turnoutModel, regVoterFracModel, voteMarginModel):

		# All Bayesian Models
		self.populationModel = populationModel
		self.turnoutModel = turnoutModel
		self.regVoterFracModel = regVoterFracModel
		self.voteMarginModel = voteMarginModel

		self.sampleModel()


	def sampleModel(self,):

		self.populationModel.sampleModel()
		self.turnoutModel.sampleModel()
		self.regVoterFracModel.sampleModel()
		self.voteMarginModel.sampleModel()
