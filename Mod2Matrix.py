import random

class Mod2Matrix(object):
	#Matrix is m x n
	def __init__(self, n, m):
		self.M = [0]*n
		for i in range(0, n):
			self.M[i] = [0]*m
		self.n = n
		self.m = m
		self.rank = -1
	
	def rref(self):
		#Adapted from http://rosettacode.org/wiki/Reduced_row_echelon_form#Python
		M = self.M
		lead = 0
		rowCount = len(M)
		columnCount = len(M[0])
		for r in range(rowCount):
			if lead >= columnCount:
				return
			i = r
			while M[i][lead] == 0:
				i += 1
				if i == rowCount:
					i = r
					lead += 1
					if columnCount == lead:
						return
			M[i],M[r] = M[r],M[i]
			lv = M[r][lead]
			for i in range(rowCount):
				if i != r:
					lv = M[i][lead]
					#Mod 2!
					M[i] = [ (iv - lv*rv)%2 for rv,iv in zip(M[r],M[i])]
			lead += 1
	
	#Find all of the zero rows
	def getRank(self):
		M = self.M
		if self.rank == -1:
			if self.n*self.m == 0:
				self.rank = 0
				return 0
			self.rref()
			zeroRows = 0
			for i in range(0, self.n):
				for j in range(0, self.m):
					if M[i][j] == 1:
						break
					elif j == self.m-1:
						zeroRows = zeroRows + 1
			self.rank = self.n - zeroRows
		return self.rank
	
	def __str__(self):
		a = []
		for row in self.M:
			a = a + row
		fmtstr = "%i "*self.m + "\n"
		fmtstr = fmtstr*self.n
		return fmtstr%tuple(a)

if __name__ == '__main__':
	#m = Mod2Matrix(2, 4)
	#m.M = [[0, 0, 1, 1], [0, 0, 1, 1]]
	#m = Mod2Matrix(3, 3)
	#m.M = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
	m = Mod2Matrix(4, 5)
	m.M = [[1, 0, 1, 0, 1], [0, 0, 0, 1, 1], [1, 1, 0, 0, 0], [0, 1, 1, 1, 0]]
	print m
	print "Rank %i"%m.getRank()
	print m

if __name__ == '__main__2':
	rows = 2
	cols = 5
	m = Mod2Matrix(rows, cols)
	m.a = [random.randint(0, 1) for i in range(0, rows*cols)]
	print m
	print "-----"
	m.rref()
	print "-----"
	print m
	print "Rank %i"%m.getRank()
	print m
