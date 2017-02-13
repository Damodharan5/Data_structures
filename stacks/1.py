##########################################################################################################################################
# Sample Input
# 10
# 1 97
# 2
# 1 20
# 2
# 1 26
# 1 20
# 2
# 3
# 1 91
# 3
# Sample Output
# 26
# 91
#########################################################################################################################################
class stack:
	def __init__(self):
		self.count = -1
		self.max_element = 0
		self.l = [] # Manipulating list as stack
	def push(self,x):
		self.count +=1
		if self.max_element < x:    #We can find max element like this also during pushing
			self.max_element = x
		self.l.append(x)
	def poppy(self):
		if self.count == -1:
			print("Empty :(")
		self.l.pop()
		self.count-=1
		if len(self.l) == 0:
			self.max_element = 0
		else:
			self.max_element = max(self.l)   # we can use max built-in fucntion also.

if __name__ == '__main__':
	n = int(input())
	s = stack()
	for i in range(n):
		k = [int(A) for A in input().split(" ")]
		if k[0] == 1:
			s.push(k[1])
		elif k[0] == 2:
			s.poppy()
		else:
			print(s.max_element)
