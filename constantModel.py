import numpy as np



class ConstantModel():

	def __init__(self,constant):
		self.constantVal = constant
	# Sample one instance of the model
	def sampleModel(self,):
		return -1

	def evalModelAtTime(self, time):
		return self.constantVal
