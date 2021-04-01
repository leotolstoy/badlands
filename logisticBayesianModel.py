import numpy as np
import pickle
import pymc3 as pm
import arviz as az
from BayesianModel import BayesianModel
from timeModel import TimeModel

class LogisticBayesianModel(BayesianModel):



	# y = A/(1 + exp(-k*(x - x0))

	def __init__(self,pathToModel, pathToTrace):

		super().__init__(pathToModel, pathToTrace)
		self.var_names = ['y','A','k','x0']

		#try sampling just one sample
		self.sampleModel()


	# Intented to sample more than 1
	def sampleModelPPC(self,samples):
		super.sampleModelPPC(samples,self.var_names)

	# Sample one instance of the model
	def sampleModel(self,):
		ppc = sampleModelPPC(1)
		self.params = ppc
		return ppc

	def evalModelAtTime(self, time):
		A = self.params['A']
		k = self.params['k']
		x0 = self.params['x0']

		return A/(1 + np.exp(-k * (time - x0)))

	def evalModelRateAtTime(self, time):
		return -1



