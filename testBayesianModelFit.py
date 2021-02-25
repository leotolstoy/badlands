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



print('*** Start script ***')
print(f'{pm.__name__}: v. {pm.__version__}')
# print(f'{theano.__name__}: v. {theano.__version__}')

if __name__ == '__main__':
	np.random.seed(7000) 

	a_true = 2
	b_true = 3

	x = np.linspace(0,10)
	y = a_true + b_true * x

	# add noise
	noise = 1*np.random.randn(len(y))
	print(noise)
	y = y + noise

	fig = plt.figure()
	ax = plt.axes()
	ax.plot(x,y,'o')
	# plt.show()
	


	#PYMC3 magic
	with pm.Model() as basic_model:
		alpha = pm.Normal('alpha',mu=0,sd=10)
		beta = pm.Normal('beta',mu=0,sd=10)
		sigma = pm.HalfNormal('sigma',sd=10)


		#Likelihood function
		mu = alpha + beta*x
		y_likelihood = pm.Normal('y_like',mu=mu,sigma=sigma,observed=y)



		trace = pm.sample(2000, tune=500,cores=4,model=basic_model)

		summary = az.summary(trace, var_names=["alpha","beta","sigma"])
		print(summary)

		#sample posterior predictive
		ppc = pm.sample_posterior_predictive(trace, var_names=["alpha","beta","sigma"], model=basic_model)




		#plot posterior
		data_spp = az.from_pymc3(trace=trace, posterior_predictive=ppc)


		# joint_plt = az.plot_pair(data_spp, var_names=['JND', 'eps'], kind='kde', fill_last=False);
		# plt.show()
		trace_fig = az.plot_trace(trace,var_names=["alpha","beta","sigma"],figsize=(12, 8));
		# az.plot_ppc(data_spp);
		# plt.show()
		# fig, _ = plt.subplots()
		ax_posterior = az.plot_posterior(data_spp,
										 point_estimate='mean',
										 hdi_prob=0.95,
										 textsize=20,
										 round_to=4);



		#try sampling just one sample
		ppc1 = pm.sample_posterior_predictive(trace, samples = 1, var_names=["alpha","beta","sigma"], model=basic_model)
		print(ppc1)

		a_s = ppc1['alpha']
		b_s = ppc1['beta']

		y_s = a_s + b_s * x
		ax.plot(x,y_s,'b')

		plt.show()











	
