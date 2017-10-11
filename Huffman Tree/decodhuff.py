"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
def decodeHuff(root , s):
    k = root
    for i in s:
        if i == '1':
            k=k.right
            if k.right == None and k.left == None:
                sys.stdout.write(k.data)
                k=root
        else:
            k=k.left
            if k.right == None and k.left == None:
                sys.stdout.write(k.data)
                k = root
