#https://en.wikipedia.org/wiki/Sparse_matrix#Compressed_sparse_row_.28CSR.2C_CRS_or_Yale_format.29
class csr:
	def __init__(self):
		self.A = []
		self.IA = [0]
		self.JA = []
	def pack(self,M):
		count = 0
		for x,i in enumerate(M):
			count = 0
			for y,j in enumerate(i):
				if j!=0:
					self.A.append(j)
					count += 1
					self.JA.append(y)
			self.IA.append(self.IA[-1]+count)

if __name__ == '__main__':
	sp = csr()
	a = [[10,20,0,0,0,0],[0,30,0,40,0,0],[0,0,50,60,70,0],[0,0,0,0,0,80]]
	sp.pack(a)
	print(sp.A)
	print(sp.IA)
	print(sp.JA)
	
