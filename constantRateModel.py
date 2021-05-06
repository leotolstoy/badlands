import numpy as np



class ConstantRateModel():

	def __init__(self,constantRate):
		self.constantRateVal = constantRate

	# Sample one instance of the model
	def sampleModel(self,):
		return -1

	def evalModelAtTime(self, time):
		return self.constantRateVal * time
