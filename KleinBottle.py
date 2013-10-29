from SimplicialComplex import SimplicialComplex

if __name__ == '__main__':
	#Writing out the Klein bottle by hand
	c = SimplicialComplex(2)
	#Add vertices
	v = [0]
	for i in range(9):
		v.append(c.addFace())
	#Add edges
	e = [0]
	a = [1, 2, 2, 3, 3, 1, 1, 4, 1, 6, 4, 6, 2, 6, 6, 7, 2, 7, 3, 7, 7, 4, 3, 4, 4, 5, 5, 8, 4, 8, 6, 8, 8, 9, 6, 9, 7, 9, 9, 5, 7, 5, 5, 1, 5, 3, 8, 3, 8, 2, 9, 2, 9, 1]
	for i in range(len(a)/2):
		e.append(c.addFace([v[a[i*2]], v[a[i*2+1]]]))
	#Add faces
	a = [1, 7, 5, 4, 5, 6, 2, 10, 9, 7, 9, 8, 3, 4, 12, 10, 12, 11, 6, 16, 15, 15, 13, 14, 8, 19, 18, 18, 17, 16, 21, 11, 13, 19, 21, 20, 14, 24, 23, 22, 23, 1, 17, 26, 25, 25, 24, 2, 20, 22, 27, 27, 26, 3]
	for i in range(len(a)/3):
		c.addFace([e[a[i*3]], e[a[i*3+1]], e[a[i*3+2]]])
		
	for i in range(1, 3):
		print "Boundary Matrix %i"%i
		BMat = c.getBoundaryMatrix(i)
		print BMat
		print "Rank = %i\n\n"%BMat.getRank()
	
	for i in range(1, 3):
		print "B%i = %i"%(i, c.bettiNumber(i))

if __name__ == '__main__2':
	#Trying to procedurally generate Klein bottle but I think there's an 
	#error somewhere
	c = SimplicialComplex(2)
	#Create the vertices
	v = [0]#Add a dummy element so the indexing starts from 1 as in my writeup
	for i in range(0, 9):
		v.append(c.addFace())
	v = [ [v[1], v[2], v[3], v[1]], 
		[v[4], v[6], v[7], v[4]], 
		[v[5], v[8], v[9], v[5]], 
		[v[1], v[3], v[2], v[1]] ]
	#Now create the edges for the face cells
	faceCells = []
	for row in range(0, 3):
		a = [0, 0, 0]
		for col in range(0, 3):
			a[col] = [0, 0, 0, 0, 0]
		faceCells.append(a)
	print faceCells
	#Each face cell contains five edges
	#0 - Left
	#1 - Top
	#2 - Diagonal
	#3 - Right
	#4 - Bottom
	for i in range(0, 3):
		for j in range(0, 3):
			e = faceCells[i][j]
			v0 = v[i][j]
			v1 = v[i][j+1]
			v2 = v[i+1][j]
			v3 = v[i+1][j+1]
			#The diagonal is unique in each cell
			e[2] = c.addFace([v1, v2])
			if j == 0:
				e[0] = c.addFace([v0, v2])
			else:#Right of one cell overlaps left of next one over
				e[0] = faceCells[i][j-1][3]
			if i == 0:
				e[1] = c.addFace([v0, v1])
			else:#Bottom of one overlaps top of next one down
				e[1] = faceCells[i-1][j][4]
			if j < 2:
				e[3] = c.addFace([v1, v3])
			else:#Identify left side to right side
				e[3] = faceCells[0][j][0]
			if i < 2:
				e[4] = c.addFace([v2, v3])
			else:#Identify the bottom side to the twist of the top side
				e[4] = faceCells[0][2-j][1]
			
	#Now add the two faces in each cell
	for i in range(0, 3):
		for j in range(0, 3):
			e = faceCells[i][j]
			c.addFace([e[0], e[1], e[2]])
			c.addFace([e[2], e[3], e[4]])

	for i in range(1, 3):
		print "Boundary Matrix %i"%i
		BMat = c.getBoundaryMatrix(i)
		print BMat
		print "Rank = %i\n\n"%BMat.getRank()
	
	for i in range(1, 3):
		print "B%i = %i"%(i, c.bettiNumber(i))
