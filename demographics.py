from timeModel import timeModel
from logisticBayesianModel import LogisticBayesianModel



class DemographicsModel():

	def __init__(self,populationModel, turnoutModel, voteMarginModel):

		# All Bayesian Models
		self.populationModel = populationModel
		self.turnoutModel = turnoutModel
		self.voteMarginModel = voteMarginModel

		self.resetDemographicsModel()


	# Evaluate the current model at a time interval
	def evaluateDemoModelAtTime(self, time):

		self.totalPopulation = self.populationModel.evalModelAtTime(time)

		# In percent
		self.projectedTurnout = self.turnoutModel.evalModelAtTime(time)

		# In percent
		self.projectedVoteMargin = self.voteMarginModel.evalModelAtTime(time)

		self.totalVotes = self.projectedTurnout * self.totalPopulation
		self.frac_dem = 0.5 + self.projectedVoteMargin/2
		self.frac_rep = 0.5 - self.projectedVoteMargin/2

		self.dem_votes = self.frac_dem * self.totalVotes
		self.rep_votes = self.frac_rep * self.totalVotes

		self.raw_margin = self.dem_votes - self.rep_votes



	def resetDemographicsModel(self,):
		self.populationModel.sampleModel()
		self.turnoutModel.sampleModel()
		self.voteMarginModel.sampleModel()

		self.evaluateDemoModelAtTime(0)
