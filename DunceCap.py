from SimplicialComplex import SimplicialComplex

if __name__ == '__main__':
	#Writing out the Dunce cap by hand
	c = SimplicialComplex(2)
	v = []
	for i in range(10):
		v.append(c.addFace())
	a = [1, 2, 2, 3, 3, 4, 4, 1, 1, 5, 1, 6, 2, 5, 5, 6, 6, 2, 3, 5, 3, 7, 7, 5, 5, 8, 8, 6, 6, 9, 6, 0, 6, 3, 3, 0, 0, 4, 0, 1, 1, 9, 9, 4, 9, 3, 9, 8, 8, 3, 8, 2, 8, 1, 1, 7, 7, 8, 7, 4, 9, 0]
	e = [0]
	for i in range(len(a)/2):
		e.append(c.addFace([v[a[i*2]], v[a[i*2+1]]]))
	a = [1, 7, 5, 5, 8, 6, 6, 9, 1, 7, 2, 10, 12, 11, 7, 3, 11, 30, 30, 28, 4, 28, 27, 29, 1, 20, 2, 29, 12, 13, 13, 8, 14, 14, 15, 24, 20, 2, 25, 23, 24, 25, 31, 15, 16, 16, 17, 18, 9, 17, 2, 3, 18, 19, 19, 20, 4, 20, 31, 21, 21, 22, 4]
	for i in range(len(a)/3):
		c.addFace([e[a[i*3]], e[a[i*3+1]], e[a[i*3+2]]])
		
	for i in range(1, 3):
		print "Boundary Matrix %i"%i
		BMat = c.getBoundaryMatrix(i)
		print BMat
		print "Rank = %i\n\n"%BMat.getRank()
	
	for i in range(1, 3):
		print "B%i = %i"%(i, c.bettiNumber(i))	