class Node:
	def __init__(self, l: int, r: int) -> None:
		self.count = [[0] * 5 for _ in range(5)] #Diana
		self.l = l
		self.r = r
		self.lson: Node = None
		self.rson: Node = None

	def mid(self)-> int:
		return (self.l + self.r) >> 1 


class Solution:
	def do(self, s: str) -> int:
		n = len(s)
		self.s = s
		rt =self.build(0, n - 1)
		# for (i, c) in enumerate(s):
		# 	self.update(rt, i, c)

		return rt.count[0][-1]

	def build(self, l: int, r: int) -> Node:
		rt = Node(l, r)
		if l == r:
			c = self.s[l]
			if c == 'D':
				rt.count[0][0] += 1
			elif c == 'i':
				rt.count[1][1] += 1
			elif c == 'a':
				rt.count[2][2] += 1
				rt.count[4][4] += 1
			elif c == 'n':
				rt.count[3][3] += 1
			return rt
		m = rt.mid()
		rt.lson = self.build(l, m)
		rt.rson = self.build(m + 1, r)
		self.pushUp(rt)
		return rt 

	def pushUp(self, rt: Node):
		for i in range(5):
			for j in range(5):
				rt.count[i][j] = rt.lson.count[i][j]
				rt.count[i][j] += rt.rson.count[i][j]
				for k in range(4):
					rt.count[i][j] += rt.lson.count[i][k] * rt.rson.count[k + 1][j]

				

S = Solution()

print(S.do('DbsaDiadasfanadaffdasa'))