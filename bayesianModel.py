import numpy as np
import pickle
import pymc3 as pm
import arviz as az


# TODO: implement subclasses for logistic, cubic, bi-mean
class BayesianModel():

	def __init__(self,pathToModel, pathToTrace):

		with open(pathToModel,'rb') as buff:
			self.model = pickle.load(buff)
		self.trace = pm.load_trace(directory=pathToTrace, model=self.model)


	def sampleModelPPC(self,samples,var_names):
		self.ppc = pm.sample_posterior_predictive(self.trace, samples=samples, var_names=var_names, model=self.model)
		return self.ppc

	def plotPosterior(self,):
		self.data_spp = az.from_pymc3(trace=self.trace, posterior_predictive=self.ppc)
		ax_posterior = az.plot_posterior(self.data_spp,
										 point_estimate='mean',
										 hdi_prob=0.95,
										 textsize=20,
										 round_to=4);

