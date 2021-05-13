import numpy as np 


from demographics import DemographicsModel
from city import CityModel
from logisticBayesianModel import LogisticBayesianModel





class State():
	def __init__(self,edu_model, no_edu_model, importer=importer):

		# We could potentially split up the 'projected' category into 'college_ed' and 'non_college_ed' categories, each with a 
		# separate model. 
		self.demographics = dict([\
			'college_ed',edu_model,\
			'non_college_ed',no_edu_model,\
			])  

		self.demo_keys = list(paramsDict.keys())
		self.importer = importer
		
		self.resetState()
		self.yearsToFlip = []

	def evalStateAtTime(self, time):

		demographics['college_ed'].evaluateDemoModelAtTime(time)
		demographics['non_college_ed'].evaluateDemoModelAtTime(time)
		# demographics['college_ed_projected'].evaluateDemoModelAtTime(time)
		# demographics['non_college_ed_projected'].evaluateDemoModelAtTime(time)

		# Update importer
		self.importer.evaluateImporterAtTime(time)
		self.importer_population_edu = self.importer.edu_model.totalPopulation
		self.importer_raw_margin = self.importer.edu_model.raw_margin


		# Tally up populations
		self.population_edu_proj = demographics['college_ed'].totalPopulation
		self.population_nedu_proj = demographics['non_college_ed'].totalPopulation

		self.population_edu = self.population_edu_proj + self.importer_population_edu
		self.population_nedu = self.population_nedu_proj

		# Could also be something along the lines of :
		# self.population_edu = f(self.population_edu)

		
		self.population_proj = self.population_edu_proj + self.population_nedu_proj
		self.population = self.population_edu + self.population_nedu


		# Tally up raw margins

		self.raw_margin_edu_proj = demographics['college_ed'].raw_margin
		self.raw_margin_nedu_proj = demographics['non_college_ed'].raw_margin

		self.raw_margin_edu = self.raw_margin_edu_proj + self.importer_raw_margin
		self.raw_margin_nedu = self.raw_margin_nedu_proj

		self.raw_margin_proj = self.raw_margin_edu_proj + self.raw_margin_nedu_proj
		self.raw_margin = self.raw_margin_edu + self.raw_margin_nedu


	def resetState(self,)
		for key in self.demo_keys:
			self.demographics[key].resetDemographicsModel()
		self.importer.resetImporterModel()

		self.evalStateAtTime(0)












