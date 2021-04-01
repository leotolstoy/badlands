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

	a_true = 20
	b_true = 3

	x = np.linspace(0,10)
	y = a_true + b_true * x

	# add noise
	noise = 1*np.random.randn(len(y))
	print(noise)
	y = y + noise

	fig = plt.figure()
	ax = plt.axes()
	ax.plot(x,y,'ro')
	# plt.show()
	

	directory_name = 'testDir'


	#Load model
	
	

	with open(directory_name+'/model.pkl','rb') as buff:
		basic_model = pickle.load(buff)

	



	#PYMC3 magic
	with basic_model:

		# with open(directory_name+'/trace.pkl','rb') as buff:
		# 	trace = pickle.load(buff)

		trace = pm.load_trace(directory=directory_name)

		summary = az.summary(trace, var_names=["alpha","beta","sigma"])
		print(summary)

		#sample posterior predictive
		ppc = pm.sample_posterior_predictive(trace, var_names=["alpha","beta","sigma","y_like"], model=basic_model)




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

		# confidence intervals

		crit_l = np.percentile(ppc['y_like'],q=2.5,axis=0)
		crit_u = np.percentile(ppc['y_like'],q=97.5,axis=0)
		mean_spp = np.mean(ppc['y_like'],axis=0)
		print(len(crit_l))

		ax.fill_between(x,crit_l, crit_u,'b',alpha=0.2)
		ax.plot(x,mean_spp,'b',label='Mean')

		#try sampling just one sample
		ppc1 = pm.sample_posterior_predictive(trace, samples = 1, var_names=["alpha","beta","sigma"], model=basic_model)
		print(ppc1)

		a_s = ppc1['alpha']
		b_s = ppc1['beta']

		y_s = a_s + b_s * x
		ax.plot(x,y_s,'b')


		plt.show()












	
