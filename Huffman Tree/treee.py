m = ""
d = {}
class _Tree_node():
	def __init__(self):
		self.left = None
		self.right = None
		self.ch = False
		self.count = 0

def _traverse(root,value):
	global m
	global d
	m+=value
	if root.left == None or root.right == None:
		d[root.ch] = m
	else:
		_traverse(root.left,'0')
		m=m[:-1]
		_traverse(root.right,'1')
		m=m[:-1]

def _create_Tree(listt):
	while len(listt)>1:
		listt = sorted(listt,key=lambda x: x[1],reverse=True)
		a = _Tree_node()
		if len(listt[-1]) == 2:
			(x1,y1) = listt[-1]
			a.left = _Tree_node()
			a.left.ch = x1
			a.left.count = y1
		else:
			(x1,y1,z1) = listt[-1]
			a.left = z1
		if len(listt[-2]) == 2:
			(x2,y2) = listt[-2]
			a.right = _Tree_node()
			a.right.ch = x2
			a.right.count = y2
		else:
			(x2,y2,z2) = listt[-2]
			a.right = z2
		listt.pop()
		listt.pop()
		a.count = y1+y2
		listt.append((a.ch,a.count,a))
	return a
if __name__ == '__main__':
	l = [('b',11),('c',8),('d',12),('e',49)]
	gg = _create_Tree(l)
	_traverse(gg,"")
	print(d)
