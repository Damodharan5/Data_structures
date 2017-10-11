########################################################################################################################################
#Input:
# 3
# {[()]}
# {[(])}
# {{[[(())]]}}
#Output:
# YES
# NO
# YES
########################################################################################################################################
import sys
br = {')':'(','}':'{',']':'['}

class stack:
	def __init__(self):
		self.l = []
		self.top = []
		self.currentpos = -1
		self.max_len = 1000 # 1000th element
	def internal(self,a):
		if self.currentpos+1 < self.max_len:
			self.currentpos += 1
			self.l.append(a)
			self.top = a
		else:
			print("Max reached ",self.max_len)
	def push(self,a):
		if(self.currentpos == -1):
			self.internal(a)
		elif(a in br.keys()):
			if self.top == br[a]:
				self.poppy()
		else:	
			self.internal(a)
	def poppy(self):
		if(self.currentpos == -1):
			print("Stack Empty")
		else:
			self.currentpos-=1
			self.top = self.l[self.currentpos]
			return self.l.pop()

if __name__ == '__main__':
	a = int(input())
	while(a):
		a -= 1
		b = input()
		s = stack()
		for i in b:
			s.push(i)
		print("YES") if (s.currentpos == -1) else print("NO")		
