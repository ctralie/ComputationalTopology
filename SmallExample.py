#This example seems to work
from SimplicialComplex import SimplicialComplex

if __name__ == '__main__':
	dim = 2
	c = SimplicialComplex(dim)
	#2 copies of two squares filled in with one triangle each
	for i in range(2):
		v0 = c.addFace()
		v1 = c.addFace()
		v2 = c.addFace()
		v3 = c.addFace()
		
		e0 = c.addFace([v0, v1])
		e1 = c.addFace([v1, v2])
		e2 = c.addFace([v2, v3])
		e3 = c.addFace([v3, v0])
		e4 = c.addFace([v3, v1])
		
		#f1 = c.addFace([e0, e4, e3])
		f1 = c.addFace([e4, e1, e2])

	for i in range(1, dim+1):
		print "Boundary Matrix %i"%i
		BMat = c.getBoundaryMatrix(i)
		print BMat
		print "Rank = %i\n\n"%BMat.getRank()
	
	for i in range(1, dim+1):
		print "B%i = %i"%(i, c.bettiNumber(i))