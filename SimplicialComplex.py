import numpy as np
from Mod2Matrix import Mod2Matrix

class SimplicialFace(object):
	def __init__(self, dim, children = None):
		self.dim = dim
		self.id = -1
		if children:
			self.children = children
		else:
			self.children = []

class SimplicialComplex(object):
	def __init__(self, maxDim):
		self.facesOfDim = []
		self.needsIDUpdate = True
		for i in range(0, maxDim+1):
			self.facesOfDim.append(set([]))
	
	#Assuming a simplicial face
	def addFace(self, children = None):
		dim = 0
		if children:
			dim = len(children)-1
		face = SimplicialFace(dim, children)
		self.facesOfDim[dim].add(face)
		self.needsIDUpdate = True
		return face
	
	def updateIDs(self):
		if self.needsIDUpdate:
			for dim in range(0, len(self.facesOfDim)):
				faces = self.facesOfDim[dim]
				ID = 0
				for face in faces:
					face.id = ID
					ID = ID + 1
				print "There are %i %i-simplices"%(ID, dim)
			self.needsIDUpdate = False
	
	def identifyFaces(self):
		print "TODO"
	
	#Boundary matrix from dim faces to dim-1 faces
	def getBoundaryMatrix(self, dim):
		if dim == 0:
			BMat = Mod2Matrix(1, len(self.facesOfDim[0]))
			BMat.a = [1]*len(self.facesOfDim[0])
			return BMat
		self.updateIDs()
		m = len(self.facesOfDim[dim])
		n = len(self.facesOfDim[dim-1])
		#BMat = np.matrix(np.zeros([n, m]))
		BMat = Mod2Matrix(n, m)
		for face in self.facesOfDim[dim]:
			for child in face.children:
				BMat.M[child.id][face.id] = 1
		return BMat
	
	def cyclesRank(self, dim):		
		BMat = self.getBoundaryMatrix(dim)
		#The dimension of the kernel of the boundary matrix from dim to dim-1
		#return BMat.shape[1] - np.linalg.matrix_rank(BMat)
		return len(self.facesOfDim[dim]) - BMat.getRank()
	
	def boundaryRank(self, dim):
		if dim >= len(self.facesOfDim):
			return 0
		BMat = self.getBoundaryMatrix(dim)
		#return np.linalg.matrix_rank(BMat)
		return BMat.getRank()
	
	def bettiNumber(self, dim):
		if dim == 0:
			return 1
		cyclesRank = self.cyclesRank(dim)
		boundaryRank = self.boundaryRank(dim+1)
		print "dim = %i, cyclesRank = %i, boundaryRank = %i"%(dim, cyclesRank, boundaryRank)
		return cyclesRank - boundaryRank
	
if __name__ == '__main__':
	c = SimplicialComplex(2)
	v1 = c.addFace()
	v2 = c.addFace()
	v3 = c.addFace()
	e1 = c.addFace([v1, v2])
	e2 = c.addFace([v2, v3])
	e3 = c.addFace([v3, v1])
	f = c.addFace([e1, e2, e3])
	for i in range(0, 3):
		print "Boundary Matrix %i"%i
		BMat = c.getBoundaryMatrix(i)
		print BMat
		print "Rank = %i\n\n"%BMat.getRank()
	for i in range(0, 3):
		print "B%i = %i"%(i, c.bettiNumber(i))
