import pymc3 as pm
import arviz as az
import numpy as np
from autograd import grad
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import glob
import pickle


# https://winderresearch.com/covid-19-hierarchical-bayesian-logistic-model-with-pymc3/
# https://winderresearch.com/covid-19-logistic-bayesian-model/

def logisticModel(A, k, x0, C, x):

	# y = A/(1 + exp(-k*(x - x0))
	y = A/(1 + np.exp(-k * (x - x0))) + C
	return y


print('*** Start script ***')
print(f'{pm.__name__}: v. {pm.__version__}')
# print(f'{theano.__name__}: v. {theano.__version__}')

if __name__ == '__main__':
	np.random.seed(7000) 

	C = 50
	A = 100
	x0 = 1
	k = -3

	x = np.linspace(0,10,100)
	y = logisticModel(A, k, x0, C, x)

	# add noise
	noise = 1*np.random.randn(len(y))
	# print(noise)
	y = y + noise

	fig = plt.figure()
	ax = plt.axes()
	ax.plot(x,y,'ro')
	# ax.plot(x,np.log(y),'ko')
	# plt.show()
	

	directory_name = 'testDir'


	#PYMC3 magic
	with pm.Model() as logistic_model:

		#set up priors

		C = pm.HalfNormal('C',sd=100) # This can't be negative
		A = pm.HalfNormal('A',sd=100) # This can't be negative
		k = pm.Normal('k',mu=0,sd=10)
		x0 = pm.Normal('x0',mu=0,sd=1)
		# sigma = pm.HalfNormal('sigma',sd=1)

		eps = pm.HalfNormal('eps',sd=10)

		growth = logisticModel(A, k, x0, C, x)
		y_pred = pm.Lognormal('y_pred', mu=np.log(growth), sigma=eps,observed=y)  # bringing it all together



		trace = pm.sample(4000, tune=2000,cores=4,model=logistic_model,init='adapt_diag')

		summary = az.summary(trace, var_names=['A','k','x0'])
		print(summary)

		#sample posterior predictive
		ppc = pm.sample_posterior_predictive(trace, var_names=['A','k','x0','C','y_pred'], model=logistic_model)




		#plot posterior
		data_spp = az.from_pymc3(trace=trace, posterior_predictive=ppc)


		# joint_plt = az.plot_pair(data_spp, var_names=['JND', 'eps'], kind='kde', fill_last=False);
		# plt.show()
		trace_fig = az.plot_trace(trace,var_names=['A','k','x0','C']);
		# az.plot_ppc(data_spp);
		# plt.show()
		# fig, _ = plt.subplots()
		ax_posterior = az.plot_posterior(data_spp,
										 point_estimate='mean',
										 hdi_prob=0.95,
										 textsize=20,
										 round_to=4);

		# confidence intervals

		crit_l = np.percentile(ppc['y_pred'],q=2.5,axis=0)
		crit_u = np.percentile(ppc['y_pred'],q=97.5,axis=0)
		mean_spp = np.mean(ppc['y_pred'],axis=0)
		print(len(crit_l))

		ax.fill_between(x,crit_l, crit_u,'b',alpha=0.2)
		ax.plot(x,mean_spp,'b',label='Mean')

		#try sampling just one sample
		ppc1 = pm.sample_posterior_predictive(trace, samples = 1, var_names=['A','k','x0','C'], model=logistic_model)
		print(ppc1)

		A_s = ppc1['A']
		k_s = ppc1['k']
		x0_s = ppc1['x0']
		C_s = ppc1['C']

		y_s = logisticModel(A_s, k_s, x0_s, C_s,x)
		ax.plot(x,y_s,'k')


		# Save model
		fname = pm.save_trace(trace=trace,directory=directory_name, overwrite='True')

		with open(directory_name+'/trace_logistic.pkl','wb') as buff:
			pickle.dump(trace,buff)

		with open(directory_name+'/model_logistic.pkl','wb') as buff:
			pickle.dump(logistic_model,buff)

		plt.show()












	
