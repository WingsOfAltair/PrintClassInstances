class PrintObject:
	def cleanVariableName(variableName, obj):return (variableName[0].replace('_'+obj.__class__.__name__,'').lstrip('_')+': '+str(variableName[1]))
	def __str__(self):return ', '.join(map(PrintObject.cleanVariableName,vars(self).items(),self))

class InheritingClass(PrintObject):
	def __init__(self):pass
	def __iter__(self):return self
	def __next__(self):return self