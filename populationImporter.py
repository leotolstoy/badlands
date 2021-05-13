import numpy as np 


from demographics import DemographicsModel
from city import CityModel
from logisticBayesianModel import LogisticBayesianModel
from constantModel import ConstantModel
from constantRateModel import ConstantRateModel




class Importer():

	def __init__(self,edu_model):
		self.edu_model = edu_model
		self.resetState()

	def evalImporterAtTime(self, time):
		self.edu_model.evaluateDemoModelAtTime(time)


	def resetImporter(self,)
		self.edu_model.resetDemographicsModel()
		self.evalImporterAtTime(0)

		


