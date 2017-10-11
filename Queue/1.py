########################################################################################################################################
#Sample Input
#10
#1 42
#2
#1 14
#3
#1 28
#3
#1 60
#1 78
#2
#2
#Sample Output
#14
#14
########################################################################################################################################
class queue:
	def __init__(self,length=100000):
		self.l = []
		self.max_length = length
		self.current_len = 0
		self.back = -1
	def enq(self,a):
		if self.back+1 < self.max_length:
			self.l.append(a)
			self.back += 1
			self.current_len += 1
	def dq(self):
		if self.current_len >= 0:
			temp = self.l[0]
			self.current_len -= 1
			del(self.l[0])
#			return temp
	def disp_front(self):
		if self.current_len >= 0:
			return self.l[0]
        
if __name__ == '__main__':
    a = queue()
    k = int(input())
    while k:
        k -=1
        s = [int(i) for i in input().split(' ')]
        if s[0] == 1:
            a.enq(s[1])
        elif s[0] == 2:
            a.dq()
        elif s[0] == 3:
            print(a.disp_front())
